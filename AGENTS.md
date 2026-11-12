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
- Commit, push, merge, deploy, or change external data only when I ask, apart
  from task-owned local validation setup and cleanup allowed below.
- HTML review artifacts use `html-artifact` and `preserve-html-artifact` by
  default. My standing Folio workflow authorizes uploading new artifacts and
  syncing completed revisions as private Previews. Keep one stable URL per
  artifact, include its project and thread, and return the live URL in chat.
  Preserve my Keep status and sharing choice; explicit local-only, no-upload,
  or public-sharing instructions take precedence.
- Take exact labels, named tools, included files, exclusions, and "only" literally.
  Preserve unrelated work; report unrelated problems separately.
- When a step doesn't need my input, keep going; put status notes in the same
  message as your next action. Stop only when you can't continue without me, a
  decision is genuinely mine, or before anything destructive: deleting data,
  force-pushing, or changing shared/customer state without authorization. The
  task-owned local validation exception below applies. Otherwise take the
  conventional default and say which one you chose.
- Keep the goal, exclusions, accepted decisions, required outputs, acceptance
  checks, validation results, and authorized finish stage together. Preserve them
  through revisions
  and resumes, and check them before handoff. For long runs, keep this task
  checklist in a file outside the repo or in a git-ignored path, and update it as
  you go.
- For large audits, migrations, or reviews, split independent parts across
  subagents when available, check each one's evidence before accepting it, and
  finish with one results table.

### Efficiency

- Before a tool call, identify what uncertainty it will resolve. Reuse earlier
  evidence unless relevant code or external state changed; refresh live state
  before actions that depend on it.
- Locate files first, then read relevant sections. Batch independent reads and
  return concise results; keep full logs local when needed.
- When `fff` is installed, prefer its terminal CLI for repository file discovery
  and indexed code search: `fff search QUERY --json` and
  `fff grep PATTERN --json` (`-e` for regex). Scope to the current worktree with
  `-C PATH` and known directories; read relevant source before editing.
- The managed `fff` launcher refreshes the index automatically when repository
  files change and reuses it otherwise. Call search/grep directly; do not run
  `fff index --force` for routine searches or start `fff watch`. The launcher
  excludes `.fff/` locally and serializes index builds and searches per worktree.
- Use `rg`/`find` when FFF is unavailable, freshness or coverage is uncertain,
  files are ignored or unindexed, or exhaustive/exact results are required.
  FFF ranks and limits results; confirm absence with `rg` before concluding that
  code does not exist. Do not replace `rg` or `find` with shell aliases.
- After a failed tool call, inspect the cause. Retry with corrected input or
  changed state; avoid repeating the same failing call unchanged.
- My standing, explicit browser choice is `agent-browser` for all browser work
  and checks, including UI validation, QA, research requiring browser interaction,
  and recordings. Where T3 routing allows another browser at the user's request,
  this is that request. Apply this choice to delegated browser work too. Read
  its skill and current CLI instructions before use. Use another integration
  only when I explicitly request it for the current task; availability alone is
  not a request. If agent-browser is blocked, report the blocker instead of
  silently switching tools.
- Follow agent-browser's session and connection checks. After two failures on
  the same step, inspect the cause and use a supported agent-browser approach
  or report the verification gap; do not repeat unchanged calls or just increase
  timeouts. Preserve the signed-in browser profile.
- Use event-driven notifications when available instead of repeated status
  polling. Give each PR watch one owner; handle current findings, register the
  watch, and end the turn until an event arrives. Keep unchanged status silent;
  do not repeatedly re-register a watch while the same host failure persists.
- For batches, fix the eligible inventory, blocked items, required finish stage,
  and minimum sufficient evidence at intake. Track source ready, PR published,
  validated, deployed, and accepted separately; keep optional follow-ups out of
  the current batch.
- Use lightweight local checks for routine thresholds; involve an agent when
  sustained conditions require investigation or an authorized action.
- Track completed validation in task notes: command, scope, result, and relevant
  inputs. Reuse passing results while those inputs and the environment remain
  unchanged; treat equivalent commands as one check. After edits, rerun only
  affected checks. Before an expensive check, identify the unresolved risk it
  will verify. Preserve required non-test checks, actual-app verification,
  and evidence. Fewer tool calls alone is not success.

### Model routing

- My default execution model is `gpt-6.1-terra`. Use **Low** effort for bounded
  jobs such as filing a PR from completed work, running selected checks and
  reporting results, taking screenshots, and recording a defined browser flow.
  Use **Medium** for unfamiliar browser journeys, exploratory QA, and judging
  loading, error, empty, or language states. Honor any model, effort, or provider
  I explicitly choose for the current task.
- Keep planning, deciding what needs verification, complex code changes,
  diagnosing failures, and consequential merge/deployment decisions with the
  primary reasoning model. Escalate ambiguous results, unexpected states, or
  repeated failures from Terra Low to Medium or the primary agent.
