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

## Use the visible-first build path

Activate this path when early walkthrough feedback is valuable, UI and flow
uncertainty dominates, the page map is known, consumer-facing contracts are
stable enough to mock, and no high-risk real boundary controls the direction.

1. Build the shell, routes, navigation, shared layout, and reusable visual
   primitives.
2. Make the in-scope page family browsable with realistic content and reachable
   loading, empty, error, success, permission, and disabled states.
3. Keep visible controls interactive through isolated fixtures or a mock adapter
   behind the same consumer-facing boundary intended for the real implementation.
4. Connect the backend by critical journey, replace mocks one seam at a time,
   and verify persistence, permissions, side effects, and integration at their
   real boundaries.

Name provisional API, data, and permission contracts before broad page work. If
conflicting local evidence or an unknown shared contract could invalidate many
screens, run the cheapest focused probe first, then return to visible work. Do
not complete every invisible service merely because one contract needed proof.

Do not claim persistence, authorization, or integration from a visible mock.
Mark unconnected behavior honestly outside product UI. When authentication,
billing, inventory, migration, destructive data, or an external API can change
the page model, probe that boundary before broad UI implementation.

## Keep development scaffolding out of product UI

Build user-visible surfaces as the intended final product, not as an
implementation-status board.

- Use production-intent labels, realistic content, and product-defined loading,
  empty, error, success, permission, and disabled states. Do not render `TODO`,
  `not implemented`, `API unavailable`, `mock`, `test`, debug badges, or
  developer notes as product copy.
- Headings and supporting copy must help the user decide or act, understand a
  material condition, or recover from a real state. Remove subtitles that merely
  restate the page title or explain an obvious function.
- Keep development status in code, fixture configuration, logs, tests, or
  handoff. It must not occupy user-facing chrome.
- Mock-backed controls may exercise the intended local interaction with final
  copy, but must not fake persisted success or real integration. Report missing
  proof outside the UI instead of adding placeholder text.

## Reuse the local component library

Existing finished components preserve consistency and avoid rebuilding behavior
the project already owns. Prefer, in order: a nearby page pattern, a finished
component and its supported variants, composition of existing components, a
shared-library extension with real reuse, then a new local component.

- When a finished component already provides the required behavior, reuse it
  even if its appearance differs. Adapt through supported public props, variants,
  tokens, slots, class names, theme APIs, or scoped styles.
- Preserve its state, focus, keyboard, accessibility, validation, and event
  mechanisms instead of copying source or rebuilding actions.
- Compose existing components before adding wrappers, forks, or parallel local
  versions. Keep page-specific styling and business logic local; do not change
  shared defaults for one page.
- Extend a shared component only when required behavior is genuinely missing and
  multiple consumers benefit; otherwise keep the smallest adaptation local.
- Fork or reimplement only when public extension points cannot satisfy approved
  Product Truth or Visual Truth; implement only the missing piece.
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
