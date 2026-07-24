# Product Design Capability

Use this capability to resolve product uncertainty for the active slice. It is
not a mandatory phase.

## Find the smallest unresolved decision

Inspect the goal, existing product, feedback, approved sources, nearby flows, and
platform constraints. Identify only questions whose answers change:

- target user or job;
- scope and priority;
- user journey or navigation;
- page anatomy or interaction state;
- content hierarchy;
- visual direction or fidelity source.

Ask when alternatives create meaningfully different products or expensive
rework. Otherwise choose a reversible default and record it.

## Produce the lightest useful evidence

- Clear local behavior: record one decision in the Slice Packet.
- Multi-step journey: capture flow and reachable states.
- New page family: capture page inventory and generate related pages together on
  an Image 2 design board when useful.
- Fidelity-sensitive UI: persist the approved source and implementation-relevant
  hierarchy, measurements, assets, states, and must-preserve details.

Do not generate a design specification, token file, matrix, manifest, freeze
record, and debt ledger together without named consumers.

## Establish visual direction

Follow [Visual Source Policy](../core/visual-source-policy.md) when UI quality or
style affects the slice. For a new or materially different surface, settle the
page job, real content, actions, states, platform, and viewport before asking GPT
Image 2 for visual directions. Generated controls or features do not become
product requirements.

Require human approval and persist one baseline for the project before UI
implementation. Later prompts and screens must reuse its visual language and the
closest existing components or tokens without repeated approval unless direction
changes. A small edit inside an established system does not need a fresh mock.

## Validate product value when uncertainty is high

For a new or weakly evidenced product direction, follow
[Product Validation](../core/product-validation.md). Prefer an early demo,
prototype, interview, or measurable user signal over polishing an untested idea.

Return the decision, evidence, affected flow, source status, material constraints,
and any unresolved high-cost question. Continue into solution or build work in the
same Jarvis context.
