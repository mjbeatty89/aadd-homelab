# Memory — em0lab

> Full second-brain entrypoint: [[Home]]
> AI operating rules: [[Resources/AI Operating Guide]]
> Host/service inventory: [[Resources/Host Inventory]] · [[Resources/Service Catalog]]
> LLM wiki schema: [[Schemas/LLM Wiki Schema]] · [[Schemas/Relationship Ontology]]

## LLM Wiki Rules
- Durable notes should use frontmatter and the note types in [[Schemas/LLM Wiki Schema]].
- Use templates in `Templates/` for wiki notes, ADRs, incidents, source captures, and homelab systems.
- Prefer typed relationship sections such as `Depends On`, `Implements`, `Extends`, `Supersedes`, and `Related`.
- Do not let agents write unstructured durable notes directly into the vault; raw captures belong in `Sources/Raw/` or `Logs/`.
- Mark uncertainty in [[Resources/Open Questions]] instead of blending guesses into inventories.
- High-risk infrastructure and guest-facing rental changes remain human-reviewed even if agents can update documentation.

## Me
Matt Miller. Chemical Engineer at GM — EV battery formation & offgassing for prismatic cells.
Ann Arbor, MI. Homeowner + attached rental suite (Ohana Suite). DIY, homelab, beginner coder.
GitHub: mjbeatty89

## Identity & Domains
| Term | Meaning |
|------|---------|
| **em0lab** | Homelab pet name |
| **AADD** | Ann Arbor Discreet Destinations — rental DBA |
| **aadd.rocks** | Primary domain — all services use *.aadd.rocks |
| **ha.aadd.rocks** | Home Assistant main instance |
| **Ohana Suite** | The attached guest house / rental unit |
| **manee-frog** | Tailscale network name — backup: *.manee-frog.ts.net |

## HA Room Agents
| Agent | Room |
|-------|------|
| Quinn | Living Room |
| Saffron | Kitchen |
| Vesper | Primary Bedroom |
| Axiom | Office |
| Kai | Ohana Suite (Rental) |

## Network Architecture
Two-box model: Oracle VPS (public) → Tailscale → Home Lab (private)

**VPS** (virtual-tunnel-vnic): 147.224.179.179, Tailscale: 100.67.166.50
- Caddy reverse proxy (auto-HTTPS) + Docker stack
- GitOps repo: /home/mjb/projects/vps-config (github: mjbeatty89/vps-config)
- VPS-local: n8n, Heimdall, Uptime Kuma, Portainer, Vaultwarden, Gitea (git.aadd.rocks), NTFY, Memos, Stirling PDF, 1Password Connect

**cashbox** (CachyOS container server): Tailscale 100.68.19.83, LAN 10.1.30.8
- Ryzen 5 7600X, 32GB RAM, 500GB NVMe
- GitOps repo: /home/mjb/projects/cash-compose (github: mjbeatty89/cash-compose)
- Running: obsidian:3002, obsidian-couchdb:5984, rxresume:3500, grafana:3001,
  influxdb:8086, loki:3100, redis:6379, postgres:5432, mongo:27017
- docker-mcp-gateway:8811 (SSE, 31 MCP servers — connected to Cowork as cashbox-docker)
- Telegraf (native systemd) → InfluxDB for host metrics

**Home hosts via Tailscale:**
- HA Pi5: 10.1.30.10 → ha.aadd.rocks
- CANTY VCM: 10.1.30.14 → pbs/pve-vcm.aadd.rocks (10 PoE ports, Tailscale bridge)
- unRAID: 10.1.30.16 → un.aadd.rocks
- Proxmox VE: 10.1.30.27 → pve.aadd.rocks
- TrueNAS: 10.1.31.70 → nas.aadd.rocks
- Frigate NVR: 10.1.30.18
- Ubuntu server: 10.1.11.129
- AdGuard DNS: 10.1.13.16
- AI server: being migrated to Ubuntu + Ansible (GPU rig)

**VLANs:** 10.1.10/11/13/20/30/31/40/50.x

## Obsidian / LiveSync Setup (Apr 2026)
- Container: obsidian.aadd.rocks (Caddy basic_auth user=mjb) → cashbox:3002 KasmVNC
- Shareable: proposal.aadd.rocks (Caddy basic_auth user=share)
- LiveSync CouchDB: cash:5984, db=obsidian-vault, user=obsidian
- From container: use URI http://obsidian-couchdb:5984 (Docker network)
- From local Mac: use URI http://100.68.19.83:5984 (Tailscale IP, more reliable than hostname)
- Credentials saved in cashbox: /home/mjb/projects/cash-compose/.credentials.txt

## SSH Setup
- 1Password SSH agent (can flood hosts with too many key attempts — known issue)
- Tailscale SSH preferred for reliable access
- Key aliases: ha, ubuntu, frigate, local-vcm, virtual-server-tunnel, spotify-pi

