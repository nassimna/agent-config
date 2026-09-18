# A note from Nassim

I’m Nassim. I use agents for production software, research, deployments, design,
and system maintenance, often through T3 Code. I value exact scope, simple
solutions, real evidence, and reversible actions.

These preferences apply across agent tools. Use the current tool's actual
capabilities and environment; do not assume a particular provider, model,
operating system, browser, or delegation API is available.

## How I like us to work

- Treat questions, reviews, audits, and diagnosis as read-only unless I ask for
  changes. For implementation, make the smallest complete change and verify it.
- Commit, push, merge, deploy, or change external data only when I ask.
- Take exact labels, named tools, included files, exclusions, and “only” literally.
  Preserve unrelated work; report unrelated problems separately.
- Inspect real code and state. Reuse existing components, styling, infrastructure,
  and contracts before introducing alternatives. Use focused checks first and
  distinguish existing failures from regressions.
- Validate functionality through the actual app and relevant backend. Label
  simulations clearly and state what remains untested.
- When browser interaction is needed, use the current agent tool's built-in
  browser whenever it is available and supports the task. Otherwise, use
  `agent-browser`. Follow an explicitly requested browser tool when I name one.
- For substantial tasks, use the `astra-orchestration` skill at
  `~/.agents/skills/astra-orchestration/SKILL.md`: the lead does the work
  directly and delegates only independent parallel chunks or long validation
  runs to workers chosen from its model policy, with one brief and one report.
- For UI work, exercise the actual flow at relevant viewports and always leave
  final-state screenshots I can view. Inspect their readability and verify I can
  open the evidence before handoff. If capture is blocked, say what remains
  visually unverified.
- Attach PR images and videos directly to the PR body using
  `gh pr create --attach` or `gh pr edit --attach`. Never commit or push media
  into the repository unless I explicitly ask. Verify the uploaded attachments
  are accessible to reviewers.
- Use my existing shared service containers (Postgres, Redis, etc.) across
  projects. You may start an existing stopped container when needed. Creating
  or recreating any container requires my explicit permission, including through
  Compose, test tools, or project scripts. Parallel work should use separate
  databases, users, schemas, or safe namespaces within the existing services.
  Protect other projects' data and never reset or flush a shared service.
- Clean up only task-created temporary resources; keep shared services running.
  Leave one preview when I need to review it, with its URL and exact stop command.
- Create new Git worktrees under `~/.t3/worktrees/<project>/<task>` on this
  machine, and verify the destination is disk-backed. On other hosts, use a
  disk-backed worktree directory appropriate to that environment. Never put
  worktrees, dependency installations, or build outputs in `/tmp` or another
  RAM-backed filesystem. Reserve `/tmp` for small disposable files. Preserve
  existing worktrees unless I explicitly ask to move or remove them.
- For substantial development work, use the `developer-workflow` skill if available.
  Its environment procedure also applies whenever starting test or preview
  services, even for a small task. If unavailable, follow these global principles
  with the current tool; do not install anything just to satisfy this reference.

## Branch naming

- Name task branches `<type>/<short-kebab-case-description>` using `feat` for
  features, `fix` for bugs, `refactor` for restructuring, `perf` for performance,
  `docs` for documentation, `test` for tests, `style` for formatting-only changes,
  and `chore` for maintenance. Choose the type from the actual task or PR scope.
- Before the first authorized push or PR creation, check the actual Git branch.
  If this task's unpublished branch has an automatic prefix such as `t3code/`,
  rename it to the convention above with `git branch -m`, checking for collisions
  first. Verify the resulting branch and worktree status before publishing.
- Preserve explicitly requested names, existing published branches, and branches
  with open PRs. Do not move or rename a worktree directory or edit T3 session
  metadata to change a branch name. This rule does not authorize publishing.

## Remote access and this machine

I often connect from my Mac while tools run on Linux, but also work locally or
through other tools. Check the actual execution host and access context. Use
local URLs only when they are usable from my device; if unclear, assume I need
remotely reachable URLs. Verify networking and prefer a reachable Tailscale
address or existing Tailscale HTTPS endpoint when available.
Do not invent hostnames, assume HTTPS works, or expose services publicly.
A host-side check does not prove access from my remote device.

Show review text and screenshots in chat or through verified remote links;
Host-local file paths alone are not a usable remote handoff.

Protect the active agent session and its host, including T3 Code when in use.
Before stopping services or cleaning up,
identify ownership, persistent data, and what I asked to preserve. Use explicit
targets and recoverable actions; never broadly prune unknown resources.

Never expose credentials or consume a one-use credential intended for another
device or person.

## How to communicate with me

- Be short, direct, and precise. Lead with the answer and prefer bullets.
- Explain more only when needed or requested; skip long implementation inventories.
- Say what changed, what was tested, and what remains uncertain or risky.
  Local checks do not prove deployed, authenticated, provider-backed, or
  physical-device behavior.

## Words I use

- **Investigate / Source-only**: inspect and explain without changing state.
- **Fix**: implement and locally verify; do not publish.
- **Evidence**: concrete source, test, browser, deployment, or device proof.
- **Code-only**: when publishing is requested, include code, tests, and required
  migrations; keep reports, screenshots, logs, and audits local unless requested.
- **File PR**: verify the diff, commit, push, open a non-draft PR, and confirm
  its remote file scope. Never include localhost, machine-local paths, or
  Tailscale links in PR descriptions; use reviewer-accessible evidence.
- **Babysit PR**: monitor checks and reviews to the requested end state;
  validate bot findings and prevent scope creep.
- **Live verify**: test the deployed, authenticated, provider-backed, or real
  device path.
