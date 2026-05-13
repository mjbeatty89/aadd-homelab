# Mac Mini M4 — External SSD Migration
**Status:** ✅ Complete
**Date:** 2026-04
**Related:** [[Areas/Homelab]]

---

## What This Was

The M4 Mac Mini shipped with a 250GB internal SSD, which filled quickly. A 1TB external SSD in a dock was added but never properly integrated — resulting in a messy split filesystem with ad-hoc symlinks, broken paths, GUI permission popups, and an unstable shell environment.

This project cleaned up the entire setup over a single session.

---

## What Was Done

### Home Directory Migration
- Moved `$HOME` from `/Users/mjb` (internal) to `/Volumes/mm2ssd/mjb` (external SSD) via System Settings → Users & Groups → Advanced Options
- Manually fixed configs and symlinks to survive the move

### Shell / PATH Fixes
- Fixed **6 hardcoded `/Users/mjb` paths** in `.zshrc` that tools (LM Studio, Docker, Antigravity, opencode, pnpm, broot) had auto-appended
- Fixed a **pnpm syntax bug** — missing closing quote on `PNPM_HOME` was silently swallowing the entire PATH block
- Fixed **`/etc/paths`** — removed `/Users/mjb` (home dir was in PATH), fixed a corrupted `115;9u/usr/local/bin` escape code, updated stale `mjb2` entry
- Added `typeset -U path` to deduplicate PATH entries permanently
- Removed duplicate zsh plugin loading (autosuggestions + syntax-highlighting were sourced twice)
- Removed duplicate `starship init` call

### Symlink Cleanup
- All symlinks in old `/Users/mjb` were broken (pointed to `/Volumes/mm2ssd/mjb2/` which didn't exist)
- Fixed by creating `/Volumes/mm2ssd/mjb2 → mjb` compatibility symlink — resolved all broken links instantly
- `/Users/mjb` itself cannot be converted to a symlink or deleted — macOS SIP protects `/Users/`. Left as ghost directory; `mjb2` bridge handles any old references.

### Filesystem Cleanup
- Migrated unique content from SSD-root `Documents/` into `~/Documents/`
- Removed stale `Documents alias` and `Documents.symlink` from home
- `Library2/` at SSD root: moved unique dirs (`Developer`, `com.apple.wallpaper`) into `~/Library/`, symlinked `Library2/Logs → ~/Library/Logs`
- Removed 1.9GB PyCharm crash dump (`java_error_in_pycharm.hprof`)
- Moved misplaced `node_modules/`, `package.json`, `package-lock.json`, `ecosystem.config.js` from `~/` to `~/Projects/Misc/tools-scratch/`
- Removed empty `homesyc/` typo directory
- Archived old `opt2/homebrew.archived` (initially misidentified as stale — see Homebrew note below)

### Homebrew (near-miss)
- `/opt/homebrew` is a **symlink** → `/Volumes/mm2ssd/opt2/homebrew/` — Homebrew lives on the SSD
- Accidentally archived `opt2/homebrew` thinking it was a duplicate; restored immediately
- `.zprofile` calls `eval "$(/opt/homebrew/bin/brew shellenv)"` which broke while the symlink was dead
- Lesson: always check for symlinks before archiving directories at `/Volumes/mm2ssd/opt2/`

### Time Machine
- Configured Time Machine backup to **TrueNAS** over SMB (ZFS pool)
- TrueNAS chosen over Unraid for this: native Time Machine SMB toggle, ZFS data integrity ideal for backups
- Setup: create dataset → SMB share → enable Time Machine toggle → macOS discovers automatically

### Documentation
- Created `/Volumes/mm2ssd/dev/CLAUDE.md` — full agent/orchestration context file for the dev environment
- Created `$HOME/CLAUDE.md` — home-level context for AI sessions

---

## Current State

| Item | Status |
|------|--------|
| `$HOME` | `/Volumes/mm2ssd/mjb` ✅ |
| PATH | Clean, no ghost entries ✅ |
| Shell startup | No errors ✅ |
| Symlinks in old home | Resolved via `mjb2` bridge ✅ |
| Time Machine | Running to TrueNAS ✅ |
| Homebrew | `/opt/homebrew` → SSD ✅ |
| CLAUDE.md context files | In place ✅ |

### Still Rough
- `dotfiles2/` in `$HOME` is a stale snapshot from migration — can be deleted once confident nothing is missing. Contains a **1Password export** (`1PasswordExport-...20260312.1pux`) that should be deleted after confirming import.
- `~/Downloads` is a symlink to `/Volumes/mm2ssd/Downloads/` (SSD root) rather than a proper directory inside `mjb/` — works fine, just non-standard
- `Library2/` at SSD root still exists with root-owned subdirs (`PrivilegedHelperTools`, `Receipts`) that couldn't be removed without sudo fighting

---

## Key Paths Reference

```
$HOME                    /Volumes/mm2ssd/mjb/
Code / projects          /Volumes/mm2ssd/dev/
Homebrew                 /opt/homebrew → /Volumes/mm2ssd/opt2/homebrew/
Docker data              /Volumes/mm2ssd/Docker/   (68GB, don't move w/o reconfiguring Desktop)
Active dotfiles          ~/dotfiles/zsh/.zshrc  (~/. zshrc symlinks here)
Machine config           ~/dotfiles/zsh/machines/mmm4.zsh
Old home (ghost)         /Users/mjb/   (SIP-protected, leave it)
Compat symlink           /Volumes/mm2ssd/mjb2 → mjb
```
