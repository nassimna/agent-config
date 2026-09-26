# A note from Nassim

I'm Nassim. I use agents for production software, research, deployments, design,
and system maintenance, often through T3 Code. I value exact scope, simple
solutions, real evidence, and reversible actions.

These preferences apply across agent tools. Use the current tool's actual
capabilities and environment.

## How I like us to work

### Scope and autonomy

- Treat questions, reviews, audits, and diagnosis as read-only unless I ask for
  changes. For implementation, make the smallest complete change and verify it.
- Commit, push, merge, deploy, or change external data only when I ask.
- Take exact labels, named tools, included files, exclusions, and "only" literally.
  Preserve unrelated work; report unrelated problems separately.
- When a step doesn't need my input, keep going; put status notes in the same
  message as your next action. Stop only when you can't continue without me, a
  decision is genuinely mine, or before anything destructive: deleting data,
  force-pushing, or changing anything outside the repo. Otherwise take the
  conventional default and say which one you chose.
- For long runs, keep a task checklist in a file outside the repo or in a
  git-ignored path, and update it as you go.
- For large audits, migrations, or reviews, split independent parts across
  subagents when available, check each one's evidence before accepting it, and
  finish with one results table.

### Quality

- Always choose the simplest readable implementation with the least code that
  fully solves the task. Don't add abstractions or helpers used once, options or
  parameters nobody asked for, error handling or fallbacks for cases that can't
  happen, compatibility shims, or comments that restate the code. Prefer editing
  existing code over adding new files or layers.
- Tests: add or update only the tests that cover the behavior you changed,
  usually one or a few focused cases. No exhaustive edge-case suites and no
  tests for code you didn't change. Run only those tests and the checks for the
  files you touched, not the full suite, unless I ask. If you notice other
  failures, mention them in one line; don't fix or investigate them.
- Reuse existing components, styling, infrastructure, and contracts before
  introducing alternatives.
- Ask before adding project dependencies.
- For research, cite sources with links and dates, mark claims that are
  unverified or recalled from memory, and say where you looked.
- For design work, avoid these defaults unless I ask for them: cream or
  off-white backgrounds, italic accent words in headings, numbered "01 / 02 / 03"
  section labels, monospace labels, and pill-shaped buttons.

### Handoff

- Show review text and screenshots in chat, using the tool's native image
  support, or through verified remote links; host-local paths alone are not a
  usable handoff. Never embed private GitHub attachment URLs in chat (they need
  auth). If a preview fails, switch methods instead of resending, and do not make
  private evidence public just to enable a preview.

### Shared machine

- Use my existing shared service containers (Postgres, Redis, etc.); you may
  start a stopped one. Creating or recreating any container, including through
  Compose, test tools, or project scripts, requires my explicit permission. Never
  reset or flush a shared service or touch another project's data.
- Clean up only task-created resources and processes; keep shared services
  running. Before stopping or removing anything, check for persistent data and
  what I asked to preserve, and protect the active agent session and its host,
  including T3 Code. Use explicit targets and recoverable actions; never broadly
  prune.
- Avoid duplicate dev stacks or heavy repo-wide commands in parallel; check
  memory and existing processes first. Keep worktrees, dependency installs, and
  build outputs on disk-backed storage, never in `/tmp` or another RAM-backed
  filesystem.
- Use the `developer-workflow` skill for any coding feature, fix, refactor, or
  migration, even small ones, and its environment gate whenever starting
  test or preview services.

## How to communicate with me

- Be short, direct, and precise. Lead with the answer, prefer bullets, and skip
  long implementation inventories.
- Start with anything you need from me, then say what changed, what was tested,
  and what remains uncertain or risky. Label simulations clearly. Local checks
  do not prove deployed, authenticated, provider-backed, or physical-device
  behavior.

## Words I use

- **Investigate / Source-only**: inspect and explain without changing state.
- **Fix**: implement and locally verify; do not publish.
- **Evidence**: concrete source, test, browser, deployment, or device proof.
- **Code-only**: when publishing is requested, include code, tests, and required
  migrations; keep reports, screenshots, logs, and audits local unless requested.
- **File PR**: use the `file-pr` skill.
- **Babysit PR**: monitor checks and reviews to the requested end state;
  validate bot findings and prevent scope creep.
- **Live verify**: test the deployed, authenticated, provider-backed, or real
  device path.
