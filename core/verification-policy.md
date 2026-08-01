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

## Select test level

Use the lowest stable level that can prove the business claim:

- **Unit:** deterministic calculation, validation, formatting, or state rules.
- **Component:** form interaction, error display, submitted payload, or a key UI
  state transition.
- **Integration:** API contracts, persistence, authorization, transactions,
  idempotency, or rollback at the real local boundary.
- **End-to-end or smoke:** a small number of critical journeys through real pages,
  real APIs, and isolated data.

Do not add tests for static copy, framework plumbing, private implementation,
call counts without business meaning, or a path already covered completely at a
more stable level. Coverage percentage alone is not a product claim.

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
  and state. Scope strict fidelity to the declared surfaces. For a large page
  family, include its entry or home surface, at least one list or detail surface,
  and a critical error, empty, or loading state when applicable, plus any
  materially different layouts, platforms, and critical journeys. Compare each
  selected surface with its current approved source at the same viewport and
  state. Do not infer family-wide visual completion from build success or an
  unpaired screenshot.

An overlay does not lower risk intensity. A production admin screen can require
both high-risk verification and visual-fidelity evidence.

## Select verification scope

- **Focused gate:** while building a page or delivery unit, run the narrowest
  check that can falsify its active acceptance claims.
- **Affected gate:** when shared logic, contracts, dependencies, or recurrent
  defects change, reconcile affected consumers across runtime code, tests,
  fixtures, configuration, and maintained documents, then run their regression
  checks plus the relevant type, syntax, or contract check.
- **Journey gate:** when the pages and boundaries for a critical journey are
  connected, exercise that journey end to end and inspect its resulting state.
- **Release gate:** only when release readiness is claimed, run the repository's
  release checks and inspect the built artifact or external environment. A zero
  exit status is insufficient when the output contains warnings relevant to the
  claimed platform or surface; each warning needs a fix or an explicit supported
  acceptance verdict.

Do not run a full suite for every page edit. A focused page check can establish
Slice done, but isolated page checks cannot establish Journey done or Product
ready. Use the Product Plan to name critical journeys and project gates; use the
current Development Guide to map page acceptance claims to focused evidence.

At the Product-ready boundary, run all applicable repository-defined Affected,
Journey, and Release gates once, then perform the bounded closure sweep defined
by Product Build. Existing green unit, type, lint, or build checks cannot replace
a failing or stale end-to-end consumer. Product ready requires every relevant
failure and warning to be resolved or explicitly shown not to invalidate the
claim.

For an in-scope visible page, use its Page Functional Model to verify actor and
goal, entry and exit, each material state transition, real data and side effects,
success readback or consistency, and reachable failure boundaries. Inspect the
real rendered result at its representative viewport. When Visual parity is
claimed, pair that render with the current approved source at the same state.
Source code, a unit test, a successful mock, or a single unpaired screenshot can
support a narrower claim but cannot independently prove page completion, Visual
parity, or Product ready. Visible `undefined`, indefinite loading, materially
blank core content, or missing required information blocks Product ready even
when an error branch exists in code. Fix it or report Hold with the failed claim
and observed state.

## Verification cadence

Batch related implementation work until a coherent checkpoint. Do not run a
compiler, build, browser suite, or broad test suite after every edit or completed
component.

During implementation, run an early check only when it can cheaply prevent
material rework, confirm an uncertain contract, reproduce a defect, or protect a
high-risk boundary. Otherwise keep the active loop focused on implementation.

Run the Focused gate when the active slice becomes coherent. Rerun it only after
a relevant code change or failed result. Run Affected, Journey, and Release gates
when their corresponding boundaries are reached, not as repeated background
rituals.

For a visible Journey, the first target-runtime observation is part of slice
development rather than a final-project ceremony. As soon as an active page or
state is coherent, inspect the reachable normal, loading, empty, error, and
permission states needed by the Journey at its representative viewport. Use a
focused runtime check, not a full suite, and repair decisive failure before
expanding unrelated surfaces.

Optimize for total delivery time rather than test frequency. Deferring broad
verification does not authorize an unsupported completion claim.

## Test usefulness

Prefer observable state changes, payloads, persisted results, rendered outcomes,
and user-visible recovery. Avoid private-method assertions, call counts without
business meaning, static copy checks, framework plumbing, and duplicate coverage.

An active quality overlay selects the smallest check that can falsify its claim.
It does not require a full accessibility, performance, security, operability, or
compatibility suite when that boundary is outside the active scope.

For a bulk translation, rename, codemod, or migration, combine structural checks
with semantic acceptance: inspect representative samples across distinct source
patterns, exercise an affected real flow where meaning controls behavior, and
search for residual old, mixed, or malformed forms. A regex match, format check,
or presence of target-language characters proves structure only.

## Evidence rule

Never claim a check passed unless it ran in the current work and its output was
inspected. A partial check supports only the claim it actually tested.

## Completion levels

- **Scaffolded:** routes, pages, visual structure, controls, components, types,
  API shapes, fixtures, mocks, or tests exist, but the Page Functional Model is
  incomplete or no broader real-behavior claim has been proved.
- **Slice done:** one coherent unit produces its claimed observable result with
  a resolved Functional Model and fresh evidence at the required local or real
  boundary.
- **Journey done:** the complete in-scope user journey works through real pages,
  data, permissions, actions, resulting state, and readback at its required
  runtime boundaries.
- **Product ready:** agreed product scope, critical journeys, permissions, data,
  operating conditions, and requested release boundary are evidenced.

State the achieved level and material gaps. Page existence, typed APIs, source
code, unit tests, fixtures, or mocks can support Scaffolded or a narrow Slice
claim; accumulating them does not promote work to Journey done or Product ready
without fresh evidence at those higher boundaries.
