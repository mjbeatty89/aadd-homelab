# Ohana Suite — Rental

> DBA: **Ann Arbor Discreet Destinations (AADD)** · Domain: aadd.rocks
> Attached guest house on the property. Managed as short-term rental.

## HA Setup
- Stable, isolated HA instance is planned, not launched yet.
- Target host: Proxmox VE / PVE server.
- Agent: **Kai** (Gracious independent host)
- Scope to port: Den and Suite dashboards/devices, plus items in the den, guest bedroom suite, and suite bathroom.
- Separate Zigbee coordinator should insulate rental devices from main HA changes.
- Dashboard: `dashboards/rental_suite.yaml` when created / ported.

## Open Tasks
- [ ] Finish flooring transitions
- [ ] Finish over-toilet organizer
- [ ] Fix tub jets
- [ ] Remove light automation from rental (main HA task)
- [ ] Launch rental HA VM on PVE server
- [ ] Inventory Den, guest bedroom suite, and suite bathroom devices
- [ ] Port Den and Suite dashboards/devices into rental HA

## Notes
- Guests get stable, reliable smart home experience
- Main instance can break freely without affecting rental
- Kai agent handles guest interaction and suite-specific controls

## Related
[[Home]] · [[Areas/Home Assistant]]
