# Contributing

The `rav-messer` Claude plugin lives in `plugins/rav-messer/`; everything else is
repo tooling that does not ship. See README.md for the
layout and the corpus refresh flow.

- Never hand-edit `plugins/rav-messer/skills/responder-knowledge/references/articles/` or the generated
  index block in `SKILL.md` — rerun the crawler instead.
- Keep executable tooling out of `plugins/rav-messer/`: the plugin directory
  scans everything in it.
- The patch version in `plugins/rav-messer/.claude-plugin/plugin.json` and `marketplace.json` is bumped
  by the refresh workflow; bump minor/major by hand for manual changes users should
  receive, keeping both files in sync.
- Run `./script/build.sh` (runs `claude plugin validate`) before pushing.
