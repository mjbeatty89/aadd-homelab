# em0lab Network Map

> Public edge: Oracle VPS. Private side: home network over Tailscale. Service inventory lives in [[Resources/Service Catalog]].

## Architecture Overview

```
Internet
    │
    ▼
Oracle Cloud VPS (virtual-tunnel-vnic)
  IP: 147.224.179.179
  Tailscale: 100.67.166.50
  Services: Caddy (HTTPS), n8n, Heimdall, Uptime Kuma,
            Portainer, Vaultwarden, Gitea, NTFY, Memos,
            1Password Connect, Stirling PDF
    │
    │ Tailscale tunnel (subnet routing)
    ▼
CANTY VCM (local-vcm) — 10.1.30.14
  Role: Local-side Tailscale bridge, Proxmox Backup Server
  10 PoE ports (underutilized)
  PBS: pbs.aadd.rocks → :8007
  PVE: pve-vcm.aadd.rocks
    │
    ▼
Local Network (UniFi)
```

## VLANs
| VLAN | Subnet | Purpose |
|------|--------|---------|
| 10 | 10.1.10.x | Pi / IoT |
| 11 | 10.1.11.x | Servers (Ubuntu) |
| 13 | 10.1.13.x | DNS (AdGuard: 10.1.13.16) |
| 20 | 10.1.20.x | TBD |
| 30 | 10.1.30.x | Main homelab |
| 31 | 10.1.31.x | NAS / storage |
| 40 | 10.1.40.x | TBD |
| 50 | 10.1.50.x | TBD |

## Homelab Hosts
| Host | IP | Role | SSH alias |
|------|----|------|-----------|
| cashbox | 10.1.30.8 (`enp14s0`, mgmt) · 10.1.30.84 (`enp15s0`, containers) | Container server, MCP gateway, observability | — |
| HA Pi5 | 10.1.30.10 | Home Assistant | `ha` |
| CANTY VCM | 10.1.30.14 | Proxmox Backup + Tailscale bridge | `local-vcm` |
| unRAID | 10.1.30.16 | Storage, Nextcloud, AgentGPT, Bambu | `winserv` area |
| Windows Server | 10.1.30.19 | Windows | `winserv` |
| Proxmox VE | 10.1.30.27 | VMs | — |
| Tipi | 10.1.30.178 | App platform | — |
| Frigate NVR | 10.1.30.18 | Camera AI | `frigate` |
| Ubuntu server | 10.1.11.129 | General Linux | `ubuntu` |
| TrueNAS | 10.1.31.70 | Media NAS | — |
| AdGuard | 10.1.13.16 | DNS filtering | — |
| Spotify Pi / Matrix | 10.1.10.55 | RPi project | `spotify-pi` |

## *.aadd.rocks Services (via Caddy on VPS → Tailscale → home)
| Subdomain | Backend | Notes |
|-----------|---------|-------|
| dash | Heimdall :8080 | VPS-local |
| n8n | n8n :5678 | VPS-local |
| status | Uptime Kuma :3001 | VPS-local |
| portainer | Portainer :9000 | VPS-local |
| vault | Vaultwarden :8222 | VPS-local |
| ntfy | NTFY :8095 | VPS-local |
| git | Gitea :3000 | VPS-local |
| pdf | Stirling PDF :8083 | VPS-local |
| notes | Memos :5230 | VPS-local |
| ha | 10.1.30.10:8123 | Via Tailscale |
| un | 10.1.30.16 | Via Tailscale |
| pve | 10.1.30.27:8006 | Via Tailscale |
| pbs | 10.1.30.14:8007 | Via Tailscale |
| nas | 10.1.31.70 | Via Tailscale |
| pve-vcm | 10.1.30.14 | Via Tailscale |
| ai | target TBD, likely 10.1.30.9 | Needs Caddy/backend refresh |

## Tailscale
- Network name: **manee-frog**
- VPS Tailscale IP: 100.67.166.50
- Backup access: `*.manee-frog.ts.net`
- VPS advertises as exit node + accepts subnet routes
- Intended home subnet router: CANTY VCM / `deb-vcm` / `vcm.manee-frog.ts.net`

## Source Of Truth
| Layer | Source |
|-------|--------|
| VPS Caddy / public services | `/home/mjb/projects/vps-config` · GitHub `mjbeatty89/vps-config` |
| cashbox Docker services | `/home/mjb/projects/cash-compose` · GitHub `mjbeatty89/cash-compose` |
| Home Assistant config | `/Volumes/config` · `main-clean` branch |
| Host and service docs | [[Resources/Host Inventory]] · [[Resources/Service Catalog]] |

## Known Issues / TODO
- [ ] **cashbox macvlan Docker network** — configure Docker macvlan on `enp15s0` (`10.1.30.84`); get DHCP reservation for that IP first; note host↔container comms require a macvlan shim interface on host side
- [ ] **Caddyfile has syntax errors** — see [[Resources/Caddy Bug Fix]]
- [ ] `ai.aadd.rocks` target needs refresh for AI server at `10.1.30.9`
- [ ] Services not yet configured: nextcloud, photoprism, adguard, lldap, komodo, syncth, diyhue
- [ ] 5-node Pi5 k3s cluster — in progress
- [ ] Pi SSH hygiene — 1Password floods hosts with too many keys

## Related
[[Home]] · [[Areas/Homelab]] · [[Resources/Host Inventory]] · [[Resources/Service Catalog]] · [[Resources/Caddy Bug Fix]]
