# Nassim's agent configuration

Portable global instructions and personal skills shared by Codex and Claude.

## Install on a new machine

```bash
git clone git@github.com:nassimna/agent-config.git ~/.agents
~/.agents/install.sh
```

The installer links:

- `~/.codex/AGENTS.md` to this repository's `AGENTS.md`
- `~/.claude/CLAUDE.md` to this repository's `CLAUDE.md`
- every directory under `skills/` into `~/.claude/skills/`

Codex discovers personal skills directly from `~/.agents/skills/`. The installer
refuses to overwrite existing files or conflicting links; move or review those
targets first, then run it again.

Install and authenticate Codex and Claude separately. Skills that use external
tools need those tools installed too; screen recording currently requires Linux
with X11. This repository does not install applications or migrate login sessions.

## Safety

Keep this repository free of credentials, histories, sessions, caches, logs,
machine-specific settings, and one-use tokens. Review `git diff --cached` before
every commit.
