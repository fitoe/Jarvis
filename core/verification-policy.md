# Verification Policy

Verification protects product claims, not implementation rituals.

## Build a claim-evidence map

Use five claim types when the distinction affects completion:

- **Product:** the slice solves the intended user problem or reduces the named
  product uncertainty.
- **Functional:** behavior, state, data, and recovery work at the claimed
  boundary.
- **Visual:** the named viewport and state match an approved source within the
  declared fidelity target.
- **Quality:** affected code satisfies relevant maintainability, type, security,
  and regression expectations.
- **Release:** the agreed artifact or environment is usable at the real release
  boundary.

Do not require every type for every slice. Do not use evidence from one type to
claim another.

For every completion claim, identify the nearest check that could prove it false:

| Claim | Closest useful evidence |
|---|---|
| deterministic rule returns the right result | unit test |
| API validates and persists data | integration test plus stored result |
| user can complete a form | focused browser flow and resulting state |
| authorization blocks another user | request under both identities and unchanged data |
| page matches an approved source | same-viewport screenshot comparison |
| release is usable | repository release gate plus external state check |

## Select intensity

### Routine

Local, reversible, narrow behavior. Run one focused check or inspect the real
affected flow.

### Shared

Reusable logic, contracts, request layers, dependencies, or recurrent defects.
Add a regression check when it can catch recurrence, then run affected tests and
the relevant type, syntax, or contract check.

### High-risk

Authentication, authorization, money, inventory, migrations, production data,
deployment, publishing, or destructive actions. Verify authority, use isolated
data, exercise the closest integration boundary, and run the repository's release
gate when the completion claim includes release readiness.

Add independent overlays when needed:

- **Product-uncertain:** seek the cheapest user or market signal that can
  challenge the value hypothesis before broad investment.
- **Visual-fidelity:** establish an approved source and compare the same viewport
  and state. Scope strict fidelity to the declared surfaces.

An overlay does not lower risk intensity. A production admin screen can require
both high-risk verification and visual-fidelity evidence.

## Test usefulness

Prefer observable state changes, payloads, persisted results, rendered outcomes,
and user-visible recovery. Avoid private-method assertions, call counts without
business meaning, static copy checks, framework plumbing, and duplicate coverage.

## Evidence rule

Never claim a check passed unless it ran in the current work and its output was
inspected. A partial check supports only the claim it actually tested.

## Completion levels

- **Slice done:** current slice claims have fresh evidence.
- **Journey done:** the complete in-scope user journey works across its boundaries.
- **Product ready:** agreed product scope, critical journeys, permissions, data,
  operating conditions, and requested release boundary are evidenced.

State the achieved level and material gaps. Passing a slice check does not imply
journey completion or release readiness.
