#!/usr/bin/env bash
# Build the release archives into dist/ and validate the manifests.
#
#   dist/responder-plugin.zip           the plugin, for claude.ai/customize/plugins
#   dist/responder-knowledge-skill.zip  the skill alone, for claude.ai/customize
#
# Run after refreshing the corpus with script/sync_articles.py (which also
# writes the skill archive this script copies).
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
plugin=plugins/rav-messer
skill=$plugin/skills/responder-knowledge

[ -d $skill/references/articles ] || {
  echo "missing article corpus: run script/sync_articles.py" >&2
  exit 1
}

# Stage the plugin with the repo-level README and LICENSE.
stage=dist/stage/rav-messer
rm -rf dist/stage
mkdir -p $stage
cp -a $plugin/. $stage/
rm -f $stage/skills/*.zip
cp README.md LICENSE $stage/

# Built with python zipfile, not the `zip` CLI: the article corpus has Hebrew
# filenames, and `zip` stores them without the UTF-8 name flag (bit 11), so
# strict readers decode the bytes as CP437 and reject the archive with
# "Zip file contains path with invalid characters". zipfile sets the flag.
python3 script/build_plugin_zip.py $stage dist/responder-plugin.zip
rm -rf dist/stage

if [ -f $skill.zip ]; then
  cp $skill.zip dist/responder-knowledge-skill.zip
fi

if command -v claude >/dev/null 2>&1; then
  claude plugin validate $plugin
  claude plugin validate "$root"
fi
