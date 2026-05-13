# Runbooks

> Repeatable procedures for common em0lab work. Prefer expanding these over relying on memory.

## Check Public Service Routing

Use when a `*.aadd.rocks` service is down or pointing at the wrong backend.

1. Identify whether the service is VPS-local or home-routed in [[Resources/Service Catalog]].
2. Check DNS / Cloudflare target for the subdomain.
3. SSH to VPS: `ssh virtual-server-tunnel`.
4. Inspect the Caddyfile from the GitOps repo first, then the deployed Caddyfile.
5. Validate Caddy before reload: `caddy validate --config /path/to/Caddyfile`.
6. Reload Caddy only after validation passes.
7. If the backend is home-routed, verify Tailscale connectivity from the VPS to the backend IP/port.
8. Commit the fix to `mjbeatty89/vps-config` if the deployed change is real.

Related: [[Resources/Caddy Bug Fix]]

## Add A New Homelab Service

1. Decide where it belongs: VPS-local, cashbox, Home Assistant, Kubernetes, Proxmox VM, or another host.
2. Prefer the matching GitOps repo or IaC playbook over manual setup.
3. Use Tailscale IPs or MagicDNS for coded connections unless there is a specific reason to use LAN-only addressing.
4. Assign a stable DNS name if it needs user access.
5. Put secrets in 1Password or the repo's intended secret mechanism, not in notes.
6. Add the service to [[Resources/Service Catalog]].
7. Add or update a system note from [[Templates/Homelab System Note]] if the service has operational details.
8. Add monitoring in Uptime Kuma for all services; enable alerts only for hardware, Home Assistant, Frigate, or services Matt explicitly promotes.

## Agent / MCP Service Changes

Use this when an MCP server or coding agent is asked to add or update homelab services through natural language.

1. Identify the source-of-truth repo or playbook for the target host.
2. If no source of truth exists yet, create a plan to establish one before making durable service changes.
3. Prefer GitOps/IaC updates over manual changes on the host.
4. Use Tailscale IPs or MagicDNS for service-to-service connections.
5. Document the service in [[Resources/Service Catalog]] and the host in [[Resources/Host Inventory]].
6. Add a system note from [[Templates/Homelab System Note]] when the service has meaningful operations, logs, backups, or secrets.

## Rebuild / Migrate AI Server

1. Back up anything worth keeping from the current install.
2. Install Ubuntu Server 24.04 LTS unless Matt chooses another distro.
3. Use separate partitions for `/` and `/home`; consider Docker data layout before heavy model downloads.
4. Install NVIDIA drivers and verify GPUs with `nvidia-smi`.
5. Install Docker, Docker Compose, and NVIDIA Container Toolkit.
6. Install Ollama or the chosen LM Studio-compatible model server.
7. Pull baseline models and document model placement / GPU pinning.
8. Write the Ansible playbook while the manual steps are fresh.
9. Update [[Resources/Host Inventory]], [[Resources/Service Catalog]], and [[Projects/Claude Orchestration]].

## Home Assistant Change Safety

1. Identify main vs rental instance.
2. For rental-impacting changes, prefer a backup/snapshot and explicit rollback.
3. Check whether the feature touches automations, Zigbee, dashboards, room agents, ESPHome, or voice.
4. For ESPHome, note the device name, source YAML, and physical location.
5. Test in the main instance before carrying stable behavior into the rental instance.
6. Document the result in [[Areas/Home Assistant]] or the relevant project note.

## Obsidian LiveSync Troubleshooting

1. From local Mac, prefer CouchDB URI `http://100.68.19.83:5984`.
2. From the Obsidian container, use `http://obsidian-couchdb:5984`.
3. Check cashbox compose state before changing plugin settings.
4. Credentials are on cashbox in `/home/mjb/projects/cash-compose/.credentials.txt`; do not copy them into notes.

## Related
[[Resources/AI Operating Guide]] · [[Resources/Service Catalog]] · [[Resources/Host Inventory]]
