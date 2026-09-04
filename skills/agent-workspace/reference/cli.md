# agent-workspace-cli — full command reference

Complete surface of the public CLI. Every remote command needs the desktop app
running, prints one compact JSON value on stdout, and writes errors to stderr with a
non-zero exit. `agent-workspace-cli --help` and `<cmd> --help` are authoritative; this
file mirrors them for quick lookup. Start with `SKILL.md` for the common workflow.

## Global options

- `--session-file <PATH>` — explicit discovery-record path (a path, **never** a
  token). Also settable via `AGENT_WORKSPACE_SESSION_FILE`.
- `--window <WINDOW>` — bind each request to a specific desktop window placement.
- `-h/--help`, `-V/--version`.

## Discovery & auth

The CLI locates the owner-only session record in this order:

1. `--session-file PATH`
2. `AGENT_WORKSPACE_SESSION_FILE`
3. Linux: `$XDG_RUNTIME_DIR/agent-workspace/cli-session.json` (UID-scoped temp fallback
   if `XDG_RUNTIME_DIR` is unset); macOS/Windows use a user-scoped temp fallback.

The record is a path to a credential, not a credential itself. There is deliberately no
token flag — never copy the token out of the record or into shell history. The record
is created by the desktop after it binds its transport and removed on shutdown; reads
reject symlinks/oversized/non-0600 files.

## Response shapes

- `identify` → `{ application, version, protocolVersion, capabilities:[…] }`.
- `workspace list` → `{ snapshot: ApplicationSnapshot }` where
  `ApplicationSnapshot = { revision, workspaces:[WorkspaceSnapshot], selectedWorkspaceId,
  shortcutOverrides, attention }`.
- `WorkspaceSnapshot = { id, name, description, color, workingDirectory, layout(PaneTree),
  selectedPaneId, panes:[{ id, tabIds, selectedTabId, title, attention }],
  tabs:[{ id, paneId, title, customTitle, content, createdAt, attention }], createdAt, updatedAt }`.
- A tab's `content` is `{ kind:"terminal", launch, runtimeSessionId? }` or
  `{ kind:"browser", state }`. **The terminal id passed to `terminal send` is that
  `runtimeSessionId`.**
- Mutating commands (`workspace create`, `terminal create`, `pane split`, all `group`
  ops, `layout save/apply/import`, `notify`) return
  `MutationResult = { revision, snapshot: ApplicationSnapshot }`. Read new IDs back from
  `.snapshot` after the call.
- `workspace organization` → `WorkspaceOrganizationSnapshot = { revision, selection:[…],
  focusedWorkspaceId, pins:[…], groups:[…], assignments:[…] }` — the source of
  `--expected-revision` for org/group mutations.

`jq` is not guaranteed to be installed; `python3 -m json.tool` or any JSON parser works.
Capture output to a file/variable before parsing so a missing reader can't break the pipe.

## Optimistic concurrency

Mutating organization commands (`workspace select-many/pin/reorder/close-selected`,
all `group` commands, `layout save/apply/import`) require:

- `--expected-revision <N>` — the current revision from `workspace list` /
  `workspace organization`. The call fails if the store moved on (someone else edited).
- `--idempotency-key <KEY>` — optional; makes a retried call safe (no double-apply).

Read the current revision first, pass it in, and re-read + retry on a revision
mismatch.

## identify

```sh
agent-workspace-cli identify
```
Prints local service identity as JSON. Cheapest liveness check.

## workspace

| Subcommand        | Required                                                                 | Optional |
| ----------------- | ------------------------------------------------------------------------ | -------- |
| `list`            | —                                                                        | — |
| `create`          | `--name`, absolute `--working-directory`                                 | `--description`, `--color`, absolute `--terminal-cwd`, `--rows`(24), `--cols`(80), trailing `--command CMD...` |
| `organization`    | —                                                                        | — |
| `select-many`     | `--focused-workspace-id`, `--expected-revision`                          | repeatable `--workspace-id`, `--idempotency-key` |
| `pin`             | `--workspace-id`, `--expected-revision`                                  | `--pinned` (flag; presence pins), `--idempotency-key` |
| `reorder`         | `--workspace-id`, `--destination-index`, `--expected-revision`           | `--idempotency-key` |
| `close-selected`  | `--expected-revision`                                                    | `--replacement-name/-description/-color/-working-directory/-terminal-cwd/-rows/-cols`, trailing `--replacement-command CMD...`, `--idempotency-key` |

```sh
agent-workspace-cli workspace list
agent-workspace-cli workspace list | jq -r '.workspaces[] | "\(.id)  \(.name)"'
agent-workspace-cli workspace create --name "Project" --working-directory /abs/path
agent-workspace-cli workspace create --name "Tests" --working-directory /abs/path \
  --rows 30 --cols 120 --command bash -lc 'pnpm test'
```

`workspace list` is the map of the world: workspaces → pane tree → terminals, each with
its UUID, plus working dir, git branch, selected process, and listening ports. Pull the
`workspace id`, `pane id`, and `terminal id` you need from here.

## terminal

| Subcommand | Required                                             | Optional |
| ---------- | ---------------------------------------------------- | -------- |
| `create`   | `--workspace-id`, `--pane-id`, absolute `--cwd`      | `--destination-index`, `--rows`(24), `--cols`(80), trailing `--command CMD...` |
| `send`     | `--terminal-id`, `--data`                            | — (alias: `terminal input`) |

