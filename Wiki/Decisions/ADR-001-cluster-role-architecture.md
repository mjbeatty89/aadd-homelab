---
type: decision
status: draft
owner: matt
created: 2026-05-16
updated: 2026-05-16
tags: [adr, architecture, cluster, storage, media-server, truenas, unraid, oracle, vcm]
confidence: medium
---

# ADR-001: Role-Based Cluster Architecture for em0lab

## Status
Proposed

## Context
em0lab has grown to include multiple servers with meaningfully different strengths: ZFS storage,
community app ecosystems, GPU compute, public-facing networking, and local network management.
Running containers and data co-located on each host independently misses the value of treating
them as a cluster with deliberate role separation. The goal is a frontend/backend split where
app containers on one layer reference databases and file storage on another — mirroring the
pattern used by Kubernetes (stateless pods + PersistentVolumeClaims) but implemented manually
with the existing hardware.

The media server use case crystallized this thinking: the *arr stack + Plex needs community
container flexibility (unRAID) while the actual media library needs ZFS data integrity (TrueNAS).
The same principle extends across all services.

## Decision

Assign each host a primary architectural role and route workloads accordingly.

### Role Map

| Host | Primary Role | Rationale |
|------|-------------|-----------|
| **Oracle VPS** | Public endpoint + external health observer | Only node with an outside-in view of the home network. If everything at home goes down, Oracle is still reachable and can alert. Runs Caddy, Uptime Kuma, and VPS-local public services. |
| **CANTY VCM** | Local network tooling + hypervisor | Tailscale subnet router bridging LAN into the Tailnet. Runs PVE and PBS. 10 PoE ports (verify against hardware — user notes possibly 12) make it the natural hub for local switching and eventually local DNS management. |
| **cashbox** | Observability + MCP gateway (self-contained) | Intentionally isolated from TrueNAS. Observability must not depend on the storage layer — Grafana should still work if TrueNAS has a blip. Runs InfluxDB, Loki, Grafana, Telegraf, MCP gateway, Obsidian LiveSync, and co-located Postgres/Mongo/Redis. |
| **unRAID** | App/compute layer | Community Applications ecosystem covers the full *arr stack and most homelab containers. Containers here are treated as semi-stateless — they reference data on TrueNAS and can be rebuilt without data loss. |
| **TrueNAS** | State/storage backend | ZFS provides checksums, scrubs, and snapshots that protect against silent bitrot on large drives over time. Primary store for media files, NFS shares, iSCSI block volumes, and Time Machine targets. |
| **HA Pi5** | Home automation | Home Assistant. Kept isolated from the storage split — HA state lives locally on the Pi. |
| **AI server** | GPU compute / local LLM inference | GTX 1080 Ti + RTX 2060. Ollama, local model endpoints. May also serve as Plex transcode backend if transcoding is offloaded from the app layer. |
| **Frigate NVR** | Camera AI / NVR | Standalone. Coral TPU target. |

### Media Server Sub-Decision

- **TrueNAS** holds the media library on a dedicated ZFS dataset.
- **unRAID** runs the app stack: Sonarr, Radarr, Prowlarr, Bazarr, Recyclarr, qBittorrent/SABnzbd,
  Overseerr, Tautulli, and Plex/Jellyfin.
- **Bridge**: TrueNAS exports media via NFS; unRAID mounts it as a local path visible to all containers.
- **Transcoding**: Evaluate whether Plex transcoding should offload to the AI server's GPUs rather
  than running on unRAID's CPU.

### Storage Protocol Guide

| Use Case | Protocol | Notes |
|----------|----------|-------|
| Media files | NFS | Shared read/write, good enough for sequential media |
| Databases needing block storage | iSCSI | Block-level access, proper locking |
| macOS Time Machine | SMB (AFP-style) | Already configured on TrueNAS |
| Nextcloud / Paperless data | NFS or SMB | Hosted on unRAID, data can optionally back to TrueNAS |

## Consequences

**Positive**
- unRAID containers become more reproducible — state lives on TrueNAS, app layer can be wiped and rebuilt.
- TrueNAS failure degrades apps but doesn't lose data; recovery is re-pointing, not restoring.
- Oracle's external position gives genuine outside-in health monitoring independent of home network state.
- VCM's PoE ports become a purposeful local switching layer rather than incidental connectivity.
- cashbox observability stays independent of the storage split — survives a TrueNAS outage.

**Negative / Risks**
- NFS introduces a network dependency for all media and app data; a TrueNAS blip pauses unRAID apps.
- iSCSI volume management on TrueNAS adds operational complexity (zvols, initiator config).
- Two-host media setup (TrueNAS + unRAID) means two systems to maintain instead of one.
- unRAID's storage/parity model is weaker than ZFS — auxiliary data on unRAID has less integrity protection.

## Alternatives Considered

- **Everything on unRAID**: Simpler to operate, but sacrifices ZFS data integrity for the media vault.
- **Everything on TrueNAS**: Better storage guarantees everywhere, but TrueCharts container ecosystem
  is more limited and higher friction than unRAID Community Applications.
- **cashbox as app layer**: cashbox has the compute (7600X) but is already loaded with observability
  and MCP duties; mixing roles risks observability going down with app problems.

## Follow-Up

- [ ] Decide final PoE port allocation on VCM (10 or 12 ports — confirm hardware spec)
- [ ] Plan VCM as local DNS primary (AdGuard currently at 10.1.13.16 — migrate or co-manage?)
- [ ] Create NFS export plan on TrueNAS (media dataset path, permissions, client IPs)
- [ ] Decide Plex transcode target: unRAID CPU vs AI server GPU (NVENC on 2060)
- [ ] Evaluate whether Nextcloud/Paperless data on unRAID should snapshot to TrueNAS
- [ ] Define which unRAID containers (if any) get iSCSI-backed volumes vs NFS
- [ ] Create ADR-002 for media server stack specifics (*arr versions, indexer config, naming convention)

## Related
- [[Resources/Host Inventory]]
- [[Resources/Service Catalog]]
- [[Resources/Network Map]]
- [[Resources/Open Questions]]
- [[Areas/Homelab]]
