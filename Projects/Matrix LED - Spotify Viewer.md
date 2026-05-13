# Matrix LED — Spotify Album Viewer

> **Hardware:** Adafruit M4 chip + Adafruit HUB75 driver (square panel)
> **Goal:** Display currently playing Spotify album art on LED matrix

## Status
⚠️ Blocked — MicroPython struggles

## Hardware
- Adafruit M4 Express (or Matrix Portal M4)
- Adafruit HUB75 RGB Matrix driver
- HUB75 LED panel (square)

## Software
- MicroPython on M4
- Spotify integration works (developer credentials set up ✅)
- Pulling album art from Spotify API → display on matrix

## Blocker
MicroPython on M4 struggling — likely memory constraints or library support gaps.

**Things to try:**
- [ ] Try CircuitPython instead of MicroPython (better Adafruit library support)
- [ ] Check `adafruit_matrixportal` library — designed for exactly this hardware
- [ ] Use ESPHome approach instead: see `/Volumes/config/esphome/Matrix-LED-Now-Playing-Record-Player/`
- [ ] HA already has `esphome/Now Playing Spotify Dashboard/` config — could adapt

## Notes
Spotify developer credentials are working fine — the blocking issue is purely the display rendering layer.

ESPHome approach may be simpler since it integrates directly with HA and the Spotify entity is already set up.

## Related
[[Projects/Matrix LED - Rectangular Display]] · [[Areas/Home Assistant]]
