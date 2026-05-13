# Home Assistant

> Config lives at `/Volumes/config` · Instance: [ha.aadd.rocks](https://ha.aadd.rocks)
> Git-synced to `main-clean` branch. Auto-commits on change.

## Architecture
**Dual-instance plan:**
- **Main** (experimental) — multi-agent, can break freely
- **Rental** (planned stable VM on PVE) — isolated Zigbee coordinator and guest-facing Den / Suite scope

## Room Agents
| Room | Agent | Personality |
|------|-------|-------------|
| Living Room | Quinn | Warm social host |
| Kitchen | Saffron | Practical culinary expert |
| Primary Bedroom | Vesper | Guardian of rest |
| Office | Axiom | Focused productivity engine |
| Ohana Suite | Kai | Gracious independent host |

## Open Tasks
- [ ] Improve dashboards — 1 tablet per room + camera hub + info hub
- [ ] Fix Solar Panel connectivity
- [ ] Add AI agents by room with specializations
- [ ] Remove light automation from Rental and Primary Bedroom
- [ ] Launch Proxmox/PVE instance for rental
- [ ] Fix Bluetooth issues
- [ ] Setup Log Scraper AI
- [ ] Setup Grafana observability
- [ ] Fix [[OpenHASP]] node functionality
- [ ] Setup Rental [[Areas/Rental Suite]] instance

## Key Custom Components
`openhasp` · `extended_openai_conversation` · `view_assist` · `magic_areas`
`bermuda` (BLE presence) · `llmvision` · `icloud3` · `frigate` · `spotcast`
`home_generative_agent` · `area_occupancy` · `pyscript` · `nodered`

## ESPHome Devices
See `/Volumes/config/esphome/` for all configs.
- [[Projects/Matrix LED - Rectangular Display]]
- [[Projects/Matrix LED - Spotify Viewer]]
- Spotify Controller (Living Room CYD display)
- HASPone light controllers → [[OpenHASP]]
- Multiple Bluetooth proxies
- Apollo MTR-1 presence sensor

## Rental Migration Scope
- Den and Suite dashboards/devices.
- Items in den, guest bedroom suite, and suite bathroom.
- See [[Areas/Rental Suite]].

## Related
[[Home]] · [[Areas/Homelab]] · [[Areas/Rental Suite]] · [[OpenHASP]]
