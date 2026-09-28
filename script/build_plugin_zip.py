#!/usr/bin/env python3
"""Zip the plugin with UTF-8 encoded entry names.

Usage: build_plugin_zip.py DEST PREFIX PATH...

Packs each PATH (a file or directory, relative to the repo root) under the
top-level folder PREFIX. The plugin lives at the repo root next to repo-only
files (.github, script, ...), so the contents are an explicit allowlist.

The `zip` CLI omits the UTF-8 name flag, which makes readers mis-decode the
Hebrew article filenames in the responder-knowledge skill. zipfile always sets
flag bit 11 for non-ASCII names, so archives built here unpack correctly on
every platform.
"""

import sys
import unicodedata
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

EXCLUDED_NAMES = {".DS_Store"}
EXCLUDED_DIRS = {"__pycache__"}


def main() -> int:
    dest = Path(sys.argv[1]).resolve()
    prefix = sys.argv[2]
    root = Path.cwd()
    tmp = dest.with_suffix(".zip.tmp")

    files = []
    for entry in sys.argv[3:]:
        path = root / entry
        files.extend([path] if path.is_file() else path.rglob("*"))
    files = sorted(
        p
        for p in files
        if p.is_file()
        and p.name not in EXCLUDED_NAMES
        and not EXCLUDED_DIRS & set(p.relative_to(root).parts)
    )

    with ZipFile(tmp, "w", ZIP_DEFLATED) as archive:
        for path in files:
            # NFC-normalize: macOS hands back decomposed names, which some
            # readers treat as different (or invalid) paths.
            arcname = unicodedata.normalize("NFC", str(prefix / path.relative_to(root)))
            archive.write(path, arcname)

    tmp.replace(dest)

    with ZipFile(dest) as archive:
        infos = archive.infolist()
        unflagged = [
            i.filename
            for i in infos
            if any(ord(c) > 127 for c in i.filename) and not i.flag_bits & 0x800
        ]
        if unflagged:
            print(f"error: {len(unflagged)} entries lack the UTF-8 flag", file=sys.stderr)
            return 1
        longest = max(len(i.filename) for i in infos)

    print(f"built {dest} ({len(infos)} entries, longest path {longest} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
