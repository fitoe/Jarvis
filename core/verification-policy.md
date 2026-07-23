# Verification Policy

Verification protects product claims, not implementation rituals.

## Build a claim-evidence map

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

## Test usefulness

Prefer observable state changes, payloads, persisted results, rendered outcomes,
and user-visible recovery. Avoid private-method assertions, call counts without
business meaning, static copy checks, framework plumbing, and duplicate coverage.

## Evidence rule

Never claim a check passed unless it ran in the current work and its output was
inspected. A partial check supports only the claim it actually tested.
