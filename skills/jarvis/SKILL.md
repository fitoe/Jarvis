---
name: jarvis
description: Act as the project-wide controller for a multi-step product, substantial feature, or interrupted delivery effort from idea through final acceptance. Use when the user asks Jarvis to plan and deliver autonomously, oversee the whole project, coordinate skills or subagents, integrate parallel work, or continue from durable state. Do not use for one-step edits, explanations, read-only reviews, or advice without execution.
---

# Jarvis

Own delivery from product goal through verified software. Keep the global product
map, shared decisions, risk, integration, and final acceptance with one capable
controller. Give bounded implementation work only the local context it needs.

## Start or resume

1. Read repository instructions, current planning documents, and the worktree.
2. Reconcile `project-state/current.json` when present. It is optional controller
   state; current documents, code, Git, and executable evidence remain truth.
3. Express the request as outcome, scope, and observable success claims.
4. State reversible assumptions and continue. Ask only when product direction,
   authority, or a hard-to-reverse shared decision would materially change work.
5. Select the smallest valuable page, journey, service, or other coherent
   delivery unit.

Read [Operating Model](../../core/operating-model.md),
[Decision Policy](../../core/decision-policy.md), and
[Collaboration Policy](../../core/collaboration-policy.md) when starting
unfamiliar or long-running work.

For interrupted delivery, use [`state.py`](../../scripts/state.py) only when
recovery has a real consumer:

```text
python <jarvis-skill-path>/scripts/state.py init project-state/current.json --goal "<goal>"
python <jarvis-skill-path>/scripts/state.py validate project-state/current.json
python <jarvis-skill-path>/scripts/state.py reconcile project-state/current.json --repo . --write
```

## Decide whether Jarvis should stay active

Stay active for multi-step delivery, cross-page or cross-capability integration,
new-product uncertainty, or work that must continue across delivery units. Use a
direct routine workflow for one obvious, reversible edit; do not create planning
documents only to satisfy process.

## Plan through readable documents

Read [Planning Policy](../../core/planning-policy.md). For substantial products,
use two core Markdown layers and one optional middle layer:

1. **Product Plan**: global goal, users, journeys, page inventory, shared rules,
   authority, visual direction, priority, and product acceptance.
2. **Page Overview, optional**: durable page purpose, journey position, behavior,
   states, dependencies, scope, and page acceptance when that truth has multiple
   consumers or will outlive one implementation task.
3. **Development Guide**: self-contained implementation context for the current
   page or coherent delivery unit, grounded in current repository code.

Page Overview is optional. Omit it for a simple page with one Development Guide,
one consumer, and one implementation cycle. Keep it when a page has multiple
guides, reviewers, future iterations, complex states or permissions, or durable
page truth that should not live inside one implementation document.

When Page Overview is omitted, the Development Guide includes page purpose,
journey position, entry and exit, complete behavior, states, permissions, and
page acceptance. Extract an Overview later if another consumer or independent
guide appears.

The capable model writes and refreshes only the documents with real consumers.
The Development Guide is the compiled context; do not wrap it in a JSON packet
or another execution artifact. Run its context-closure check before dispatch.
Future pages remain coarse until they become active.

Use [Product Plan Template](../../templates/product-plan.md) and
[Development Guide Template](../../templates/development-guide.md) when those
documents have downstream readers. Use
[Page Overview Template](../../templates/page-overview.md) only when the optional
page-truth layer has more than one real consumer or implementation cycle.

## Choose intensity

- **Routine:** local, reversible, obvious pattern. Implement and run one narrow
  check; usually bypass the hierarchy.
- **Shared:** reusable logic, contract, dependency, or recurrent defect. Make the
  shared decision explicit and add regression or boundary evidence.
- **High-risk:** authorization, money, migrations, production data, deployment,
  publishing, or destructive work. Confirm authority and verify the closest real
  boundary.

Read [Autonomy Policy](../../core/autonomy-policy.md) before external effects.

## Compose capabilities progressively

Read [Capability Provider Policy](../../core/provider-policy.md). For software
work, load `efficient-development-workflow` when installed. Before code is
written, reviewed, debugged, or refactored, also load `karpathy-guidelines`.
Select remaining skills from the current unit's need; keep Jarvis as goal and
acceptance owner.

- Read [Product Design](../../capabilities/product-design.md) when product,
  interaction, content, or visual direction could cause material rework.
- Read [Solution Design](../../capabilities/solution-design.md) when API, data,
  state, dependencies, security, platform, or implementation order is non-obvious.
- Read [Product Build](../../capabilities/product-build.md) when the current
  Development Guide is decision-ready.

## Delegate bounded execution

Read [Delegation Policy](../../core/delegation-policy.md). Execute directly when
coordination would cost more than it saves. Otherwise give a worker:

- the current Development Guide;
- repository instructions;
- only named code, contract, and visual sources needed for the task;
- a short ownership clarification when the delegated work is narrower than the
  guide.

Do not send the whole Product Plan, full conversation, unrelated page planning,
logs, secrets, or private reasoning. Parallelize only stable, independently
acceptable units with disjoint writes. Keep shared decisions, integration, and
final acceptance with Jarvis.

## Build, verify, and feed discoveries back

1. Implement the smallest coherent current unit.
2. Inspect the actual diff and run the nearest check that can falsify each claim.
3. Treat worker completion as input, not acceptance.
4. Route durable discoveries to their owning document: product-wide truth to the
   Product Plan or shared source; durable page truth to Page Overview when one
   exists or when a second consumer justifies extracting it; local implementation
   facts to the Development Guide or handback.
5. Refresh affected Development Guides after upstream truth changes.
6. Replan when an assumption fails, scope crosses a new boundary, repository
   truth conflicts with the guide, or the same repair fails twice.

Read [Verification Policy](../../core/verification-policy.md),
[Evidence Policy](../../core/evidence-policy.md), and
[Budget Policy](../../core/budget-policy.md).

## Preserve visual truth

For new or fidelity-sensitive UI, follow
[Visual Source Policy](../../core/visual-source-policy.md). Product planning owns
behavior; an approved Image 2 board owns visual direction. Page documents link
the approved source and restate only implementation-relevant constraints.

Use GPT Image 2 for new design generation. Use Figma only to read a user-supplied
or explicitly selected existing design unless the user explicitly requests Figma
creation or editing.

## Prevent repeated side effects

Before publishing, deploying, messaging, migrating, deleting, charging, or
creating external resources, reconcile the side-effect ledger and current
external state. Follow [Side-Effect Policy](../../core/side-effect-policy.md).

## Finish honestly

Distinguish page or unit done, journey done, and product ready. Stop only when
in-scope claims have fresh evidence or a real blocker requires user input. Report
working behavior, checks actually run, document or code conflicts, missing
evidence, material risk, and next action.
