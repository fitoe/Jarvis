# Visual Source Policy

Use an approved visual source before implementing a new page-level UI, a key new
visual state, or a material visual redesign. The approved source governs Visual
Truth only; Product Truth still governs functions, data, states, and authority.
Figma may define visual composition, content hierarchy, and interaction it
explicitly expresses. It cannot establish API behavior, permissions, state
meaning, idempotency, side effects, or the source of real data. Resolve those
facts from product truth, code, and current contracts rather than guessing from
the design.

## Choose the source path

- New visual design generation: use the user's configured GPT Image 2 provider.
  Do not route generation to Figma, another design canvas, or another image model
  unless the user explicitly overrides the provider.
- Existing approved mock, Figma node, or screenshot supplied or explicitly
  selected by the user: use it as source of truth. Reading an existing Figma
  source does not authorize creating or redesigning in Figma.
- Existing product with a mature nearby pattern: reuse its components, tokens,
  and interaction language.
- New page-level UI, key visual state, or materially different surface: define
  the page job, real content, actions, reachable states, platform, and viewport;
  then generate GPT Image 2 designs before coding.
- Small convention-based UI edit: follow the existing system directly. Do not
  generate a new mock solely to satisfy process.

Copy changes, narrow color or spacing corrections, visual-neutral bug fixes, and
mechanical composition of already approved components may bypass generation.
When uncertain whether a change establishes new visual language, treat it as a
new surface.

Generated images may propose composition and art direction. They must not create
product scope. Ignore controls, claims, data, or states that are absent from the
approved product behavior.

## Mature the design source before approval

GPT Image 2 produces a visual proposal, not validated UX. Before generation,
hold enough active product truth to name:

- the target user, page job, journey position, entry, and exit;
- primary and secondary actions, their priority, and completion result;
- representative real content, expected density, and data relationships;
- reachable loading, empty, error, success, permission, and completed states;
- platform, target viewport, responsive unknowns, and existing components;
- reference-image roles, desired product identity, and explicit visual
  anti-patterns.

If a missing answer would create a materially different product or expensive
rework, resolve it or run a reversible product probe before high-fidelity
generation. Do not ask Image 2 to invent product behavior and visual language in
the same unsupported step.

Judge each generated direction in dependency order:

1. **Correct behavior:** approved jobs, actions, content, authority, and states
   are present without invented product scope.
2. **Task clarity:** purpose, hierarchy, primary action, status, and next step are
   immediately understandable.
3. **Journey efficiency:** the key task avoids competing actions, unnecessary
   navigation, and avoidable cognitive load.
4. **System consistency:** grid, density, typography, spacing, components, and
   interaction language form one reusable system.
5. **Product distinctiveness:** domain and brand identity replace generic cards,
   decorative dashboards, arbitrary gradients, and interchangeable AI styling.
6. **Polish:** alignment, contrast, iconography, imagery, rhythm, and detail are
   production-grade.

Do not spend another round polishing a lower item while an earlier item fails.
Visual beauty cannot rescue incorrect UX.

### Classify the largest blocking mismatch

After each output, compare it with Product Truth, the active visual input, and
approved references. Name the largest blocker and choose the smallest repair
that can test the diagnosis:

- wrong job, flow, action, content, or state: return to product and UX framing;
- weak information hierarchy or composition: regenerate that page or semantic
  section with corrected structure;
- generic or incoherent visual language: keep behavior fixed and explore a
  reference-driven direction with explicit identity and anti-pattern constraints;
- local spacing, contrast, copy, or asset defect: make a single targeted edit to
  the current output and repeat all must-preserve invariants;
- uninspectable detail, feasibility, or responsive uncertainty: add the missing
  implementation constraint or generate only the required detail or viewport.

Generate divergent directions only while the direction-level uncertainty is
still active. Once a baseline is approved, prefer constrained edits and variants
over restarting art direction. For a new baseline or material redesign, use an
independent product or visual critique when it can reveal a costly error; the
critic identifies a blocker and evidence, while Jarvis retains approval.

Approve a baseline only when it is implementation-ready: the core task and key
states are clear, representative content has credible density, key journey
screens share one visual system, product identity is visible, and the target
viewport is inspectable enough to derive components and constraints. An image
alone still cannot prove functionality, accessibility, or responsive behavior.

## Preserve one project design language

For a new project or page family, require human approval of one visual baseline
before UI implementation starts. This is one direction decision, not approval of
every later screen. Later screens may proceed automatically while they preserve
the baseline; ask again only when they materially change the visual language or
the approved source is too ambiguous to implement safely.

Persist the selected source because code and later Image 2 prompts consume it.
After approval, extract only implementation constraints a downstream builder or
verifier will consume. Keep project-wide visual language and the approved source
in the Product Plan; keep current-surface constraints in its Page Overview when
one exists, otherwise in the Development Guide:

- source paths and target viewport;
- page type, hierarchy, density, and key states;
- typography, color, spacing, radius, elevation, icon, and imagery language;
- project components and tokens to reuse;
- must-preserve details and must-not-invent boundaries.

