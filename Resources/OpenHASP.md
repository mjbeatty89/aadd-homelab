# OpenHASP

> LVGL-based touch panel custom component for Home Assistant.
> Displays interactive dashboards on small ESP32 touch screens.
> Custom component lives at `/Volumes/config/custom_components/openhasp/`

## What It Is
OpenHASP (Open Home Automation Switch Panels) lets you design rich LVGL UIs
on ESP32-based touch displays, controlled by and integrated with Home Assistant.
Good for: room light controllers, media controls, status displays.

## Current Use
Matt is experimenting with a **small light controller dashboard** in a room with
bad switch locations. Ran into config issues — "went a little off the rails."

## Status
- [ ] Fix openhasp node functionality (in HA task list)
- [ ] Get light controller dashboard working properly

## Hardware Options
- Most cheap ESP32 touch displays work (CYD, Sunton, Guition, Elecrow)
- Matt has multiple ESPHome display configs that could run HASP

## Useful Links
- Config: `/Volumes/config/esphome/` — several display configs present
- HA component: `/Volumes/config/custom_components/openhasp/`

## Related
[[Areas/Home Assistant]] · [[Resources/Glossary]]
