---
type: concept
status: active
owner: matt
created: 2026-05-12
updated: 2026-05-13
tags: [schema, llm-wiki, obsidian]
confidence: high
---

# LLM Wiki Schema

> Agent-facing conventions for writing durable notes in this vault.

## Core Rule
Every durable wiki note should have YAML frontmatter and a clear role. If a note is only a scratchpad, put it in `Sources/Raw/` or `Logs/` instead of the durable wiki.

## Required Frontmatter

```yaml
---
type: infrastructure | service | concept | decision | incident | project | source | index
status: draft | active | stable | deprecated | archived
owner: matt
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
---
```

## Optional Frontmatter

```yaml
source:
aliases: []
depends_on: []
implements: []
extends: []
supersedes: []
related: []
confidence: high | medium | low
```

## Note Types
| Type | Use For | Preferred Folder |
|------|---------|------------------|
| `infrastructure` | Hosts, networks, storage, gateways, clusters | `Wiki/Infrastructure/` |
| `service` | Apps, ports, URLs, integrations, monitoring | `Wiki/Infrastructure/` |
| `concept` | Reusable ideas or patterns | `Wiki/Concepts/` |
| `decision` | ADRs and durable design choices | `Wiki/Decisions/` |
| `incident` | Outages, breakage, recovery, lessons | `Wiki/Incidents/` |
| `project` | Multi-step work with tasks and outcomes | `Projects/` |
| `source` | Captured external article, transcript, or raw material | `Sources/` |
| `index` | Maps, dashboards, lists, navigation pages | Anywhere appropriate |

## Relationship Rules
- Prefer typed relationship sections over vague link piles.
- Use `Depends On`, `Implements`, `Extends`, `Supersedes`, and `Related` sections when the relationship matters.
- Keep cross-links selective. A useful note should usually link to 3-7 high-value neighbors, not every possible mention.
- If a relationship has operational consequences, describe the consequence in one sentence.

## Write Rules For Agents
1. Read [[Home]], [[Resources/AI Operating Guide]], and this schema before durable edits.
2. Use a template from `Templates/` when creating durable notes.
3. Do not paste secrets, tokens, passwords, private keys, or one-time codes.
4. Mark uncertain facts with `confidence: low` or put them in [[Resources/Open Questions]].
5. Update indexes or parent notes when adding durable notes.
6. Run a link/frontmatter health check when available.
7. Summarize what changed at the end of the session.

## Related
[[Projects/LLM Wiki Second Brain]] · [[Schemas/Relationship Ontology]] · [[Templates/Wiki Note]] · [[Templates/ADR]]
