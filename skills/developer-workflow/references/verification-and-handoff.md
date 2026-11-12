# Verification and handoff

Use existing task notes as the single record; scale detail to the risk.

## Readiness and data
Before driving a journey, establish target URL/datastore and available build
identity, process/port ownership, browser connection, valid session/role and
required representative records. Report ready, blocked or unknown facts without
printing credentials. A responding process or empty database is not proof that
the journey is usable. Repeat affected checks after environment changes or
surprising failures, not before every click. Preserve signed-in profiles.

Identify relevant side effects from source and observation: a GET or a page open
may write activity. Use task-owned fixtures only under existing authorization;
track setup, mutations and cleanup. Do not weaken a journey because data is
missing. Avoid unknown writes to shared/customer systems.

## Reuse the project's verification recipe

Look for the repo's existing verification skill, feature map or documented run
recipe before reconstructing setup. Read only the journey relevant to the change.
Use its real launch/readiness command, safe auth setup, representative data,
normal entry points, expected results and cleanup instructions. Confirm current
state rather than trusting a remembered port or login. Never store credentials
in a recipe or task record.

When an authorized task proves a previously undocumented journey, preserve a
short reusable recipe in the existing task notes or an ignored task location.
Record the actual commands, readiness signal, safe data prerequisites, side
effects, proof and owned-resource cleanup that worked. Label unexecuted steps
unverified. Follow any separately owned feature-map system; do not silently
replace it, create a new framework or edit tracked repo guidance outside scope.
For a later task, reuse the recipe after checking its relevant inputs; do not
require the user to explain setup again. A substantial new verifier still needs
the self-check below before broad reliance.

## Evidence and reuse
For each material check record: operation/criterion, status, tested revision or
working diff, build identity if available, environment, relevant data/cache/tool
conditions, command or user steps, observed result and evidence pointer. Unknown
identity remains unknown. These can be a few lines, not a mandatory JSON schema.
When code, build, data or environment changes, rerun dependent checks; unchanged
commits or irrelevant documentation do not automatically invalidate every result.
A patch fingerprint alone cannot establish unchanged dependency/base behavior.
Never infer runtime success from an old screenshot, compiler output or self-report.

## Maintenance and checker reliability
Use the project's existing verification skill or recipe; do not invent or
replace Nassim's separately owned feature-map system. When maintaining an
existing authorized recipe, distinguish doc drift, harness gap and product
regression. Fix only owned material; preserve expected behavior and rerun the
changed recipe. Report product regressions separately rather than editing the
expectations to hide them. Maintain affected material when touched; no automatic
schedule is installed by these instructions.
Before relying on a newly created or substantially revised verifier, use
`evaluate-agent-skills`: execute launch/readiness/drive/evidence/cleanup, confirm
evidence survives, and challenge a critical assertion with a known-bad case in
isolated task-owned state. An unexecuted recipe is a draft. Never seed a defect
or bad data into shared/customer systems.

## Receipt and resume
Use the global short receipt. Include scope of cleanup and affected rechecks.
For incomplete or multi-session work, keep accepted/excluded scope, decisions
with reasons, current files/revision, valid versus stale checks, resource owners,
remaining blockers and the exact next action. Verify inherited claims against
current source/state before resuming; do not restart completed discovery.
