# Pattern catalog

These are contextual review hypotheses, not automatic deletion rules. Names,
language choice, abstraction count, and coding style do not reveal authorship.
The evidence requirements in SKILL.md apply to every candidate.

## Structure and residual edits

| Candidate | Evidence to establish | Smallest useful action | Reasons to keep it |
| --- | --- | --- | --- |
| Duplicate policy or helper | An existing implementation has the same inputs, semantics, ownership, and intended evolution. | Reuse that implementation and remove the redundant copy. | Similar syntax across independent domains can be deliberate; forced unification can create coupling. |
| Pass-through layer | The layer adds no policy, boundary, stable interface, or useful explanation. Inspect consumers before inlining. | Call the existing dependency directly or simplify the layer. | Transaction, authorization, instrumentation, dependency injection, and compatibility boundaries can justify one caller or one implementation. |
| Speculative generality | Flags, factories, strategy variants, or configuration support no current requirement or contract. | Keep the required path and remove unused private machinery. | Supported public options, staged migrations, and documented extension contracts are real requirements. |
| Abandoned attempt | A debug path, helper, stub, or compatibility branch no longer contributes to the solution. Trace reachability and history when available. | Remove the residual edit and its task-owned unused wiring. | Registries, plugins, reflection, generated entry points, and external callers can make apparently unused code live. |
| Reinvented repository pattern | The change bypasses an established component or contract and adds equivalent infrastructure. | Adapt the existing mechanism. | A documented limitation or distinct requirement can justify a new implementation. |
| Difficult control flow | Nesting or intertwined responsibilities obscure a specific decision or duplicate a branch. | Use clear conditions or move logic to an existing owner. | Extraction is worthwhile only when it improves understanding; do not manufacture a helper per line. |

## Validation, errors, and state

| Candidate | Evidence to establish | Smallest useful action | Reasons to keep it |
| --- | --- | --- | --- |
| Redundant defensive code | An enforced invariant makes a branch unreachable on every relevant path. | Remove the branch; preserve the enforcing boundary. | Type annotations, assertions, and current fixtures alone cannot prove runtime input validity. Defense across independent trust boundaries can be necessary. |
| Fake success on failure | A catch returns an empty/default result for an error that the contract requires callers to see. | In repair mode, use the established error path and test it. In cleanup mode, report the behavior change first. | Optional enrichment, cache fallback, or best-effort work may legitimately degrade if the contract represents that outcome. |
| Empty error ceremony | A catch only rethrows the same error without cleanup, conversion, or context. | Remove the redundant catch while retaining the error and async contract. | Finally blocks, monitoring, framework interception, and error translation affect behavior. |
| Type suppression hiding a mismatch | A cast, unchecked value, lint suppression, or ignore directive conceals a demonstrated invalid assumption. | Correct the boundary or underlying type using the project's existing tools. | Narrow interop assertions and documented compiler limitations may justify an escape hatch. |
| Conflicting state ownership | Two stored values describe the same fact and can diverge on an actual update path. | Derive the value from its existing owner when semantics permit. | Snapshots, optimistic state, memoization, and temporal differences may require independent values. |

## Verification and explanatory noise

| Candidate | Evidence to establish | Smallest useful action | Reasons to keep it |
| --- | --- | --- | --- |
| Test that proves little | A test echoes the calculation, asserts only a mocked return, or bypasses the behavior it claims to cover. | Assert a known outcome through the relevant boundary; preserve intentional regression coverage. | Mocks can correctly isolate expensive boundaries; interaction tests can prove required side effects or ordering. |
| Misleading narration or debug residue | Comments restate syntax or describe behavior that no longer exists; logs are leftover diagnostics. | Remove narration, correct misleading text, or remove task-owned debug output. | Keep rationale, invariant explanations, licenses, directives, operational logs, and security audit evidence. |
| Unrelated patch growth | A changed hunk contributes neither to the requirement nor a necessary supporting change. | Leave unrelated existing work alone; narrow only the edits owned by this cleanup. | Migrations and mechanical changes can be necessary parts of an explicitly requested task. |

## Examples that require judgment

### Redundant wrapper versus a real boundary

```python
def _read_account(db, account_id):
    return db.accounts.get(account_id)
```

If this is private, has one ordinary caller, and owns no contract or meaningful
concept, a direct call may be clearer. This shape alone proves nothing. Keep a
similar wrapper that checks the tenant, applies authorization, or supplies a
stable adapter used by consumers.

### A catch can be removed; a fallback needs a contract decision

```python
def read_settings(client):
    try:
        return client.read_settings()
    except Exception:
        raise
```

Removing just this catch preserves error propagation. Conversely, replacing
`except Exception: return {}` with propagation changes what callers observe.
Do that only as an authorized defect repair with evidence for the intended
error contract. An empty successful result and a failed request are different.

### A type is not a runtime guarantee

```python
def send_email(address: str):
    if not isinstance(address, str):
        raise TypeError("address must be a string")
    return mailer.send(address)
```

The annotation does not make the guard redundant. Determine whether this is a
public boundary, what actual callers can pass, and where validation occurs.
Do not strip it simply because the annotation says `str`.

### Simplicity can require retaining code

Two short formulas owned by unrelated domains may be easier to maintain than
a shared helper with modes. An explicit branch may be clearer than a nested
conditional expression. A retry budget or resource cleanup can be necessary
despite increasing line count. Optimize comprehension and required behavior.