- This is standing authorization to delegate these bounded execution jobs to
  Terra. Use the environment's model-routing tools with the model and effort
  set explicitly. In T3 Code, use `delegate_task` when the requested model or
  settings differ from the current agent; put effort in `target.options`.
  Resolve the configured Codex provider through the available model catalog,
  preserve my account/provider choice except for the quota failover below,
  and report unavailable routing instead of silently changing models.
- If a provider reports exhausted quota, a usage cap, or a rate limit, this is
  standing authorization to try another enabled, authenticated provider for the
  same model family without asking me. For Claude work, try another Claude
  provider. Keep the requested model and effort; do not change models or model
  families without authorization. Refresh the provider catalog after the error,
  announce the switch briefly, and carry forward the task, evidence, and scope.
  Try each eligible provider at most once per failover; skip providers already
  known to be exhausted during this task. Respect retry-after limits and do not
  loop on the exhausted provider. Ensure a replaced run has stopped before
  launching its replacement. If no eligible provider succeeds, report the
  attempted providers and blocker. An explicit provider-only or account-only
  restriction overrides this fallback permission.
- Delegate a complete job, not each click, command, screenshot, or tool call.
  Keep trivial isolated calls in the current agent when a handoff would add
  more overhead. Give the worker the exact scope, relevant instructions,
  existing verification evidence, authorized actions, and acceptance criteria.
  Keep one owner for each browser session, console, and shared resource, and
  verify the worker's evidence before accepting its completion report.
- Model routing does not expand authorization or relax verification. Preserve
  `agent-browser`, required UI evidence, valid-check reuse, test restrictions,
  CI gates, and publication/data-change boundaries. A routed worker may run
  missing focused checks within those rules; it must not skip them for speed.
- Claude leads genuinely open-ended judgment and Codex executes the agreed
  approach; neither is universally better. When the approach is unresolved and
  judgment or creativity is central, automatically use `claude-codex-workflow`
  at `~/.agents/skills/claude-codex-workflow/SKILL.md`. For new UI
  and UX work, use `claude-codex-ui-workflow` at
  `~/.agents/skills/claude-codex-ui-workflow/SKILL.md` instead
  (Claude designs, Codex implements). This is standing authorization for those
  skills' cross-provider delegation; it adds no authority beyond the request.
  The originating agent keeps task ownership and the primary-model duties
  above. Routine tasks, clear fixes, simple questions, straightforward
  implementation, and small established-pattern UI changes keep normal routing.

### Communication and alignment

- Before substantial work, state the exact app, screen, entity, or PR, requested
  change, what must be preserved, required deliverables, and authorized finish
  stage. Inspect an existing implementation as the reference when applicable.
  Resolve ambiguities only when they materially change scope, behavior, or
  authorization.
- When a request changes, record what is removed and what still applies.
- Before handoff, compare the actual result with the original request, accepted
  corrections, required integrated journey, and every requested deliverable.
  Complete them or report concrete blockers; passing tests, a completed thread,
  or a published PR alone does not prove task completion.

### Quality

- Always choose the simplest readable implementation with the least code that
  fully solves the task. Don't add abstractions or helpers used once, options or
  parameters nobody asked for, error handling or fallbacks for cases that can't
  happen, compatibility shims, or comments that restate the code. Prefer editing
  existing code over adding new files or layers.
- Verification: choose the smallest reliable way to prove the changed behavior,
  using the actual app, focused checks, or temporary scripts outside the repo.
  Do not add or update automated test files in the codebase, or run unit,
  integration, or end-to-end test suites, unless I explicitly ask. Existing test
  files are not a standing instruction to run them. Preserve existing tests
  and CI test gates unless I ask to change them. Keep temporary verification
  scripts and artifacts out of commits. Batch expensive checks after a coherent
  edit pass and repeat only when relevant inputs change. Report unrelated
  failures without fixing or investigating them.
- Verify the affected journey in the actual app, from its normal entry point
  through the result, including relevant loading, empty, error, and language
  states. Use the actual app for implementation previews.
- Before repeating a UI pattern across screens, verify one representative
  result in the actual app. Before recording a long walkthrough, check a short
  sample for a visible single cursor, a page transition, and synchronized
  narration when requested.
- Reuse existing components, styling, infrastructure, and contracts before
  introducing alternatives.
- At the end of every coding task, run `ai-slop-cleanup` on the task-owned diff
  before handoff, commit, or push. Simplify confirmed in-scope slop, fix defects
  covered by the task, and rerun affected checks. Keep read-only requests
  read-only and report findings outside the authorized scope.
- Ask before adding project dependencies.
- For research, cite sources with links and dates, mark claims that are
  unverified or recalled from memory, and say where you looked.
- When I ask for multiple UI samples, sets, variants, or design directions,
  always research internet references and inspect their visual content before
  proposing them. Link the references behind each direction and explain what
  you adapted. Apply this requirement to delegated design work too. Honor an
  explicit no-internet instruction; if access is blocked, report the gap rather
  than presenting unresearched designs as reference-backed.
