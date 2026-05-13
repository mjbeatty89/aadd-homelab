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

# [em0lab_vault] recent context, 2026-05-13 9:38am EDT

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision 🚨security_alert 🔐security_note
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 38 obs (15,017t read) | 464,292t work | 97% savings

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
### May 13, 2026
46 8:36a 🔵 Homelab Second Brain Documentation Project Initiated
47 8:37a 🔵 em0lab Obsidian Vault Structure Fully Surveyed
48 " 🔵 Second Brain Project Has Been Attempted Multiple Times — History in AGENTS.md
49 " 🔵 Homelab Service Infrastructure Identified from Vault Reference Scan
50 " 🔵 Active Homelab Project Backlog Captured from To Do List and Projects
51 " 🟣 Vault Bootstrapped as Proper Git Project with .gitignore, README, and wiki_health.py
52 8:38a 🟣 Vault Now Has Its Own Git Repository — Separate from Home Dir Repo
53 " 🟣 wiki_health.py Iteratively Debugged and Passes Clean — Broken Wikilink in Home.md Fixed
54 " 🟣 Initial Git Commit Made — 47 Files, 2095 Lines Committed to "Initialize homelab second brain"
55 8:39a 🟣 Vault Pushed to GitHub — Remote Repo at mjbeatty89/aadd-homelab
56 " 🟣 GitHub Actions CI Added — wiki-health.yml Runs on Every Push and PR
57 " 🟣 MkDocs + GitHub Pages Publishing Pipeline Added to Vault
58 8:40a 🔵 MkDocs Local Build Fails — docs_dir Cannot Equal Config File Directory
S1 Expand em0lab Obsidian vault into a full homelab "second brain" with git backing, CI, and web publishing for AI model consumption (May 13 at 8:40 AM)
**Investigated**: - Full vault structure at /Volumes/mm2ssd/mjb/Documents/obsidian/em0lab_vault surveyed: Areas, Projects, Resources, Schemas, Templates, Wiki, images, memory, Daily Notes, Sources directories
    - AGENTS.md session history confirmed this is the 3rd iteration of this project (prior sessions May 2 and May 12, 2026 already built substantial structure)
    - 362k tokens of prior work logged in AGENTS.md via claude-mem
    - Smart Connections plugin active with .ajson embeddings for all notes in .smart-env/multi/
    - Vault was previously part of the parent home dir git repo at /Volumes/mm2ssd/mjb, not independently tracked
    - Credential scan confirmed no secrets in vault notes; all stored in 1Password and cashbox:/home/mjb/projects/cash-compose/.credentials.txt
    - Active homelab services: obsidian.aadd.rocks (KasmVNC via Caddy), CouchDB LiveSync on cashbox:5984, Vaultwarden on Oracle VPS
    - Active project backlog: HA per-room AI agents, Claude orchestration, matrix LED displays, Kubernetes, AI server fix (Garuda Linux GPU issue), personal website
    - gh CLI not installed on Mac Mini
    - Local Python is 3.9 (system); CI targets 3.12

**Learned**: - MkDocs does not allow docs_dir to equal the parent directory of mkdocs.yml — config must reference a child directory
    - MkDocs also rejects site_dir inside docs_dir (infinite loop prevention)
    - The fix path: generate a temporary .site-src/ directory from tracked markdown, then point docs_dir at that for the build
    - Excluding a file from git (.gitignore) breaks any wikilinks pointing to it; discovered when `Home.md` still linked to `Projects/2026 Taxes.md` after that file was gitignored
    - Projects/Proposal/Mal Engagement.md uses image wikilinks (.jpg) that break wiki_health.py unless the entire Proposal directory is path-excluded
    - IGNORED_PATHS must use tuple prefix matching, not simple directory name matching, to exclude files two levels deep
    - mkdocs-roamlinks-plugin emits a DeprecationWarning on MkDocs 1.2+ but is non-fatal
    - Material for MkDocs has flagged MkDocs 2.0 as potentially breaking the plugin system entirely (noted for future awareness)

**Completed**: - Created .gitignore (excludes .smart-env, .obsidian/plugins, workspace.json, images/*, Projects/Proposal/, Projects/2026 Taxes.md, all credential patterns, .site, .venv, .tmp)
    - Created .gitattributes (LF line endings for md/json/yml/yaml/sh/py)
    - Created README.md (agent onboarding doc identifying canonical entry points)
    - Created scripts/wiki_health.py (frontmatter checker for Wiki/ and Schemas/ dirs, broken wikilink scanner, IGNORED_PATHS for private dirs)
    - Added frontmatter to Projects/LLM Wiki Second Brain.md, Schemas/LLM Wiki Schema.md, Schemas/Relationship Ontology.md
    - Fixed `Home.md` to remove the broken link to `Projects/2026 Taxes.md`
    - wiki_health.py passes clean: 36 files checked, exit 0
    - git init created dedicated vault repo (separate from home dir repo)
    - git add + initial commit: "Initialize homelab second brain" — SHA cba077a, 47 files, 2095 insertions
    - git remote added: https://github.com/mjbeatty89/aadd-homelab.git
    - Pushed to GitHub (cba077a → main)
    - Created .github/workflows/wiki-health.yml (CI runs wiki_health.py on every push/PR, Python 3.12, ubuntu-latest) — committed as SHA 2fd822d and pushed
    - Created mkdocs.yml with Material theme, roamlinks plugin, full nav structure covering all vault sections
    - Created .github/workflows/pages.yml (builds MkDocs site, runs wiki_health.py, deploys to GitHub Pages on push to main)

**Next Steps**: Fixing the MkDocs docs_dir configuration error: generating a temporary .site-src/ directory populated from tracked markdown files so that mkdocs.yml can reference a proper child directory as docs_dir rather than the vault root itself. This keeps the Obsidian vault layout unchanged while satisfying MkDocs' directory requirements. After the build passes locally, the fix will be committed and pushed so the pages.yml GitHub Actions workflow can successfully deploy to https://mjbeatty89.github.io/aadd-homelab/.


Access 464k tokens of past work via get_observations([IDs]) or mem-search skill.
</claude-mem-context>
