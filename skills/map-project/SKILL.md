---
name: map-project
description: Generate or refresh a project's agent-readable feature map and user flows from its actual source. Use when asked to map a project, document agent navigation or create feature/journey maps. Not for ordinary coding, repository style rules or proving an app works.
---

# Map Project

Give the next agent a compact guide to what this project does, how users reach
its features, and where to inspect or verify each flow. Generate the map inside
the selected project. This is documentation work, not authorization to modify
product code, install tools, start services, publish or change external data.

## Establish the target and existing map

Use the project/app the user names; otherwise use the current repository. Read
its applicable AGENTS.md and existing verification skills, maps and relevant
docs first. Reuse the established destination and structure. Do not create a
second map beside a maintained one or overwrite human-owned content wholesale.
If the current folder is not an identifiable project and no target is supplied,
ask for the target instead of mapping the home directory or guessing a repo.

When no map exists, use `.agents/project-map/README.md` as the index and
`.agents/project-map/flows/<feature>.md` for details. Respect an explicit output
path. A request to generate/update maps authorizes these local documentation
writes and a short loading pointer in the applicable project AGENTS.md; do not
commit them. A question/review stays read-only and only proposes changes.
Do not create a new project AGENTS.md solely for the pointer when none exists;
the development workflow knows the default map location.

## Discover behaviors from source

Inventory exposed apps, routes, screens, navigation, CLI commands, service
endpoints, jobs and public package entry points before selecting flow details.
Use the user's file-search conventions. Exclude build/vendor/generated output
from the explanation, while reading an authoritative generated contract when
needed. Do not treat every source file as a separate user feature.

Trace each mapped behavior from its normal entry to its result: navigation or
command → input/state → handler/service → authorization/validation → storage or
external boundary → observable outcome. Follow imports and real contracts;
filenames, route names and old docs alone are not proof. Name concrete source
paths/symbols. Record unavailable backend/provider behavior as unknown.

Use the declared scope. Without one, index all discovered exposed feature areas
and map their principal flows. In a large monorepo, group by app/domain and
finish coherent slices. List discovered but unmapped areas explicitly with the
reason and next slice; never label a partial map complete. Delegate independent
source slices only when available and authorized, with one owner for writing
and no simultaneous browser driving. Prefer a compact useful map to an API dump.

## Write a map another agent can use

The index records project/app boundaries, source revision or working state,
inspection date, map scope and coverage. For each area, link its flow file and
normal entry, state whether mapped or pending, and name any access/source gap.
Distinguish the feature inventory from an implementation backlog.

Each flow file contains only applicable fields:
- **Purpose and entry:** user goal, actual menu/route/command/public entry point,
  roles/tenant context and how to reach it through normal navigation.
- **Prerequisites:** required data, account state, flags and environment variable
  names; link existing setup instructions. Never include credentials or tokens.
- **Flow:** ordered actions, branch points and observable outcomes. Use a small
  Mermaid flowchart when it clarifies branches; text steps remain authoritative.
- **Implementation:** source paths/symbols for the UI/CLI, handlers, contracts,
  authorization, persistence and external boundaries; enough to trace the path.
- **States and side effects:** relevant loading, empty, invalid/error, success,
  cancel and persistence states; mark each evidenced, not applicable or unknown.
  Include activity writes on reads, provider calls and destructive actions.
- **How to verify:** the existing app/CLI/browser recipe and decisive observable
  proof. Copy commands only from confirmed scripts/help/source. State safe target
  and mutation boundaries; a plan to run a command is not evidence it ran.
- **Evidence and freshness:** source citations, inspected revision/working state,
  runtime checks actually performed and remaining gaps. Runtime status is
  `unverified`, `verified`, `failed` or `blocked`; source-only maps start unverified.

Use relative file links that resolve from each document. Avoid duplicating whole
schemas or code; link the source. Do not invent selectors, startup commands,
permissions, data or backend guarantees to fill an empty field. Unknown is useful.
For the source of the verification-map approach, see [sources](references/sources.md).

## Validate and hand off

Check every generated local link and source anchor against the project. Confirm
that the entry reaches the named handler and that branches reflect actual code.
A source map can be useful without launching the app: do not run suites or write
application state just to claim coverage. If runtime verification is requested,
use the existing project recipe, agent-browser for web work and applicable
readiness/ownership rules; keep source coverage separate from live proof.

Reread generated files for made-up steps, secrets, duplicated content and missing
areas. The handoff names the map index, covered/pending areas, evidence level and
any blocker. No time-saving claim follows from generating Markdown.

When a later authorized change touches a mapped flow, update that flow and the
index's freshness/coverage when necessary; preserve other entries. In a read-only
task, report drift instead. Do not rewrite a map to hide a product regression.
