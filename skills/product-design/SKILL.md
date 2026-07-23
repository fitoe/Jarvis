---
name: product-design
description: Turn uncertain product goals into decision-ready user flows, page behavior, content structure, and visual direction. Use when product meaning, user journey, interaction, information architecture, or visual source is unclear enough to cause implementation rework. Produce only the design evidence the active slice needs.
---

# Product Design

Resolve product uncertainty for the active slice. Design is a capability, not a
mandatory stage before every implementation task.

## Inspect context

Read the product goal, active slice, existing UI, brand assets, user feedback,
nearby flows, and platform constraints. Reuse approved design and established
patterns before proposing a new direction.

## Identify the decision

Name the smallest unresolved question that blocks confident implementation:

- target user or job;
- scope and priority;
- user flow or navigation;
- page anatomy or interaction state;
- copy hierarchy;
- visual direction or approved source.

Ask only when alternatives create meaningfully different products or large
rework. Otherwise choose the strongest reversible default and record it.

## Produce the lightest useful output

- Clear local behavior: concise decision in the active slice.
- Multi-step user journey: flow and state notes.
- New page family: page inventory plus one representative direction.
- Fidelity-sensitive UI: persisted visual source plus implementation-relevant
  measurements and must-preserve rules.

Do not require a design specification, token file, page matrix, component matrix,
manifest, freeze record, and debt ledger together. Create an artifact only when
its named consumer needs it.

## Cover product states

For affected behavior, consider only relevant states: initial, loading, empty,
success, error, permission, offline, partial data, and recovery. Do not invent
states that the product cannot reach.

## Handoff readiness

Return:

- decision and evidence;
- affected user flow or page;
- approved or provisional source;
- important states and constraints;
- open high-cost question, if any;
- next recommended capability.

Route to `solution-design` when technical constraints can change the product.
Route to `product-build` when the active slice is clear enough to implement.
Approval is required only for direction with high rework cost, not for reversible
scaffolding or technical exploration.

Read [Decision Policy](../../core/decision-policy.md) for escalation and
[Planning Policy](../../core/planning-policy.md) for artifact discipline.
