# AADD Homelab Second Brain

This repository is the Git-backed source for Matt Beatty's em0lab / AADD homelab knowledge base.

Start here:

- [Home.md](Home.md)
- [AGENTS.md](AGENTS.md)
- [CLAUDE.md](CLAUDE.md)
- [Resources/AI Operating Guide.md](Resources/AI%20Operating%20Guide.md)
- [Projects/LLM Wiki Second Brain.md](Projects/LLM%20Wiki%20Second%20Brain.md)

## Purpose

- Keep durable homelab knowledge in local-first markdown.
- Let AI agents read and maintain the wiki using schemas and templates.
- Support GitOps/IaC workflows for service additions and infrastructure updates.
- Publish a private web wiki later without making local Obsidian the bottleneck.

## Agent Rules

Agents should read `Home.md`, `Resources/AI Operating Guide.md`, and `Schemas/LLM Wiki Schema.md` before durable edits.

Do not commit secrets, tokens, private keys, local plugin caches, Smart Connections embeddings, proposal images, or tax notes.

## Health Check

Run:

```bash
python3 scripts/wiki_health.py
```

The first version checks for basic frontmatter coverage on durable wiki files and broken wikilinks.

