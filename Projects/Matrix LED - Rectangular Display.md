# Matrix LED — Rectangular Display

> **Hardware:** Raspberry Pi Zero 2 W + Adafruit HUB75 adapter
> **Goal:** Rotating display for weather / stocks / sports / time

## Status
⚠️ Blocked — LED library dependency errors

## Hardware
- RPi Zero 2 W
- Adafruit HUB75 RGB Matrix Bonnet/Adapter
- HUB75 LED panel (rectangular)

## Software Plan
- Button to switch between visuals:
  - 🌤 Weather
  - 📈 Stocks
  - 🏒 Sports
  - 🕐 Time

## Blocker
LED library dependency errors on RPi Zero 2 W with Adafruit HUB75 adapter.
Likely related to `rpi-rgb-led-matrix` Python bindings or GPIO conflicts.

**Things to try:**
- [ ] Test with `rpi-rgb-led-matrix` library directly (no Python wrapper)
- [ ] Check if RPi Zero 2 W needs `--led-slowdown-gpio` flag
- [ ] Try building from source instead of pip install
- [ ] Check if there's a conflict with onboard Bluetooth/WiFi
- [ ] Consider switching to Pi 3/4 if Zero 2 W limitations are the cause

## Related
[[Projects/Matrix LED - Spotify Viewer]] · [[Areas/Home Assistant]] · [[Areas/Homelab]]
