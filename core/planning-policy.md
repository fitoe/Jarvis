# Planning Policy

Plan only enough to remove the largest delivery risk and make the next action
executable.

## Two planning horizons

Keep a coarse product map containing outcomes, dependencies, and major risks.
Expand only the active vertical slice into file- or boundary-level steps.

Each active slice states:

- observable result;
- in-scope and out-of-scope behavior;
- relevant local patterns and dependencies;
- material assumptions and decisions;
- ordered implementation steps;
- verification for each product claim;
- replanning triggers.

## Step quality

A useful step produces an observable change and names its proof. Avoid steps such
as "finish backend", "add error handling", or "write tests" without a boundary
or expected behavior.

Prefer this shape:

```text
Add order creation through the existing order service.
Files: order schema, service, route, integration test.
Proof: authorized request persists one order and returns its identifier.
```

## Progressive detail

Do not choose future helper names, component splits, or internal algorithms before
their slice starts. Do decide shared contracts, hard-to-reverse dependencies, and
security boundaries before dependent work spreads.

## Parallel work

Parallelize only independent slices with clear ownership and integration points.
Do not delegate by default; coordination cost must be lower than expected time or
context savings. Follow [Delegation Policy](delegation-policy.md) for task
packets, write isolation, handback, integration, and acceptance.

## Artifacts

Create an artifact when it has a named consumer. Examples:

- a visual source used by implementation;
- an API contract shared by separate clients and services;
- a migration plan used for an irreversible data change;
- a release checklist used by an actual release.

Otherwise keep the decision in the active slice or source code.