For later surfaces, inspect whether the generation provider accepts image
references. Attach the baseline and closest approved screen when it does.
Otherwise supply the approved source location, current Development Guide, and
exact reuse constraints, then rely more heavily on approved tokens and
components. Text-only prompting is degraded
style evidence and cannot alone support a project-wide consistency claim. A new
direction is warranted only when the product intentionally changes its visual
language.

## Generate usable references

Generate related pages together on one Image 2 design board when this improves
speed, token use, cross-page comparison, or style consistency. The board may be
the approved Visual Baseline and global overview. It must show enough real
content and page identity for a human to judge direction; it need not make every
implementation measurement readable.

Generate multiple directions only when direction is unresolved or the human asks
for alternatives. After approval, crop readable pages or semantic sections from
the board for implementation. Generate a higher-resolution page or detail only
when the approved board cannot support reliable extraction; preserve the board's
composition, content, and style unless the replacement is explicitly approved.

One desktop reference does not define mobile behavior. When a breakpoint changes
the composition materially, generate or approve that viewport separately;
otherwise follow the existing responsive system and do not claim visual parity
for an unreferenced viewport.

Use the user's configured GPT Image 2 path when available. Keep selected images
in a durable project location; drafts can remain disposable.

Figma is an import and inspection provider only when an existing Figma source is
in scope. `Product Design:image-to-code` remains an implementation and visual-QA
provider. Neither may replace Image 2 as the new-design generator without an
explicit user instruction.

## Decompose only when the source is hard to inspect

Activate complex visual decomposition only when the source's length, density, or
cross-section relationships make reliable one-pass implementation or comparison
unlikely. Decide from inspectability and fidelity risk, not an arbitrary pixel
height or section count. Keep ordinary pages and small edits on the normal path.

When decomposition is active, retain the approved full-page source as global
Visual Truth and create a compact Visual Map only when implementation or QA will
consume it. Capture:

- semantic section order, bounds, approximate height, and density;
- shared grid, shell, tokens, components, assets, and responsive rules;
- cross-section rhythm, overlaps, transitions, and alignment constraints;
- for each section, its source, adjacent boundary context, states, and integration
  boundary.

Split by product and layout meaning, not fixed rectangles. If the design is still
being generated, approve one full-page overview plus readable section references
and detail views as needed. If a long source is already approved, crops from that
source retain authority; newly generated close-ups are supplementary and cannot
silently replace its composition, content, or boundaries.

For a complex approved Figma page, first read enough page-level context to retain
the global hierarchy, grid, shared components, and section relationships. Then
request implementation context section by section when one full-node response
would be too large to inspect reliably. Each bounded read must include the owned
section plus the adjacent boundary and shared style information needed for
integration. Do not compress the entire page into a shallow summary merely to fit
one context window, and do not let partial Figma reads redefine the approved
full-page source.

Build the shared shell and visual primitives first, then implement and assemble
sections continuously. Compare each section with its source and compare the
assembled page with the full-page source at the same viewport and state. Section
parity does not prove full-page rhythm, continuity, or final visual acceptance.

## Translate and compare

For a Figma source, resolve the referenced file and node through the authorized
provider when implementation starts and resolve them again immediately before
final visual acceptance. Node identifiers are external references, not permanent
truth. If a node was removed, moved, or replaced, locate the current approved
node, update the existing Product Plan, Development Guide, or delivery note that
owns the mapping, and mark evidence tied to the old node stale. Stop requesting
or citing the invalid node; do not compare implementation against cached output
from an unresolved reference.

When the Product Design plugin is available, use
`Product Design:image-to-code` as the preferred translation workflow for an
approved Figma node, screenshot, mockup, or image reference. For Figma, use the
authorized Figma provider to read implementation context and assets and capture
the approved visual target; use a supplied image directly. Then run
`Product Design:design-qa` with the source and rendered implementation together
at the same viewport and state. A saved screenshot alone is not comparison.

For a large page family, choose a bounded representative set that includes its
entry or home surface, at least one list or detail surface, and a critical error,
empty, or loading state when those categories exist. Include additional samples
only when materially different layouts, platforms, or critical journeys would
otherwise be unrepresented. Each sample needs its own current approved source
and same-viewport, same-state comparison. Passing samples support only the page
family characteristics they actually represent, not every page in the product.

Jarvis retains goal, product truth, budget, implementation, and completion
ownership. The plugin replaces a separate `design-to-code` workflow; it does not
replace this policy, local component reuse, or Image 2 generation.

Follow [Capability Provider Policy](provider-policy.md). Apply the configured
Image 2 provider and Jarvis repair budget; do not import another workflow's
artifact set into Jarvis unless a downstream consumer needs it.

If the plugin is unavailable, perform the same minimum loop directly:

1. Extract layout, typography, color, components, assets, content, and states.
2. Implement with existing project primitives where they match.
3. Capture the same viewport and state as the source.
4. Compare source and implementation together; fix the largest visible gaps.

Use the normal repair budget. Fidelity does not justify an unbounded loop. Report
remaining mismatches and distinguish visual parity from functional, responsive,
and accessibility claims.
