# Tailscale Snapshot

> Last checked live: 2026-05-02 from `mmm4` with `tailscale status --json`.
> Matt update on 2026-05-11: Tailscale identities were pruned; this note should be refreshed from live Tailscale before using offline peers operationally.

## Tailnet
- Tailnet: `mjbeatty89.github`
- MagicDNS suffix: `manee-frog.ts.net`
- Current workstation: `4m4.manee-frog.ts.net`
- Current workstation Tailscale IP: `100.115.54.11`

## Online Peers

| Hostname | MagicDNS | Tailscale IP | Tags / Routes | Notes |
|----------|----------|--------------|---------------|-------|
| `cash-containers` | `cash.manee-frog.ts.net` | `100.68.19.83` | `tag:client`, `tag:exit`, `tag:homelab`, `tag:server` | cashbox / container host. |
| `unraidserv` | `un.manee-frog.ts.net` | `100.76.50.59` | `tag:exit`, `tag:homelab`, `tag:server` | unRAID. |
| `truenas-scale` | `nas.manee-frog.ts.net` | `100.99.131.90` | `tag:exit`, `tag:homelab`, `tag:server` | TrueNAS. |
| `deb-vcm` | `vcm.manee-frog.ts.net` | `100.83.134.110` | `tag:exit`, `tag:gateway`, `tag:homelab`, `tag:server` | CANTY VCM; should be the subnet router. |
| `frig` | `frig.manee-frog.ts.net` | `100.79.30.100` | `tag:exit`, `tag:homelab`, `tag:server` | Frigate NVR at LAN `10.1.30.18`. |
| `homeassistant` | `ha.manee-frog.ts.net` | `100.79.62.42` | `tag:exit`, `tag:homelab`, `tag:server`; route was `10.1.30.0/23` on 2026-05-02 | HA should not be the intended subnet router long term. |
| `HAPIOS` | `hapios.manee-frog.ts.net` | `100.118.97.73` | `tag:client`, `tag:homelab`, `tag:server` | Likely HA OS-related; confirm role. |
| `cloud-proxy` | `oracle.manee-frog.ts.net` | `100.67.166.50` | `tag:exit`, `tag:remote`, `tag:server` | Oracle VPS / public proxy. |
| `ai-server` | `ai-server.manee-frog.ts.net` | `100.75.111.86` | `tag:client`, `tag:exit`, `tag:homelab`, `tag:server` | AI server has live Tailscale identity. |

## Offline / Historical Peers

| Hostname | MagicDNS | Tailscale IP | Notes |
|----------|----------|--------------|-------|
| `debian-docker-desktop` | `debian-docker-desktop.manee-frog.ts.net` | `100.96.210.38` | Offline Docker Desktop peer. |
| `LapMacPro` | `lapmacpro.manee-frog.ts.net` | `100.93.201.57` | Offline MacBook Pro. |
| `mjbmacmini` | `mjbmacmini.manee-frog.ts.net` | `100.95.106.89` | Older/offline Mac Mini identity. |
| `mmm4-docker-desktop` | `mmm4-docker-desktop.manee-frog.ts.net` | `100.81.61.121` | Offline Docker Desktop peer. |
| `winserv` | `winserv.manee-frog.ts.net` | `100.112.241.11` | Offline Windows server. |

## Follow-Up Questions
See [[Resources/Open Questions]].

## Related
[[Resources/Network Map]] · [[Resources/Host Inventory]] · [[Resources/Open Questions]] · [[Resources/AI Operating Guide]]
