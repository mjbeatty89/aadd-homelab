# Open Questions

> Questions that need Matt or live-system confirmation before the docs should be treated as authoritative.

## Network / Tailscale
- [x] CANTY VCM / `deb-vcm` should be the subnet router for homelab routes.
- [x] Frigate is at `10.1.30.18`.
- [x] Tailscale identities have been pruned.
- [x] NetBird is deprioritized because the free tier did not provide much value; Tailscale is the default overlay for now.

## Hosts
- [x] AI server LAN IP is `10.1.30.9`; GPUs are GTX 1080 Ti and RTX 2060.
- [ ] What owns Tipi at `10.1.30.178`?
- [x] Windows Server at `10.1.30.19` / `winserv.manee-frog.ts.net` is on standby for Windows-specific features.
- [ ] Establish definitive sources of truth for Proxmox VE, TrueNAS, unRAID, and CANTY VCM.
- [ ] Decide AI server current distro, model storage path, and intended Ansible repo.

## Services
- [ ] Is `proposal.aadd.rocks` backed by the same `cashbox:3002` Obsidian container or a separate share service?
- [ ] Should `ai.aadd.rocks` point directly at `10.1.30.9` / `ai-server.manee-frog.ts.net` after migration?
- [x] Uptime Kuma should track all services, but only alert for down hardware, Home Assistant, and Frigate.
- [ ] Design MCP/agent connections for natural-language updates and service additions.

## Home Assistant / Rental
- [x] Rental Home Assistant VM is planned, not launched yet; it should run on the PVE server.
- [x] Guest-facing migration scope: Den and Suite dashboards/devices, plus items in den, guest bedroom suite, and suite bathroom.
- [ ] Inventory exact Den, guest bedroom suite, and suite bathroom devices to port.
- [ ] Which room tablets / dashboards already exist, and which are still planned?

## Related
[[Home]] · [[Resources/Host Inventory]] · [[Resources/Service Catalog]] · [[Resources/Tailscale Snapshot]]
