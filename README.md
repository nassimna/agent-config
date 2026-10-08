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

## Folio HTML artifacts

`html-artifact` creates and checks the review page, then uses
`preserve-html-artifact` to upload it to [Folio](https://folio.devexa.net).
New artifacts are private Previews, grouped by project and thread. Completed
revisions update the same URL; the owner's Keep status and sharing choice stay
intact. Explicit local-only or public-sharing instructions take precedence.

The uploader needs Python 3.9 or newer, Git, and HTTPS access to Folio. Sign in,
verify your email, and create a revocable token in **Settings → Upload tokens**.
Save it using a local editor or private secret-input tool in
`~/.config/artifact-library/upload.json`, with file permissions `0600`:

```json
{"url":"https://folio.devexa.net","token":"YOUR_UPLOAD_TOKEN"}
```

Keep that file outside this repository. No Wrangler, Cloudflare or Resend
credentials are needed. On a configured machine, agents use the installed skill
automatically; start a fresh conversation if an agent cached older instructions.

The helper keeps `.folio-sync.json` beside the HTML to preserve its identity
across revisions and adds local Git ignore rules for the manifest. Keep the
manifest with the editable source; do not commit it. See the
[sync skill](skills/preserve-html-artifact/SKILL.md) for upload commands, bundled
assets and conflict handling.

## Safety

Keep this repository free of credentials, histories, sessions, caches, logs,
machine-specific settings, and one-use tokens. Review `git diff --cached` before
every commit.
