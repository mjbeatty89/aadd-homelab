# em0lab — Homelab

> Homelab name: **em0lab** · Domain: `aadd.rocks` · Overlay network: Tailscale `manee-frog`

## Start Here
- [[Resources/AI Operating Guide]] — safety and working rules for AI assistants.
- [[Resources/Network Map]] — topology, VLANs, and public service routing.
- [[Resources/Host Inventory]] — machines, roles, addresses, and source of truth.
- [[Resources/Service Catalog]] — public/private services and ownership.
- [[Resources/Runbooks]] — repeatable operational procedures.

## Infrastructure
- Oracle VPS as public reverse proxy and VPS-local Docker host.
- `cashbox` as core home container server and observability/data hub.
- CANTY VCM as local Tailscale bridge, Proxmox Backup Server, and PoE mini-PC.
- Proxmox VE for VMs; rental Home Assistant instance should live here and remain stable.
- TrueNAS and unRAID for storage.
- Multiple Raspberry Pis for Home Assistant, matrix display, kiosk, and future k3s work.
- AI server / GPU rig being migrated from Garuda/Arch-family Linux to Ubuntu + Ansible.
- Mac Mini `mmm4` as local workstation with `$HOME` on external SSD.

## Networking
- UniFi network stack with VLANs documented in [[Resources/Network Map]].
- Tailscale is the current overlay and backup access path; coded service connections should use Tailscale by default.
- Zigbee2MQTT and ESPHome support smart home devices.
- NetBird is deprioritized because the free tier did not provide much value; revisit only if Tailscale leaves a clear gap.

## Open Tasks
- [ ] Complete server services
- [ ] Setup local and remote Kubernetes clusters
- [ ] Optimize SSL and SSH
- [x] Fix Mac Mini secondary SSD security issue (2026-04 — see Projects/Mac Mini M4 - External SSD Migration)
- [ ] Finish AI server source-of-truth setup and model/service documentation

## AI Infrastructure
- Local model server at `10.1.30.9` / `ai-server.manee-frog.ts.net` with GTX 1080 Ti and RTX 2060.
- Target APIs: Ollama / LM Studio compatible.
- HA uses `extended_openai_conversation` and `ollama_vision`
- [[Projects/Claude Orchestration]] for multi-model agent work
- OpenClaw for untethered local model sandboxing

## Services Running
See [[Resources/Service Catalog]].

## Related
[[Home]] · [[Areas/Home Assistant]] · [[Projects/Claude Orchestration]] · [[Resources/Host Inventory]]
