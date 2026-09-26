---
name: extract-repo-patterns
description: Derive practical agent rules from a repository's actual code and contracts. Use when the user asks to document repo patterns, create repo-specific agent guidance, or compare implementation conventions across repositories.
---

# Extract Repo Patterns

Use this skill to inspect a real repository and produce practical agent-facing
implementation rules. The output should help future agents make changes in the
same style as the repo, not produce a generic architecture essay.

## Workflow

1. Identify scope

- Use the current repo unless the user names another path.
- If the user names a reference repo, inspect both the current repo and the
  reference repo.
- Decide whether the request is a read-only review or asks for saved guidance.
  Do not create or edit files during a read-only review.
- Only when the user asks for a file, create or update a repo-local Markdown
  file such as `docs/agents/repo-patterns.md`.

2. Read existing agent instructions first

- Read `AGENTS.md`, `.agents/`, `.codex/`, and existing `docs/agents/` files
  when present.
- Preserve stronger existing rules. Add only missing repo-specific guidance.

3. Map the actual code shape

Start with a breadth-first inventory of the whole repo before naming the
architecture:

- list tracked files and top-level folders with `rg --files`, `find`, and
  package/workspace metadata
- identify every app, service, package, tool, config area, generated area, and
  test area
- read representative files from each major folder before deciding what the
  folder means
- note repeated file names, import paths, naming conventions, and test locations
- mark generated/vendor/build output so it does not become a source of patterns

Only after that, classify the repo type from evidence. It may be frontend,
backend, full-stack, library/package, CLI, mobile, infrastructure, data/ML, or a
monorepo containing several of these.

Inspect the universal surfaces:

- package/build metadata and dependency stack
- entrypoints, app/service/package boundaries, and folder layout
- configuration, environment, secrets, and deployment files
- runtime data boundaries: API payloads, schemas, commands, jobs, events, DB
  models, generated clients, file formats, or external services
- tests, lint, typecheck, build, migration, seed, and deploy commands
- naming conventions, import aliases, error handling, logging, and observability
- existing agent instructions and documented architectural decisions

Then inspect the repo-type-specific surfaces that the inventory proves are
present. Treat these as discovery prompts, not expected structures:

- UI surfaces: routing, screens, components, state, data fetching, forms,
  validation, localization, dates, styling, accessibility, browser checks.
- Server/API surfaces: externally exposed endpoints, request flow, validation,
  auth, permissions, persistence, transactions, jobs, migrations, contracts,
  integration tests.
- Package surfaces: public exports, build output, typing, examples, release
  scripts, compatibility tests.
- CLI/tooling surfaces: commands, config loading, filesystem behavior, prompts,
  stdout/stderr, exit codes, snapshots/e2e tests.
- Infrastructure surfaces: environments, state, secrets, CI/CD, plan/apply,
  drift detection, rollback and safety rules.
- Data/ML surfaces: pipeline stages, dataset contracts, model/artifact layout,
  reproducibility, evaluation, scheduled jobs, notebooks vs production code.

Use `rg --files`, `find`, `sed`, targeted source reads, and `jq` when it is
available and useful. Do not infer patterns from filenames alone.

4. Separate source of truth from guesses

- For contracts, inspect the strongest source available: OpenAPI/Swagger,
  protobuf/GraphQL schemas, database schema, generated types, SDKs, backend
  routes, CLI help/snapshots, IaC plans, migration files, or test fixtures.
- If no authoritative source exists, say so. Do not document guesses as facts.
- Flag hardcoded business data, mock records, fake defaults, static option lists,
  fake env values, and copied fixtures separately from acceptable local constants.

5. Extract rules from evidence

For every rule, tie it to observed files or a confirmed contract. Prefer
actionable rules that name the repo's actual paths, tools, and boundaries.

Avoid vague rules:

- "Keep code clean"
- "Follow best practices"
- "Make components reusable"

6. Write the pattern document

Recommended sections:

- Core Rule
- Project Structure
- Repo Type And Stack
- Folder And Boundary Rules
- Runtime Contracts And Source Of Truth
- Data, State, Or Persistence Rules
- Validation, Error Handling, And Security
- UI, API, CLI, Package, Infra, Or Pipeline Rules as applicable
- No Mock Or Hardcoded Business Data unless explicitly accepted
- Verification

The Project Structure section must include a concrete folder tree or table for
the scoped repo, app, package, service, or module. It should mark entrypoints,
feature/module boundaries, shared libraries, tests, configuration, generated
output, vendor/build artifacts to ignore, and any repo-specific placement
rules discovered from evidence.

Keep the document direct and enforceable. Use "Do" and "Do not" language. Do
not include sections that do not apply to the target repo.

7. Wire the document into agent loading

- When the user requested persistent agent guidance, add a short pointer in
  `AGENTS.md` so future agents read the pattern file before changing
  application code.
- For a report-only request, do not change `AGENTS.md` unless the user asks.
- Do not duplicate the whole pattern document inside `AGENTS.md`; link to it.

8. Validate

- Format Markdown with the repo formatter when available.
- Re-read the generated document and verify it names concrete paths and rules.
- If code was not changed, no typecheck/build is needed.

## Output Standard

Final response should include:

- path of the created or updated pattern file
- whether `AGENTS.md` was wired to it
- the most important rules added
- any source-of-truth gaps discovered, especially missing backend contracts for
  business options/defaults, schemas, permissions, database behavior, CLI
  behavior, deployment behavior, or generated artifacts

## Guardrails

- Do not create overbroad abstractions or new docs folders unless needed.
- Do not encode temporary mistakes as permanent patterns.
- Do not assume a conventional frontend, backend, layered, DDD, MVC, service, or
  package structure before the repo proves it.
- Do not make backend claims without checking a backend source of truth.
- Do not hide uncertainty. If a rule is inferred rather than confirmed, label it
  as inferred.
