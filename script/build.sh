#!/usr/bin/env bash
# Build the release archives into dist/ and validate the manifests.
#
#   dist/responder-plugin.zip           the plugin, for claude.ai/customize/plugins
#   dist/responder-knowledge-skill.zip  the skill alone, for claude.ai/customize
#
# Run from anywhere after refreshing the corpus with
# skills/responder-knowledge/scripts/sync_articles.py (which also writes the
# skill archive this script copies).
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

[ -d skills/responder-knowledge/references/articles ] || {
  echo "missing article corpus: run skills/responder-knowledge/scripts/sync_articles.py" >&2
  exit 1
}

# Built with python zipfile, not the `zip` CLI: the article corpus has Hebrew
# filenames, and `zip` stores them without the UTF-8 name flag (bit 11), so
# strict readers decode the bytes as CP437 and reject the archive with
# "Zip file contains path with invalid characters". zipfile sets the flag.
mkdir -p dist
python3 script/build_plugin_zip.py dist/responder-plugin.zip rav-messer \
  .claude-plugin/plugin.json .claude-plugin/icon.svg .mcp.json README.md LICENSE \
  skills/responder-knowledge

if [ -f skills/responder-knowledge.zip ]; then
  cp skills/responder-knowledge.zip dist/responder-knowledge-skill.zip
fi

if command -v claude >/dev/null 2>&1; then
  claude plugin validate .claude-plugin/plugin.json
  claude plugin validate "$root"
fi
