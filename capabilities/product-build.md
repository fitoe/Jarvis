# Product Build Capability

Turn the current page or coherent delivery unit into verified behavior across
frontend, backend, data, integrations, automation, or configuration.

## Before editing

1. Read repository instructions, inspect the worktree, and confirm the
   observable result and success claims.
2. Find the closest existing implementation. For UI work, inspect the local
   component library, design system, Storybook, tokens, and nearby page usage.
3. Name the smallest check that can falsify each claim. When a Development Guide
   exists or a downstream worker needs one, confirm it is context-closed.
   Otherwise keep the active claims in context and proceed.

Read [Code Quality Policy](../core/code-quality-policy.md) when ambiguity, shared
code, debugging, review, or refactoring makes its full guidance useful.

## Implement the smallest coherent change

- Follow the closest implementation and reuse existing components, services,
  types, and dependencies; touch only files required by the active result.
- Avoid speculative abstractions; remove only code this change makes unused.
- Keep mock behavior separate from real integration claims.
- Batch related edits to a coherent checkpoint. Avoid repeated compile-test loops
  before then; check early only to prevent material rework, confirm an uncertain
  contract, reproduce a defect, or protect a high-risk boundary.
- At the checkpoint, run the focused or affected check warranted by the claims.
  Read [Verification Policy](../core/verification-policy.md) when shared or
  high-risk boundaries, uncertain evidence depth, journey acceptance, or release
  makes broader guidance useful.

Load one [Feature Recipe](../recipes/README.md) only when the project lacks a
closer pattern.

## Reuse the local component library

Existing finished components preserve consistency and avoid rebuilding behavior
the project already owns. Prefer, in order: a nearby page pattern, a finished
component and its supported variants, composition of existing components, a
shared-library extension with real reuse, then a new local component.

- Reuse public component APIs, variants, tokens, accessibility, interaction
  states, and established usage patterns instead of copying component source.
- Compose existing components before adding wrappers, forks, or parallel local
  versions. Keep page-specific business logic outside the component library.
- Extend a shared component only when required behavior is genuinely missing and
  multiple consumers benefit; otherwise keep the smallest adaptation local.
- Do not force a component that cannot satisfy approved product behavior or the
  visual source. Record the gap and implement only the missing piece.
- Verify the assembled page, journey, and affected states. Do not duplicate tests
  for component-library internals already covered at their owning boundary.

## Visual implementation

Follow [Visual Source Policy](../core/visual-source-policy.md). When approved
visual evidence exists and fidelity is part of success, treat it as the visual
source of truth while product behavior remains authoritative. Preserve page type,
hierarchy, density, typography, color, assets, states, and action priority.

For an approved Figma node or image reference, use Visual Source Policy's
`Product Design:image-to-code` and `Product Design:design-qa` route when the
plugin is available, without transferring Jarvis ownership. Compare source and
implementation together and repair the largest visible gaps within budget.
Record simplifications instead of calling them parity. Do not require a generated
mock for a small edit that already has a clear project pattern.

When the source is too complex for reliable one-pass inspection, use the
conditional decomposition defined by Visual Source Policy. Implement semantic
sections against the shared visual language, assemble them continuously, and
require both section-level and full-page comparison before accepting parity.
For complex approved Figma pages, read implementation context in bounded semantic
sections rather than reducing an oversized node to a coarse one-pass summary.

Treat other skills, plugins, models, and services the same way. Follow
[Capability Provider Policy](../core/provider-policy.md); accept their bounded
output, then verify the active Jarvis claim.

## Adapt rather than patch blindly

Stop and replan when a material assumption fails, scope crosses a new boundary,
a closer project pattern invalidates the approach, the same failure survives two
repairs, or verification cannot prove the intended claim.

Return changed behavior, changed files, acceptance criteria covered, checks
actually run, document or code conflicts, stale or missing evidence, remaining
risk, and next action. Return `needs-context` instead of inventing shared
behavior, authority, or contracts.
