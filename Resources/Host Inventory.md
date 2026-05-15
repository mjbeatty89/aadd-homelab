# Host Inventory

> Source of truth for machines in em0lab. Update this when hosts move, roles change, or new aliases are added.

## Public Edge

| Host | Addresses | Role | Source of Truth | Notes |
|------|-----------|------|-----------------|-------|
| Oracle VPS / `virtual-tunnel-vnic` / `cloud-proxy` | Public `147.224.179.179`; Tailscale `100.67.166.50`; MagicDNS `oracle.manee-frog.ts.net` | Public reverse proxy, VPS-local Docker services, Tailscale bridge into home | `/home/mjb/projects/vps-config`; GitHub `mjbeatty89/vps-config` | Runs Caddy and public `*.aadd.rocks` service entrypoints. |

## Core Home Servers

| Host | Addresses | Role | Source of Truth | Notes |
|------|-----------|------|-----------------|-------|
| `cashbox` / `cash-containers` | Tailscale `100.68.19.83`; LAN `10.1.30.8` (`enp14s0`, management); LAN `10.1.30.84` (`enp15s0`, container NIC — macvlan planned); MagicDNS `cash.manee-frog.ts.net` | CachyOS container server, observability/data services, Obsidian LiveSync, MCP gateway | `/home/mjb/projects/cash-compose`; GitHub `mjbeatty89/cash-compose` | Ryzen 5 7600X, 32GB RAM, 500GB NVMe. Dual RTL8125 2.5GbE NICs. `enp15s0` reserved for Docker macvlan — containers get direct LAN IPs, no NAT. DHCP reservation needed for `10.1.30.84` before macvlan setup. |
| CANTY VCM / `local-vcm` / `deb-vcm` | LAN `10.1.30.14`; Tailscale `100.83.134.110`; MagicDNS `vcm.manee-frog.ts.net` | Intended Tailscale subnet router, Proxmox Backup Server, 10-port PoE mini-PC | Source of truth to establish | Tagged as Tailscale gateway; also exposes `pbs.aadd.rocks` and `pve-vcm.aadd.rocks`. |
| Proxmox VE | LAN `10.1.30.27` | VM host | Source of truth to establish | Planned host for rental Home Assistant VM. |
| TrueNAS / `truenas-scale` | LAN `10.1.31.70`; Tailscale `100.99.131.90`; MagicDNS `nas.manee-frog.ts.net` | NAS and Time Machine target | TBD | SMB Time Machine share on ZFS pool. |
| unRAID / `unraidserv` | LAN `10.1.30.16`; Tailscale `100.76.50.59`; MagicDNS `un.manee-frog.ts.net` | Storage and apps | TBD | Mentioned services include Nextcloud, AgentGPT, and Bambu-related tooling. |
| AI server | LAN `10.1.30.9`; Tailscale `100.75.111.86`; MagicDNS `ai-server.manee-frog.ts.net` | Local model server / GPU rig | Future Ansible repo | GPUs: GTX 1080 Ti and RTX 2060. Target stack includes NVIDIA drivers, Docker, Ollama, LM Studio-compatible APIs. |

## Smart Home / Edge Devices

| Host | Address | Role | SSH Alias | Notes |
|------|---------|------|-----------|-------|
| HA Pi5 / `homeassistant` | LAN `10.1.30.10`; Tailscale `100.79.62.42`; MagicDNS `ha.manee-frog.ts.net` | Main Home Assistant | `ha` | Experimental main HA instance. CANTY VCM should be subnet router instead of HA. |
| HAPIOS | Tailscale `100.118.97.73`; LAN TBD | Home Assistant OS-related host | TBD | Role needs confirmation. |
| Frigate NVR / `frig` | LAN `10.1.30.18`; Tailscale `100.79.30.100`; MagicDNS `frig.manee-frog.ts.net` | Camera AI / NVR | `frigate` | Coral TPU installation is planned. |
| Ubuntu server | `10.1.11.129` | General Linux server | `ubuntu` | Role needs refresh. |
| AdGuard DNS | `10.1.13.16` | DNS filtering | TBD | Network DNS service. |
| Spotify Pi / Matrix | `10.1.10.55` | Matrix LED project | `spotify-pi` | Raspberry Pi project host. |
| Windows Server / `winserv` | LAN `10.1.30.19`; MagicDNS `winserv.manee-frog.ts.net` | Standby Windows host | Source of truth to establish | Limited role until a Windows-specific feature is necessary. |

## Local Workstation

| Host | Path / Address | Role | Notes |
|------|----------------|------|-------|
| `mmm4` Mac Mini / `Matts mm-m4` | `$HOME=/Volumes/mm2ssd/mjb`; Tailscale `100.115.54.11`; MagicDNS `4m4.manee-frog.ts.net` | Primary local workstation for Codex/Cowork, Obsidian, development | `/Users/mjb` is a SIP-protected ghost directory; do not use it. Code lives in `/Volumes/mm2ssd/mjb/dev/`; `/Volumes/mm2ssd/dev` is a symlink. |

## Unknowns To Fill
See [[Resources/Open Questions]].

## Related
[[Resources/Network Map]] · [[Resources/Service Catalog]] · [[Resources/Tailscale Snapshot]] · [[Resources/Open Questions]] · [[Areas/Homelab]]
