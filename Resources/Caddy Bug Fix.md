# Caddy Bug Fix — Caddyfile Syntax Errors

> Config location on VPS: `/opt/docker/caddy/Caddyfile` (or wherever deployed)
> Repo: https://github.com/mjbeatty89/vps-config
> Current note: AI server is now at `10.1.30.9`; old examples below preserve the historical broken Caddy block.

## Bug 1 — `ai.aadd.rocks` block never closed ⚠️ CRITICAL

The closing brace `}` is **commented out**, which means everything after
`ai.aadd.rocks` in the file is parsed as part of that block — breaking all
subsequent entries.

**Current (broken):**
```
ai.aadd.rocks {
    reverse_proxy 10.1.30.14:5000
# }
```

**Fix:**
```
# ai.aadd.rocks {
# 	reverse_proxy 10.1.30.14:5000
# }
```
Comment out the whole block until the Tailscale subnet route for VCM is working.

## Bug 2 — `pve-vcm.aadd.rocks` block missing closing brace

The `ha.aadd.rocks` block got swallowed inside `pve-vcm` — missing `}` before it.

**Current (broken):**
```
pve-vcm.aadd.rocks {
	reverse_proxy https://10.1.30.14 {
		transport http {
			tls_insecure_skip_verify
		}
	}
ha.aadd.rocks {    ← INSIDE pve-vcm block, shouldn't be
```

**Fix — add the missing closing brace:**
```
pve-vcm.aadd.rocks {
	reverse_proxy https://10.1.30.14 {
		transport http {
			tls_insecure_skip_verify
		}
	}
}                  ← ADD THIS

ha.aadd.rocks {
```

## Steps to Fix

1. SSH to VPS: `ssh virtual-server-tunnel`
2. Edit Caddyfile
3. Validate: `caddy validate --config /path/to/Caddyfile`
4. Reload: `caddy reload --config /path/to/Caddyfile`
   Or if running in Docker: `docker exec caddy caddy reload --config /etc/caddy/Caddyfile`

## After Fix
- Commit fix to vps-config repo
- Update DNS in Cloudflare to point to 147.224.179.179 (DNS only, no proxy orange cloud)
- Verify affected subdomains: `ha`, `pve-vcm`, `nas`, `pbs`, `un`, `bamboo`, `ag`, `tipi`, etc.

## Related
[[Resources/Network Map]] · [[Areas/Homelab]]
