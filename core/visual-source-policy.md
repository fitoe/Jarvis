# Visual Source Policy

Use a visual source when UI quality or project style materially affects the
active slice. The approved source governs Visual Truth only; Product Truth still
governs functions, data, states, and authority.

## Choose the source path

- Existing approved mock, Figma node, or screenshot: use it as source of truth.
- Existing product with a mature nearby pattern: reuse its components, tokens,
  and interaction language.
- New or materially different visual surface: define the page job, real content,
  actions, reachable states, platform, and viewport; then generate GPT Image 2
  directions before coding.
- Small convention-based UI edit: follow the existing system directly. Do not
  generate a new mock solely to satisfy process.

Generated images may propose composition and art direction. They must not create
product scope. Ignore controls, claims, data, or states that are absent from the
approved product behavior.

## Preserve one project design language

Approve one visual baseline early enough to guide implementation. Persist the
selected source because code and later Image 2 prompts consume it. Keep a compact
Visual Source Record with:

- source paths and target viewport;
- page type, hierarchy, density, and key states;
- typography, color, spacing, radius, elevation, icon, and imagery language;
- project components and tokens to reuse;
- must-preserve details and must-not-invent boundaries.

For later surfaces, inspect whether the generation provider accepts image
references. Attach the baseline and closest approved screen when it does.
Otherwise supply the Visual Source Record and exact reuse constraints, then rely
more heavily on approved tokens and components. Text-only prompting is degraded
style evidence and cannot alone support a project-wide consistency claim. A new
direction is warranted only when the product intentionally changes its visual
language.

## Generate usable references

When direction is unresolved, generate two or three meaningfully different
directions and select one. Once selected, generate readable references at the
claimed viewport or by meaningful section; avoid one compressed board whose text
and spacing cannot be inspected. Regenerate unclear sections instead of guessing.

One desktop reference does not define mobile behavior. When a breakpoint changes
the composition materially, generate or approve that viewport separately;
otherwise follow the existing responsive system and do not claim visual parity
for an unreferenced viewport.

Use the user's configured GPT Image 2 path when available. Keep selected images
in a durable project location; drafts can remain disposable.

## Translate and compare

When the Product Design plugin is available, use its
`Product Design:image-to-code` workflow as the preferred translation and
visual-QA provider. Jarvis retains goal, product truth, budget, implementation,
and completion ownership. The plugin replaces a separate `design-to-code`
workflow; it does not replace this policy or Image 2 generation.

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