## Tech Terms
| Term | Meaning |
|------|---------|
| HUB75 | Standard RGB LED matrix panel interface |
| OpenHASP | LVGL touch panel custom component for HA |
| OpenClaw | Open-source autonomous AI agent sandbox (local models, no always-allow prompts) |
| Grafana | Observability platform (sometimes written "Garfana") |
| CYD | Cheap Yellow Display (ESP32-2432S028) |
| DIF checker | Recursive multimodal diff checker (Codex orch project) |
| CANTY VCM | Mini-PC with 10 PoE ports, acts as local Tailscale subnet router + PBS |
| k3s | Lightweight Kubernetes — Matt building 5-node Pi5 cluster |
| GitOps | Goal: operate one server purely via git-driven deployments |

## Active Projects
| Project | Status |
|---------|--------|
| 2026 Taxes | Due 4/10 — Quicken output + rental writeoffs |
| Resume + Website | Due ASAP — static site with dashboards/infra views |
| Matrix LED (rectangular) | RPi Zero 2W + HUB75 — blocked on LED lib deps |
| Matrix LED (Spotify viewer) | M4 + HUB75 — blocked on MicroPython |
| Codex Orchestration | OpenClaw downstream models + multimodal diff checker |
| HA Dashboards | Per-room tablets + camera hub + info hub |
| k3s cluster | 5-node Pi5 cluster in progress |
| ai.aadd.rocks | Needs backend refresh; AI server now at 10.1.30.9 |
| Grafana observability | Deployed on cashbox, needs HA + Pi data sources |
| OpenHASP light controller | Room light panel — config went sideways |
| Rental DIY | Flooring transitions, over-toilet organizer, tub jets |
| AI server Ubuntu migration | Wipe Arch/Garuda, partition /home separately, then Ansible |
| Ansible IaC | First playbook: AI server (GPU drivers, Docker, Tailscale, SSH hardening) |

## Preferences
- Likes proactive suggestions and initiative
- Beginner coder — explain things clearly, don't assume deep syntax knowledge
- Interested in Codex orchestration / multi-agent systems
- Cowork mode preferred over OpenClaw for Codex agent work
- Wants most work pushed to GitHub (mjbeatty89)
- GitOps goal: one server driven purely by git commits


<claude-mem-context>
# Memory Context

# [em0lab_vault] recent context, 2026-05-13 8:36am EDT

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 25 obs (10,380t read) | 362,493t work | 97% savings

### May 2, 2026
1 10:46a ⚖️ Homelab Second Brain Documentation Project Initiated
2 " 🔵 Obsidian Vault Structure Mapped
3 " 🔵 Vault Has Smart Connections Plugin and Is Not Git-Tracked
4 10:47a 🔵 AGENTS.md Is the Existing AI Memory Document for em0lab
5 " 🔵 Areas/Homelab.md Is a Stub — Second Brain Gap Identified
6 " 🔵 Network Map.md Contains Most Detailed Infrastructure Inventory
7 10:48a 🔵 Home Assistant Has Dual-Instance Setup with Rich Custom Component Stack
8 " 🔵 Two Specific Caddyfile Bugs Documented with Exact Fixes
9 " 🔵 TASKS.md Contains AI Server Rebuild Plan with Specific Model and GPU Targets
10 " ⚖️ Second Brain Architecture Plan: Spine + Entrypoint + Runbooks + Templates
11 10:49a 🟣 Homelab Second Brain Spine Created — 5 New Files, 5 Updated
12 " 🔵 Consistency Audit Found Stale images/Home.md and Pending TBD Entries
13 10:50a 🔵 Live Tailscale Status Reveals AI Server Is Online and Frigate IP Is Wrong in Docs
14 10:51a 🔵 Full Tailscale Node Inventory with Live Status
15 " 🔵 Dev Directory Layout Reveals Active Local Projects and AI Model Cache
16 " 🟣 Host Inventory Updated with Live Tailscale Data; Two New Resource Files Added
### May 12, 2026
17 5:53a 🔵 Homelab "Second Brain" Documentation Project Initiated
18 5:54a 🔵 em0lab Obsidian Vault Structure Surveyed
19 " ✅ Mass Vault Accuracy Pass — 12 Files Updated with Confirmed Facts
40 8:38a 🔵 Homelab Second Brain Documentation Project Initiated
41 " 🔵 em0lab Obsidian Vault Already Has Substantial Second Brain Structure
42 " 🔵 Matt Miller Homelab Identity and Network Architecture Captured in CLAUDE.md
43 8:39a 🔵 em0lab Vault Installed Plugins and Frontmatter Usage Inventory
44 " ✅ New Second Brain Directory Structure Created in Vault
45 8:41a 🟣 LLM Wiki Second Brain Architecture Scaffolded in em0lab Vault

Access 362k tokens of past work via get_observations([IDs]) or mem-search skill.
</claude-mem-context>