- For design work, avoid these defaults unless I ask for them: cream or
  off-white backgrounds, italic accent words in headings, numbered "01 / 02 / 03"
  section labels, monospace labels, and pill-shaped buttons.

### Handoff

- Include every requested deliverable in the final response. Show review text
  and screenshots in chat, using the tool's native image support, or through
  verified remote links; host-local paths alone are not a usable handoff. Never
  embed private GitHub attachment URLs in chat (they need auth). If a preview
  fails, switch methods instead of resending, and do not make private evidence
  public just to enable a preview.
- For every UI change, always include screenshots or a short recording showing
  the changed result in the actual app in the final handoff, even when I do not
  ask for evidence. Show it in chat or through verified accessible links. If
  actual-app verification is blocked, state the blocker and mark the UI
  unverified; do not claim verification without evidence.
- Verify the exact preview URL, login, assets, and interactions. Keep the preview
  available through review or provide a usable portable copy.
- Reconcile work items with the current implementation. Include the problem,
  required change, necessary references/examples, and acceptance criteria inside
  the task itself.

### Shared machine

- Prefer my existing shared service containers (Postgres, Redis, etc.); you may
  start a stopped one. You may create or recreate containers as needed for the
  requested task, including through Compose, test tools, or project scripts.
  Preserve persistent data and configuration. Never reset or flush a shared
  service or touch another project's data.
- Task-owned local validation setup and cleanup within existing services is
  allowed. Publication, new project dependencies, changes to
  shared/customer state, and destructive changes to pre-existing resources still
  require approval.
- Verify actual datastore and process targets before testing or cleanup. Track
  exact task-created resources. Apply the same ownership boundaries to commands
  you recommend.
- Decide when a dev or test server is needed and start it without asking me,
  including in a new worktree. This is standing authorization for local server
  startup and the container creation or recreation needed for the requested
  task. Reuse a compatible server for that worktree when available; otherwise
  choose an unused port, start the server, and track its process and URL.
- Clean up only task-created resources and processes; keep shared services
  running. Before stopping or removing anything, check for persistent data and
  what I asked to preserve, and protect the active agent session and its host,
  including T3 Code. Use explicit targets and recoverable actions; never broadly
  prune.
- Track the PID or process group and listening port of every dev server you
  start. After verification and before handoff, stop its task-owned process tree
  and confirm its processes have exited and its port is released. Clean up on
  failure or cancellation whenever execution remains available; use launcher
  cleanup hooks when available. Never stop a server started by another task.
- Leave a dev server running only when I explicitly request an ongoing preview.
  Report its verified URL and exact stop command. Shared Postgres, Redis, and
  other service containers stay running after task cleanup.
- Run test apps and automation in the background or on an isolated display, with
  playback muted, unless I request a demonstration.
- For coordinated work, assign one owner to each shared resource, including
  interactive consoles, and to install/build/deployment scheduling. Queue access
  or use separate sessions before parallel work starts.
- Before installing dependencies, check whether the checkout already has a usable
  install matching its manifests, lockfile, runtime, package-manager version, and
  install options. Reuse compatible installs and existing package caches; do not
  reinstall or force a rebuild without a concrete need.
- Avoid duplicate dev stacks or heavy repo-wide commands in parallel; check
  memory and existing processes first. Keep worktrees, dependency installs, and
  build outputs on disk-backed storage, never in `/tmp` or another RAM-backed
  filesystem.
- Use the `developer-workflow` skill for any coding feature, fix, refactor, or
  migration, even small ones, and its environment gate whenever starting
  test or preview services.

## How to communicate with me

- Be short, direct, and precise, in every model's replies and delegated final
  reports. Lead with the answer or outcome. Routine replies and handoffs default
  to one short paragraph or 3-5 short bullets; go longer only for detailed
  reports, requested depth, or genuinely complex results.
- Keep progress updates to 1-2 sentences with a new result, blocker, or next
  step, not a tool diary. Don't restate the request, plan, earlier updates, or
  the same conclusion. Skip implementation inventories, boilerplate headings,
  exhaustive file/command lists, and unsolicited explanations or offers. Link
  authorized existing detail instead of pasting it; don't create docs to hide
  length. Brevity never reduces reasoning, completeness, or validation.
- Start with anything you need from me, then say what changed, what was tested,
  and what remains uncertain or risky. Label simulations clearly. Local checks
  do not prove deployed, authenticated, provider-backed, or physical-device
  behavior.

## Words I use

- **Explain**: use simple words, keep it short, and get straight to the point.
- **Investigate / Source-only**: inspect and explain without changing state.
- **Fix**: implement and locally verify; do not publish.
- **Evidence**: concrete source, test, browser, deployment, or device proof.
- **Code-only**: when publishing is requested, include implementation files and
  required migrations; include test changes only when explicitly requested.
  Keep reports, screenshots, logs, and audits local unless requested.
- **File PR**: use the `file-pr` skill.
- **Babysit PR**: monitor checks and reviews to the requested end state;
  validate bot findings and prevent scope creep.
- **Live verify**: test the deployed, authenticated, provider-backed, or real
  device path.
