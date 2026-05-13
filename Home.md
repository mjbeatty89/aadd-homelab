# em0lab — Homelab Second Brain

> Start here. This vault is the working memory for Matt's home lab, smart home, rental suite, and local AI environment.

## Fast Orientation
- Matt is a beginner coder with a serious homelab: explain clearly, move carefully, and prefer reversible changes.
- Primary domain: `aadd.rocks`; backup Tailscale domain: `*.manee-frog.ts.net`.
- Architecture pattern: public Oracle VPS reverse proxy -> Tailscale -> private home services.
- Home Assistant is important but split by risk: main instance is experimental; rental / Ohana Suite automation should be treated as stable guest-facing infrastructure.
- Secrets live in 1Password. Do not invent, print, or store credentials in notes.

## AI Onboarding Path
Read these in order when a new AI model or agent joins the environment:

1. [[Resources/AI Operating Guide]] — how to act safely in this homelab.
2. [[Resources/Network Map]] — network topology, VLANs, hosts, and public service routing.
3. [[Resources/Host Inventory]] — what each machine does and where its source of truth lives.
4. [[Resources/Service Catalog]] — services, URLs, ports, backends, and ownership.
5. [[Resources/Tailscale Snapshot]] — live overlay-network peer snapshot.
6. [[Resources/Dev Workspace Map]] — local development folders and repo orientation.
7. [[Resources/Runbooks]] — repeatable checks and maintenance procedures.
8. [[Resources/Glossary]] — local names, acronyms, and project shorthand.
9. [[Resources/Open Questions]] — uncertainty that needs Matt or live-system confirmation.
10. [[Projects/LLM Wiki Second Brain]] — project to make this vault agent-maintained and schema-checked.

## Main Areas
- [[Areas/Homelab]] — servers, networking, Docker, Kubernetes, observability, AI infrastructure.
- [[Areas/Home Assistant]] — smart home, room agents, ESPHome, dashboards, voice, sensors.
- [[Areas/Rental Suite]] — Ohana Suite / AADD guest-facing systems and physical projects.

## Active Projects
- [[Projects/Claude Orchestration]] — multi-model orchestration and local agent sandboxing.
- [[Projects/Matrix LED - Rectangular Display]] — Raspberry Pi Zero 2W + HUB75 display.
- [[Projects/Matrix LED - Spotify Viewer]] — Matrix Portal M4 + HUB75 album art viewer.
- [[Projects/Resume and Website]] — static site with dashboard / infrastructure views.
- [[Projects/Magic Mirror]] — mirror dashboard deployment.
- [[Projects/LLM Wiki Second Brain]] — Obsidian as local LLM wiki / developer second brain.

## Operational Priorities
- Move infrastructure toward GitOps: server state should be reconstructable from repos and playbooks.
- Build Ansible/IaC while changes are fresh, especially for the AI server and Pi cluster.
- Keep guest-facing rental systems stable and isolated from experimental automation.
- Improve observability with Grafana, InfluxDB, Loki, Telegraf, Home Assistant metrics, and n8n alerts.

## Inbox For Future Notes
Use [[Templates/Homelab System Note]] when documenting a new host, service, integration, or project.
Use [[Templates/Wiki Note]], [[Templates/ADR]], [[Templates/Incident]], and [[Templates/Source Capture]] for durable agent-maintained knowledge.

Unresolved infrastructure questions are tracked in [[Resources/Open Questions]].
