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

A successful build does not erase its warnings. Warning evidence must retain the
issuing command, target platform or surface, warning identity, disposition, and
impact. A warning is accepted only when current evidence shows why it does not
invalidate the claim; unexplained or ignored warnings leave Quality or Release
claims unverified.

Evidence for a cross-cutting migration must cover the bounded consumer search,
not only the implementation that introduced the new contract. A stale route in
an end-to-end test, fixture, configuration file, or maintained document means
Affected evidence is incomplete even when unit tests and builds pass. For bulk
semantic changes, retain representative inspected samples and residual searches;
structural presence alone cannot prove meaning.

For a large page family, visual evidence may support only the selected page
families, layouts, states, platforms, and critical journeys that the approved
sources and same-viewport comparisons represent. Record why the selected pages
represent their family. Without an approved source and paired comparison, report
visual status as unverified rather than extrapolating from functional or build
evidence.

External design references require freshness checks. For Figma, retain the file
and node identity and the latest successful resolution at implementation start
and final acceptance. A missing, moved, or replaced node makes cached context,
screenshots, and comparisons tied to that node stale until the current approved
node is resolved and the owning mapping is updated.

When it has a durable consumer, page acceptance evidence should preserve the
active Page Functional Model: actor and goal, Journey position and entry or exit,
material state transitions, real data owners, actions and side effects, success
readback or consistency, failure boundaries, current design entry, code route,
platform, and representative viewport. Functional acceptance must observe the
intended state with its real data boundary; visual acceptance must pair the
rendered state with its current approved source. An unpaired screenshot or proof
that an error branch exists cannot establish that the live page is usable.

Delivery progress requires improved user-visible behavior or new evidence at a
real business boundary. A page shell, typed API, source file, unit test, mock,
document, rule, or evaluation fixture is evidence only for its narrow claim; its
existence or count is not evidence that a Journey or product advanced. When two
successive loops produce only process assets, or the active time budget is more
than half consumed by them, treat that pattern as evidence to reframe toward the
highest-value unresolved product claim.

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
