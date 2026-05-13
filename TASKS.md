# Tasks

## Hardware Week — Apr 20–22 (Mal arrives Thu Apr 23)

> Goal: hardware out of sight by Thursday. AI server first so a local model can offload work for the rest of the week.

### Mon Apr 20 — AI server rebuild, phase 1
- [ ] Relocate AI server to final spot (clear from work surfaces)
- [ ] Back up anything worth keeping off current Garuda install
- [ ] Flash Ubuntu Server 24.04 LTS installer USB
- [ ] Partition scheme: `/` (100GB), `/home` (separate, rest of NVMe minus swap), swap (32GB matching RAM), optional `/var/lib/docker` carve-out
- [ ] Base install, SSH via Tailscale reachable, user account + sudo

### Tue Apr 21 — AI server phase 2 + delegation online + Spotify pivot
- [ ] NVIDIA drivers (535 or newer), verify both GPUs with `nvidia-smi`
- [ ] Docker + Docker Compose + NVIDIA Container Toolkit
- [ ] Ollama install, pull models: `qwen2.5-coder:14b-instruct-q5_K_M` (→1080 Ti), `llama3.1:8b-instruct-q5_K_M` (→2060), `nomic-embed-text`
- [ ] Configure per-model GPU pinning (avoid tensor-splitting across Pascal+Turing)
- [ ] Test local model endpoint from cashbox + HA
- [ ] **First Ansible playbook** — codify everything above while fresh
- [ ] Spotify matrix: pivot to ESPHome using existing `/Volumes/config/esphome/Matrix-LED-Now-Playing-Record-Player/` as base

### Wed Apr 22 — HA cleanup + n8n + mirror deploy + final tidy
- [ ] HA: remove light automations from Rental + Primary Bedroom
- [ ] HA: fix Bluetooth
- [ ] HA: fix Solar Panel connectivity
- [ ] HA: fix OpenHASP node
- [ ] HA: voice implementation wired to existing room agents (Quinn/Saffron/Vesper/Axiom/Kai)
- [ ] Frigate: HA integration polish check (NVR at 10.1.30.18)
- [ ] Frigate: install 2x Coral TPUs
- [ ] n8n network monitoring workflow v1 — ping core hosts → InfluxDB → NTFY on failure
- [ ] Magic Mirror: MM² server on cashbox, Chromium kiosk on Pi 4B (+ Pi 3B if only one Pi 4B), Pi Zero 2W skipped
- [ ] Caddyfile syntax fix (see Resources/Caddy Bug Fix)
- [ ] `ai.aadd.rocks` → refresh backend target for AI server at 10.1.30.9
- [ ] Final hardware declutter walkthrough

### Deferred past Thursday (stretch goals)
- Grafana/Loki observability expansion (wait until AI server + n8n are emitting signal)
- k3s cluster unification (local + Oracle) — own weekend
- Magic Mirror server config iteration — better done with Mal around to see it

---

## Active

- [ ] **LLM Wiki / Second Brain** - make Obsidian vault agent-maintained with schema, sync, validation, and MCP/agent workflows
  - [ ] Decide automation bridge: Obsidian native CLI, Local REST API, or both
  - [ ] Establish reliable sync for other devices/homelab agents
  - [ ] Add frontmatter/link validation
  - [ ] Create service-add / incident-log / wiki-ingest workflows
- [ ] **File 2026 Taxes** - due 4/10, use Quicken Desktop output
  - Update rental write-offs: utilities (%), hardware store purchases
- [ ] **Generate Resume** - due ASAP
- [ ] **Build personal static website** - dashboards + network infra views
- [ ] **Fix Matrix LED (rectangular display)** - RPi Zero 2W + HUB75, LED lib dependency errors
- [ ] **Fix Matrix LED (Spotify viewer)** - M4 + HUB75, MicroPython issues
- [ ] **Fix OpenHASP light controller** - config went sideways, room light panel
- [ ] **Setup Claude orchestration** - OpenClaw downstream models + multimodal diff checker
- [ ] **HA: Improve dashboards** - 1 tablet per room + camera hub + info hub
- [ ] **HA: Fix Solar Panel connectivity**
- [ ] **HA: Setup Grafana observability**
- [ ] **HA: Setup Log Scraper AI**
- [ ] **HA: Fix Bluetooth issues**
- [ ] **Do machine learning homework**
- [ ] **Fix Mac Mini secondary SSD security issue**
- [ ] **Migrate AI server to Ubuntu** - wiping Arch/Garuda, GPU issues; consider partitioning /home separately next time
- [ ] **Learn & Setup Ansible or Terraform** - IaC to automate server provisioning after distro wipes; triggered by Ubuntu migration of AI server. Also applies to Pi cluster nodes. Goal: rebuild any machine from scratch in minutes, not hours.
- [ ] **Pi5 k3s Kubernetes Cluster** - 5x Pi5 nodes + Oracle free tier cloud cluster, orchestrated from CachyOS server. Currently running k3s. Next steps: unify local + Oracle nodes, then evaluate integrating with Proxmox 2-node cluster (note: one Proxmox node is the Canty VCM local endpoint — keep isolated or use separate namespace).

## Waiting On

## Someday

- [ ] **HA: Add AI agents by room** - specializations per room
- [ ] **HA: Setup Proxmox rental HA instance** - stable isolated VM
- [ ] **HA: Remove light automation from Rental and Primary Bedroom**
- [ ] **Networking: Optimize SSL and SSH**

## Done
