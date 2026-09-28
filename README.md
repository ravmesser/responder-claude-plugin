# Responder plugin for Claude

Bundles everything a Claude user needs to work with the Responder / Rav Messer
(רב מסר) email-marketing platform:

- **`responder-knowledge` skill** — an offline mirror of the official help center
  (topical references + the full article corpus), plus a classification router that
  maps a request to the right product area (lists, series, forms, landing pages,
  SMS, integrations, statistics…). Works with no internet access.
- **`responderai` MCP server** — the hosted Responder API at
  `https://ai.responder.live/mcp`: manage lists, subscribers, tags, email series,
  drafts and sending, forms, landing pages, senders, the blocklist and statistics.

## Install

In Claude Code:

```
/plugin marketplace add ravmesser/responder-claude-plugin
/plugin install responder@responder
```

Or download `responder-plugin.zip` from the [latest release][releases] and upload
it at [claude.ai/customize/plugins](https://claude.ai/customize/plugins), or load it
directly with `claude --plugin-dir responder-plugin.zip`.

[releases]: https://github.com/ravmesser/responder-claude-plugin/releases/latest

## Authorize the MCP server

The MCP server uses OAuth. After installing, run `/mcp`, pick `responderai`, and
complete the browser login with your Responder account. Skill-only usage (asking
"how do I…" questions) needs no authorization.

## Layout

The repository root is the plugin:

```
.claude-plugin/plugin.json       plugin manifest
.claude-plugin/marketplace.json  single-plugin marketplace pointing at ./
.mcp.json                        responderai MCP server definition
skills/responder-knowledge/      the skill
  references/*.md                curated topical references
  references/articles/           crawled help-center corpus (generated)
  scripts/sync_articles.py       the crawler
script/build.sh                  builds dist/*.zip and validates the manifests
.github/workflows/refresh.yml    weekly crawl → commit → release
```

## Refreshing the corpus

The `Refresh and release` workflow runs every Sunday and can be started by hand
(`gh workflow run refresh.yml`). It re-crawls the help center and, when articles
changed, bumps the patch version, commits to `main` and publishes a release with
both archives.

To do it locally:

```sh
python3 -m venv .venv
.venv/bin/pip install -r skills/responder-knowledge/scripts/requirements.txt
.venv/bin/python skills/responder-knowledge/scripts/sync_articles.py
./script/build.sh
```

The crawler starts at `https://support.responder.co.il/portal/he/kb/responderlive`,
extracts every article with Trafilatura, atomically replaces
`references/articles/` (a failed crawl leaves the previous corpus in place), writes
the catalog to `references/articles/INDEX.md`, updates the generated block in
`SKILL.md`, and rewrites official article URLs in the curated references into links
to the local copies. Use `--delay SECONDS` to change the delay between requests.

Do not hand-edit `references/articles/` or the block between
`BEGIN GENERATED OFFLINE ARTICLE INDEX` and `END GENERATED OFFLINE ARTICLE INDEX`
in `SKILL.md`; the next crawl replaces them. The other files in `references/` are
curated and edited normally.