`--data` is raw UTF-8; you supply newlines. Rows/cols accept 1–65535.

```sh
agent-workspace-cli terminal create --workspace-id WS --pane-id PANE --cwd /abs/path
agent-workspace-cli terminal send --terminal-id T --data $'pnpm build\n'
agent-workspace-cli terminal send --terminal-id T --data $'\x03'      # Ctrl-C
agent-workspace-cli terminal send --terminal-id T --data $'\x04'      # Ctrl-D / EOF
```

## pane split

```
pane split --workspace-id WS --target-pane-id PANE --axis <horizontal|vertical> \
  [--placement <before|after>] [--ratio <0..1>] <CONTENT>
```
`--placement` defaults to `after`; `--ratio` defaults to `0.5` (strictly between 0 and
1). `<CONTENT>` is exactly one of:

- `terminal --cwd <abs> [--rows N --cols N --command CMD...]`
- `browser --url <URL> [--profile-partition <NAME>]`
- `existing-tab --tab-id <UUID>`

```sh
agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis vertical --ratio 0.5 terminal --cwd /abs/path
agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis horizontal browser --url https://example.com/
agent-workspace-cli pane split --workspace-id WS --target-pane-id PANE \
  --axis vertical existing-tab --tab-id TAB
```

## notify

```
notify --title <T> [--body <B>] [--level info|warning|error] \
  [--workspace-id WS] [--pane-id PANE] [--tab-id TAB]
```
Level defaults to `info`. With no target IDs it targets the currently selected
workspace. Env fallbacks: `AGENT_WORKSPACE_WORKSPACE_ID`, `AGENT_WORKSPACE_PANE_ID`,
`AGENT_WORKSPACE_TAB_ID` (explicit flags win).

## group

Create/rename/delete/move/assign/collapse workspace groups. All mutate and take
`--expected-revision` (+ optional `--idempotency-key`).

- `group create --group-id <ID> --name <NAME> --expected-revision <N>`
- `group rename --group-id <ID> --name <NAME> --expected-revision <N>`
- `group delete --group-id <ID> --expected-revision <N>`
- `group move   --group-id <ID> --destination-index <N> --expected-revision <N>`
- `group assign --workspace-id <WS> [--group-id <ID>] --expected-revision <N>`
  (omit `--group-id` to unassign)
- `group collapse --group-id <ID> [--collapsed] --expected-revision <N>`

## layout

Portable saved layouts (JSON you can move between machines).

- `layout list`
- `layout get --layout-id <ID>`
- `layout export --layout-id <ID>` → prints the portable JSON
- `layout save --layout-id <ID> --name <NAME> [--workspace-id WS ...] --expected-revision <N>`
- `layout apply --layout-id <ID> --expected-revision <N>`
- `layout import --layout-id <ID> --file <PATH> --expected-revision <N>`
- `layout delete --layout-id <ID>`

## action

Stable, versioned public actions with bounded parameters (an extensible command bus).

- `action list [--cursor <C>] [--limit <N=64>]` — one page of action definitions; each
  carries an `id`, `version`, parameter schema, and the current `idempotency-epoch`.
- `action invoke --action-id <ID> --action-version <V> --idempotency-epoch <E>
  [--parameters-json '<JSON>'] [--idempotency-key K] [--correlation-id C]
  [--target-window-id W] [--target-window-generation G]`
- `action cancel --invocation-id <ID> --correlation-id <C>`

Discover with `action list` before invoking; the epoch comes from that listing.

## browser automation

`browser automation <op>` — closed, capability-gated browser operations against panes'
isolated browser views (not general web browsing). Ops: `session-create`,
`session-list`, `session-get`, `session-destroy`, `navigate`, `wait`, `query`, `focus`,
`click`, `type`, `key`, `key-at`, `screenshot`, `screenshot-read`, `screenshot-release`,
`cancel`. Use `agent-workspace-cli browser automation <op> --help` for each op's flags.

## hook (agent notification integration)

The only commands that don't need the desktop running. Install reversible, user-level
notification hooks so another agent's events surface in the workspace.

- `hook install <codex|claude>` / `hook status ...` / `hook uninstall ...`
- `hook codex <JSON payload argv>` — adapter entry point (Codex calls this)
- `hook claude` — adapter entry point, reads bounded JSON on stdin (Claude calls this)

What install writes:
- **Codex** → `~/.codex/config.toml`: `notify = ["/abs/agent-workspace-cli","hook","codex"]`
- **Claude** → `~/.claude/settings.json`: appends one owned entry to `hooks.Notification`
  running `<abs cli> hook claude`.

Idempotent; only installer-owned values are touched. Uninstall restores/removes only
those and reports `conflict` (refusing) if the user edited the managed value. Installer
state + first backups live under
`${XDG_STATE_HOME:-~/.local/state}/agent-workspace/hooks/`. No token, socket path, or
endpoint is ever written into agent configs; hook payloads are size-bounded, processed
in memory, and only sanitized title/body/type are published.

## Failure modes

- Discovery/session error → the desktop isn't running (or the record is stale/insecure).
  Start the app; don't retry blindly.
- Revision mismatch on a mutating org/group/layout command → re-read `workspace list`
  / `workspace organization`, pass the fresh `--expected-revision`, retry.
- Requests time out after a bounded interval. The CLI cannot supply arbitrary control
  commands, raw tokens, or general browser automation.
