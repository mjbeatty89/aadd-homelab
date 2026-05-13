---
type: concept
status: active
owner: matt
created: 2026-05-12
updated: 2026-05-13
tags: [schema, ontology, llm-wiki]
confidence: high
---

# Relationship Ontology

> Shared vocabulary for describing how notes connect.

## Relationship Types
| Relationship | Meaning | Inverse |
|--------------|---------|---------|
| `depends_on` | This thing requires the target to function or make sense. | `required_by` |
| `implements` | This thing is a concrete implementation of the target pattern/decision. | `implemented_by` |
| `extends` | This thing builds on the target without replacing it. | `extended_by` |
| `supersedes` | This thing replaces the target. | `superseded_by` |
| `blocks` | This thing prevents the target from progressing. | `blocked_by` |
| `monitors` | This thing observes health/state of the target. | `monitored_by` |
| `routes_to` | This thing forwards traffic or requests to the target. | `routed_from` |
| `documents` | This note is documentation for the target. | `documented_by` |
| `source_for` | This source supports or explains the target note. | `has_source` |
| `related` | Soft association when no stronger relationship applies. | `related` |

## Capacity Guideline
- Prefer 3-7 meaningful relationships per note.
- If a note needs more than 7 links, create an index or split the note.
- Avoid relationship lists that are only a dump of every mentioned term.

## Homelab Examples
- Oracle VPS `routes_to` Home Assistant through Caddy and Tailscale.
- Uptime Kuma `monitors` services, but alerts only for hardware, Home Assistant, and Frigate.
- CANTY VCM `implements` the intended home Tailscale subnet router role.
- Rental Home Assistant VM `depends_on` Proxmox VE and a separate Zigbee coordinator.

## Related
[[Schemas/LLM Wiki Schema]] · [[Projects/LLM Wiki Second Brain]]
