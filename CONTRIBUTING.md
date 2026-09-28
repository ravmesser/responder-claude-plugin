# Contributing

The repository root is the `rav-messer` Claude plugin. See README.md for the
layout and the corpus refresh flow.

- Never hand-edit `skills/responder-knowledge/references/articles/` or the generated
  index block in `SKILL.md` — rerun the crawler instead.
- Keep the plugin archive allowlist in `script/build.sh` in sync when adding
  top-level plugin files (e.g. `commands/`, `agents/`, `hooks/`).
- The patch version in `.claude-plugin/plugin.json` and `marketplace.json` is bumped
  by the refresh workflow; bump minor/major by hand for manual changes users should
  receive, keeping both files in sync.
- Run `./script/build.sh` (runs `claude plugin validate`) before pushing.
