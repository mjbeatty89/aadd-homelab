# Service Catalog

> Public and private services in em0lab. Keep this boring and accurate: URL, backend, owner, source of truth.

## Public `*.aadd.rocks` Services

| Public URL | Backend | Location | Source of Truth | Notes |
|------------|---------|----------|-----------------|-------|
| `dash.aadd.rocks` | Heimdall `:8080` | Oracle VPS | `vps-config` | Dashboard. |
| `n8n.aadd.rocks` | n8n `:5678` | Oracle VPS | `vps-config` | Automation workflows. |
| `status.aadd.rocks` | Uptime Kuma `:3001` | Oracle VPS | `vps-config` | Status monitoring. |
| `portainer.aadd.rocks` | Portainer `:9000` | Oracle VPS | `vps-config` | Docker UI. |
| `vault.aadd.rocks` | Vaultwarden `:8222` | Oracle VPS | `vps-config` | Secrets/password UI; do not expose credentials in notes. |
| `ntfy.aadd.rocks` | NTFY `:8095` | Oracle VPS | `vps-config` | Notifications. |
| `git.aadd.rocks` | Gitea `:3000` | Oracle VPS | `vps-config` | Self-hosted Git. |
| `pdf.aadd.rocks` | Stirling PDF `:8083` | Oracle VPS | `vps-config` | PDF utilities. |
| `notes.aadd.rocks` | Memos `:5230` | Oracle VPS | `vps-config` | Notes/memos. |
| `ha.aadd.rocks` | `10.1.30.10:8123` | Home via Tailscale | VPS Caddy + HA config | Main Home Assistant. |
| `un.aadd.rocks` | `10.1.30.16` | Home via Tailscale | VPS Caddy | unRAID. |
| `pve.aadd.rocks` | `10.1.30.27:8006` | Home via Tailscale | VPS Caddy | Proxmox VE. |
| `pbs.aadd.rocks` | `10.1.30.14:8007` | Home via Tailscale | VPS Caddy | Proxmox Backup Server. |
| `nas.aadd.rocks` | `10.1.31.70` | Home via Tailscale | VPS Caddy | TrueNAS. |
| `pve-vcm.aadd.rocks` | `10.1.30.14` | Home via Tailscale | VPS Caddy | CANTY VCM Proxmox endpoint. |
| `ai.aadd.rocks` | Target TBD, likely AI server `10.1.30.9` | Home via Tailscale | VPS Caddy | Should be revisited now that AI server is at `10.1.30.9`; old target was `10.1.30.14:5000`. |
| `obsidian.aadd.rocks` | `cashbox:3002` | cashbox | `cash-compose` + VPS Caddy | KasmVNC Obsidian container, basic auth user `mjb`. |
| `proposal.aadd.rocks` | `cashbox:3002` or related shareable view | cashbox | `cash-compose` + VPS Caddy | Shareable proposal access, basic auth user `share`. |

## cashbox Internal Services

| Service | Port | Role | Notes |
|---------|------|------|-------|
| Obsidian container | `3002` | Browser-accessible Obsidian / KasmVNC | Public via `obsidian.aadd.rocks`. |
| CouchDB LiveSync | `5984` | Obsidian LiveSync database | From Mac use `http://100.68.19.83:5984`; from container use `http://obsidian-couchdb:5984`. |
| rxResume | `3500` | Resume builder | Tied to resume/website project. |
| Grafana | `3001` | Dashboards | Needs HA + Pi data source expansion. |
| InfluxDB | `8086` | Metrics | Receives Telegraf host metrics. |
| Loki | `3100` | Logs | Observability stack. |
| Redis | `6379` | Data service | Used by apps/workflows as needed. |
| Postgres | `5432` | Database | Shared app database. |
| MongoDB | `27017` | Database | Shared app database. |
| Docker MCP gateway | `8811` | SSE MCP gateway | Connected as `cashbox-docker`; exposes many Docker MCP servers. |

## Service Ownership Rules
- VPS-local public apps are usually changed in `vps-config`.
- cashbox-hosted apps are usually changed in `cash-compose`.
- Home Assistant behavior should be changed in the HA config repo / `/Volumes/config`, with rental isolation in mind.
- New services should get a row here and a short system note using [[Templates/Homelab System Note]].
- Coded service connections should use Tailscale addresses or MagicDNS by default.
- Goal: establish source-of-truth repos/playbooks for Proxmox VE, TrueNAS, unRAID, and CANTY VCM so MCP/agents can safely make natural-language updates and service additions through GitOps/IaC.

## Monitoring Policy
- Uptime Kuma should track all services.
- Alerts should fire only for down hardware, Home Assistant, and Frigate unless Matt explicitly promotes another service to alert-worthy.

## Related
[[Resources/Host Inventory]] · [[Resources/Network Map]] · [[Resources/Runbooks]]
