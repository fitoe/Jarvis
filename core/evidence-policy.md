# Evidence Policy

Evidence supports a specific claim only while its relevant inputs remain valid.

Classify the claim as product, functional, visual, quality, or release. Evidence
for one type does not prove another: screenshots do not prove persistence, unit
tests do not prove visual fidelity, and mock behavior does not prove a real
integration.

For durable evidence, record:

- stable evidence and claim identifiers;
- kind of check;
- command or observation;
- result and environment;
- checked time;
- Git commit when code is involved;
- files or directories whose changes invalidate the evidence.

Comparative delivery claims need paired evidence. When claiming that an agent,
model, Skill, or workflow performs better than a baseline, run the same raw task
from the same repository state with the same model, budget, tools, and authority.
Compare observable outcome, human intervention, rework, elapsed time, quality,
visual drift when relevant, and unsafe or repeated side effects. Green repository
checks or one successful run cannot establish a comparative improvement.
When the claim spans product delivery generally, keep visual drift explicit for
UI work even if a particular nonvisual comparison records it as not applicable.

Mark evidence stale when a dependency changes after the recorded commit, the
environment no longer represents the claim, or external state cannot be confirmed.
Stale evidence remains useful history but cannot support completion.

```json
{
  "id": "E1",
  "claim_id": "C1",
  "claim_type": "functional",
  "kind": "test",
  "status": "fresh",
  "commit": "<git-commit>",
  "checked_at": "2026-07-24T00:00:00Z",
  "environment": "local-test",
  "command": "python -m unittest",
  "depends_on": ["src/orders.py", "tests/test_orders.py"],
  "result": "passed"
}
```

Run the bundled state tool from its resolved Jarvis skill path with `reconcile
project-state/current.json --repo . --write` to detect code-path invalidation.
External evidence still requires a fresh query at the real boundary.
