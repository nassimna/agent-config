---
name: agent-workspace
description: Control the local Agent Workspace desktop app through agent-workspace-cli. Use when the user asks to inspect or change its workspaces, panes, terminals, layouts, browser panes, or notifications.
metadata:
  short-description: Control the Agent Workspace desktop app via agent-workspace-cli
---

# Agent Workspace

Agent Workspace is a local desktop app for terminal-driven development: workspaces
that contain recursively split panes (terminals, browser views, tabs). The public,
scriptable surface is the **`agent-workspace-cli`** command, which talks to the
running desktop's local service and prints **one compact JSON value on stdout** per
command (errors go to stderr, non-zero exit).

Use this skill whenever you're asked to inspect or manipulate the workspace: list or
create workspaces, open terminals, run a command in a pane, send keystrokes to a live
terminal, split panes, open a browser pane, manage layouts/groups, or post a
notification.

## Before anything: the CLI and the desktop

1. **The desktop app must be running** for every command except the local `hook`
   commands. If a command fails with a discovery/session error, the desktop isn't
   running — say so; don't retry blindly.
2. **Find the CLI.** Try in order and use the first that works:
   - `agent-workspace-cli` on `PATH`
   - the `$AGENT_WORKSPACE_CLI` env var (absolute path to the binary)
   - the resolver bundled with this skill: `scripts/aw` (prints/execs the resolved
     binary). Run `<this-skill-dir>/scripts/aw --which` to print the resolved path.
   - a dev build: `<repo>/target/release/agent-workspace-cli` (or `target/debug/...`)
   Examples below use `agent-workspace-cli`; substitute the resolved path.
3. **Every command prints one JSON value on stdout.** Parse it (with `jq` if
   installed, `python3 -m json.tool`, or your own JSON reading) — never scrape text.
   Don't pipe into a reader that may exit early (a missing `jq` closes the pipe and
   the CLI reports a broken-pipe error); capture to a file or variable first if unsure.

Authoritative interface: `agent-workspace-cli --help` and `<cmd> --help`. Full
command surface (groups, layouts, actions, browser automation, organization):
see `reference/cli.md`.

## Core workflow

Almost every task follows: **identify → list → pick IDs → act → (notify)**.

```sh
# 1. Confirm the service is reachable
agent-workspace-cli identify

# 2. Snapshot everything (workspaces → panes → tabs, each with its UUID)
agent-workspace-cli workspace list > /tmp/aw.json

# 3. Pull the IDs you need (jq shown; python3/any JSON reader works too)
jq -r '.snapshot.workspaces[] | "\(.id)  \(.name)"' /tmp/aw.json
```

### Response shapes (important)

- `workspace list` → `{ "snapshot": { revision, workspaces:[…], selectedWorkspaceId } }`.
  Workspaces are at **`.snapshot.workspaces[]`**.
- Mutating commands (`workspace create`, `terminal create`, `pane split`, group/layout
  ops, `notify`) return **`{ "revision": N, "snapshot": {…} }`** — the same snapshot,
  updated. Read the new IDs back out of `.snapshot` after the call.

### Where the IDs live (all UUIDs)

- **workspace id** → `.snapshot.workspaces[].id`
- **pane id** → `.snapshot.workspaces[].panes[].id` (current one: `.selectedPaneId`)
- **terminal id** (what `terminal send` wants) → a terminal tab's runtime session:
  `.snapshot.workspaces[].tabs[] | select(.content.kind=="terminal") | .content.runtimeSessionId`
  (may be null until the runtime session is live)

## Essential commands

### Create a workspace (with its first terminal)
Working directories must be **absolute**. `--terminal-cwd` defaults to
`--working-directory`. Put `--command` last if any value starts with `-`.

```sh
agent-workspace-cli workspace create \
  --name "Project" --working-directory /abs/path/to/project

agent-workspace-cli workspace create \
  --name "Tests" --working-directory /abs/path/to/project \
  --rows 30 --cols 120 --command bash -lc 'pnpm test'
```

### Add a terminal to an existing pane
Use the workspace id + pane id from `workspace list`.

```sh
agent-workspace-cli terminal create \
  --workspace-id WORKSPACE_UUID --pane-id PANE_UUID --cwd /abs/path
```

### Run something / send keystrokes to a live terminal
Input is raw UTF-8; include the trailing newline yourself to "press Enter".
`terminal input` is an alias for `terminal send`.

```sh
agent-workspace-cli terminal send --terminal-id TERMINAL_UUID --data $'pnpm build\n'
agent-workspace-cli terminal send --terminal-id TERMINAL_UUID --data $'\x03'   # Ctrl-C
```

### Split a pane
`--axis horizontal|vertical`, `--placement before|after` (default after),
`--ratio` in (0,1) default 0.5. The new pane's content is exactly one of
`terminal`, `browser`, or `existing-tab`:

```sh
agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis vertical --ratio 0.5 terminal --cwd /abs/path

agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis horizontal browser --url https://example.com/

agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis vertical existing-tab --tab-id TAB_UUID
```

### Post a notification into the workspace
`--level info|warning|error` (default info). With no target IDs it hits the
currently selected workspace.

```sh
agent-workspace-cli notify --title "Build complete" --level info
agent-workspace-cli notify --title "Review needed" --body "Tests failed" \
  --level warning --workspace-id WS --pane-id PANE
```

## Notification hooks (works for Codex and Claude Code)

The CLI can install reversible, user-level notification hooks so another agent's
"needs attention" events surface in the workspace. These are the only commands that
don't need the desktop running.

```sh
agent-workspace-cli hook install codex     # writes ~/.codex/config.toml notify=[...]
agent-workspace-cli hook status  codex
agent-workspace-cli hook uninstall codex

agent-workspace-cli hook install claude    # appends a hooks.Notification entry to ~/.claude/settings.json
agent-workspace-cli hook status  claude
```

Installs are idempotent and only touch installer-owned values; uninstall reports
`conflict` and refuses if the user edited the managed value. No tokens or socket
paths are ever written into agent configs. Details: `reference/cli.md`.

## Gotchas

- **Absolute paths only** for `--working-directory`, `--terminal-cwd`, `--cwd`.
- **`--command` goes last** when its args start with `-` (e.g. `-lc`); it consumes
  the rest of the line.
- **Newlines are explicit** in `terminal send` — no trailing `\n` means the command
  is typed but not run.
- `rows`/`cols` accept 1–65535; `--ratio` must be strictly between 0 and 1.
- The CLI is **not** a raw protocol escape hatch — it can't run arbitrary control
  commands or read auth tokens; requests time out and fail if the desktop is down.
- One JSON value per call on stdout; check the exit code and read stderr on failure.

## More

`reference/cli.md` documents the complete surface: `workspace`
list/create/organization/select-many/pin/reorder/close-selected, `group`,
`layout` (save/export/import/apply portable layouts), `action` (discover/invoke
stable public actions), `browser automation`, plus discovery/auth internals.
