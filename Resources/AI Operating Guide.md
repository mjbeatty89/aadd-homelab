# AI Operating Guide

> Purpose: give any AI model enough context to help inside em0lab without causing avoidable damage.

## Default Behavior
- Treat this vault as the first source of truth, then verify against live systems or Git repos before making infrastructure changes.
- Prefer reading and reporting before changing. When changing, make the smallest reversible change that solves the issue.
- Explain commands and risk plainly. Matt is technical and hands-on, but still learning code and infrastructure conventions.
- Favor GitOps/IaC changes over manual server drift when a repo or playbook exists.
- Record useful findings back into this vault when they would help the next session.

## Hard Safety Rules
- Never hardcode `/Users/mjb`; `$HOME` is `/Volumes/mm2ssd/mjb`.
- Do not move or remove `/Volumes/mm2ssd/opt2/homebrew/`; `/opt/homebrew` points there.
- Do not remove `/Volumes/mm2ssd/mjb2`; old configs may depend on that compatibility symlink.
- Do not move Docker data at `/Volumes/mm2ssd/Docker/`.
- Dotfile edits go under `~/dotfiles/zsh/`, not directly into `~/.zshrc`.
- Do not run broad `find /` on this SSD. Scope searches to known paths and use `rg` / `fd` first.
- Do not print, copy, or commit secrets. Use 1Password and `withai <cmd>` for ephemeral AI API env vars.
- Treat the rental suite as production. Avoid experimental changes to guest-facing automation without an explicit rollback plan.

## Access Patterns
- Tailscale SSH is usually preferred.
- 1Password SSH agent can offer too many keys and fail against small hosts.
- Useful aliases: `ha`, `ubuntu`, `frigate`, `local-vcm`, `virtual-server-tunnel`, `spotify-pi`.
- Public services generally terminate HTTPS on the Oracle VPS Caddy proxy, then route over Tailscale to private hosts.

## Decision Rules
- If a service is public-facing, check Caddy / DNS / Tailscale routing before changing the backend.
- If a service is Docker-managed, find the compose repo before running ad hoc container changes.
- If a task changes Home Assistant behavior, identify whether it affects the main instance, rental instance, or both.
- If a task changes storage, backups, DNS, TLS, SSH, Docker data paths, or Homebrew, pause and document the intended operation first.
- If a task has a real-world guest, safety, or home automation impact, prefer read-only inspection unless Matt explicitly asks for action.

## Good Session Closeout
When finishing infrastructure work, capture:
- What changed.
- Where the source of truth now lives.
- Commands used to validate.
- Any rollback command or restore point.
- Follow-up tasks that should become checkboxes in [[TASKS]].

## Related
[[Home]] · [[Resources/Network Map]] · [[Resources/Runbooks]] · [[Resources/Host Inventory]]

