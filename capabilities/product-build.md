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

## Model page function and acceptance before coding

Before coding an active page or page family, form one lightweight Page Functional
Model from Product Truth, current code, and real API or data contracts. Keep it in
active context by default. Persist it only in an existing Development Guide or
Page Overview when a cross-session handoff, multiple workers or reviewers, a
complex state machine, or a later slice is a real consumer. Do not create a new
document or second acceptance matrix for it.

For each representative surface, resolve:

- actor or role and the user's goal;
- Journey position, entry conditions, and exit result;
- real data sources and their fact owners, distinguishing integration from mocks;
- core actions, authority, and side effects;
- each material precondition -> action -> target-state transition;
- successful server readback, navigation, or multi-party consistency;
- loading, empty, error, permission, disabled, and completed boundaries;
- current valid Figma node or visual source, code route, platform, and acceptance
  viewport.

Figma does not complete this model. If actor, core action, state transition, or
success result is materially ambiguous, inspect current product truth, code, and
API contracts first. If the ambiguity remains and guessing could cause rework,
ask the smallest blocking question or report Hold. Decide ordinary reversible
presentation details autonomously.

Refresh the model before implementation and final acceptance. Observe the real
rendered surface as well as its source and tests. Visible `undefined`, an
unbounded loading state, a materially blank core region, or missing required
content is a failed page state even when source code contains an error branch or
mock tests pass. Fix the state or report the page as Hold in the ordinary handoff;
do not create another status system or claim Product ready.

Run this target-runtime observation as soon as the active page or state is
coherent, before implementing an unrelated page. Exercise the reachable normal,
loading, empty, error, and permission states needed by the active Journey; do not
defer obvious runtime failure to project-wide acceptance.

## Deliver one real Journey at a time

Default to the highest-value unclosed Journey. Move it vertically through:

1. current approved product and visual truth;
2. the required pages, routes, content, and reachable states;
3. real data, permissions, and side effects rather than fixture-only success;
4. the cross-page action, resulting state, and readback;
5. target-runtime checks and same-viewport visual comparison when claimed;
6. accepted Journey evidence or an explicit Hold.

Do not expand a secondary page family while a higher-value core Journey remains
broken. A high-risk contract probe may precede the Journey when it controls the
safe implementation path, but return to the Journey as soon as the boundary is
settled.

## Reconcile cross-cutting changes

When a route scheme, name, platform convention, shared contract, or other rule
changes across an active product, identify its bounded consumer set before
claiming the migration complete. Search runtime code, unit and end-to-end tests,
fixtures and mocks, configuration, generated inputs, and maintained documents
that encode the changed truth. Update each in-scope consumer and run the affected
and journey checks that own the shared behavior; a green compiler, unit suite, or
build alone does not prove consumer reconciliation.

When a new cross-cutting rule is adopted after implementation has started, scan
the current in-scope surface once. Fix violations that fall inside the completion
claim. Record known out-of-scope debt in the ordinary handoff or existing project
truth and narrow the claim; do not create a new registry. Known in-scope
violations block Product ready.

For translation, bulk renaming, codemods, and other mechanical transformations,
inspect representative samples across distinct variants and search for residual
old forms, mixed terminology, and malformed meaning. Structural checks such as
matching a regex, compiling, or containing target-language characters cannot
establish semantic quality by themselves.

## Use the visible-first build path

Activate this path when early walkthrough feedback is valuable, UI and flow
uncertainty dominates, the page map is known, consumer-facing contracts are
stable enough to mock, and no high-risk real boundary controls the direction.

1. Build the shell, routes, navigation, shared layout, and reusable visual
   primitives needed to expose the product shape.
2. Make the known page map browsable only deeply enough for early flow and
   information-architecture feedback. Use realistic content and the same
   consumer-facing seams intended for real implementation.
3. Once the shape is visible and the active contracts are stable, stop horizontal
   mock expansion. Select the highest-value unclosed Journey and connect its
   pages and states to real data, permissions, side effects, and readback.
4. Verify that Journey in the target runtime, replace its mocks one seam at a
   time, and finish or hold it before polishing secondary page families.

Name provisional API, data, and permission contracts before broad page work. If
conflicting local evidence or an unknown shared contract could invalidate many
screens, run the cheapest focused probe first, then return to visible work. Do
not complete every invisible service merely because one contract needed proof.

Do not claim persistence, authorization, or integration from a visible mock.
Mark unconnected behavior honestly outside product UI. When authentication,
billing, inventory, migration, destructive data, or an external API can change
the page model, probe that boundary before broad UI implementation.
Visible-first is a temporary discovery accelerator. Routes, pages, controls, and
fixtures that only demonstrate shape remain Scaffolded, not delivered product.

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

## Close Product-ready claims

Before claiming Product ready, run one bounded closure sweep over the agreed
scope. This is a final acceptance boundary, not a repeated per-edit ritual.

1. Run every repository-defined Affected, Journey, and Release gate that applies
   to the claim, including target-platform builds and their observable smoke
   checks. Inspect failures instead of substituting a green unit suite or build.
2. Search in-scope user-visible surfaces for development-status copy and
   redundant filler, then inspect representative matches in context. Reconcile
   fixed-destination navigation and platform-runtime rules the same way.
3. Inspect compiler, linter, bundler, framework, and target-platform warnings.
   Fix each warning or retain explicit evidence that names the warning, affected
   surface, impact, and why it is acceptable. An unexplained warning blocks
   Product ready even when the command exits successfully.
4. Reconcile active cross-cutting migrations and newly adopted rules against
   their current consumers. Stale tests, fixtures, routes, or documents are
   unresolved product work, not harmless test noise.
5. For a large page family, apply the representative visual evidence rules in
   Verification Policy. Report visual completion only for surfaces supported by
   approved-source comparison.

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

## Preserve link semantics for navigation

First identify the target runtime and follow its native navigation semantics.
When activating a visible element takes the user to a known addressable
destination, prefer the platform's declarative navigation component with a real
destination. Do not hide a known route behind a generic container, button, or
click handler that only calls an equivalent router API.

- On the web, use a native link or the framework's `Link` component for page,
  menu, breadcrumb, tab, card, list-row, and external-resource navigation when
  the destination is known before activation. Preserve browser behavior such as
  open in a new tab, copy link, focus, keyboard use, screen-reader semantics, URL
  inspection, and framework prefetching.
- In WeChat, Alipay, or another mini-program runtime, use its native declarative
  navigation component and platform router, lifecycle, storage, request, and UI
  APIs. Do not emit `<a>`, `window`, `document`, DOM APIs, `localStorage`, or other
  browser-only elements and globals unless the code is explicitly isolated to a
  supported web-view boundary.
- Use buttons for commands that act on the current context: submit, mutate,
  delete, toggle, open a dialog, start a process, or reveal local UI.
- Use programmatic navigation when it is genuinely conditional or follows a
  completed action, such as a successful create flow, authentication redirect,
  route guard, or history repair. A side effect followed by navigation remains
  an action; a fixed destination alone remains a link.
- Follow the repository router and component-library conventions. Styling a
  link like a button does not turn navigation into a button action.

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
