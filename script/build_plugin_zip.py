#!/usr/bin/env python3
"""Zip a plugin directory with UTF-8 encoded entry names.

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
    src = Path(sys.argv[1]).resolve()
    dest = Path(sys.argv[2]).resolve()
    tmp = dest.with_suffix(".zip.tmp")

    files = sorted(
        p
        for p in src.rglob("*")
        if p.is_file()
        and p.name not in EXCLUDED_NAMES
        and not EXCLUDED_DIRS & set(p.relative_to(src).parts)
    )

    with ZipFile(tmp, "w", ZIP_DEFLATED) as archive:
        for path in files:
            # NFC-normalize: macOS hands back decomposed names, which some
            # readers treat as different (or invalid) paths.
            arcname = unicodedata.normalize("NFC", str(src.name / path.relative_to(src)))
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
