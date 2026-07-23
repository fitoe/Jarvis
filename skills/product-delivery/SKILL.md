---
name: product-delivery
description: Drive a product from an idea, request, or interrupted work state to verified working software. Use whenever the user asks to start, plan, build, continue, finish, or autonomously deliver a product or multi-step feature. Keep process proportional, route specialist context only when needed, and continue until success is evidenced or a true blocker remains.
---

# Product Delivery

Own the product outcome. Control work through short feedback loops, not a fixed
sequence of stage gates.

## Start or resume

1. Read repository instructions and current worktree state.
2. Read `project-state/current.yaml` when it exists; verify it against current
   files instead of trusting stale status.
3. Express the request as outcome, smallest useful scope, and observable success.
4. State low-risk assumptions and continue. Ask only when direction or authority
   would materially change the work.
5. Select the smallest valuable vertical slice.

Read [Operating Model](../../core/operating-model.md) for the feedback loop and
[Decision Policy](../../core/decision-policy.md) when uncertainty is material.

## Choose workflow intensity

- **Routine:** local, reversible, obvious pattern. Implement and run one narrow
  check. Do not create a spec or plan merely because code changes.
- **Shared:** reusable logic, API contract, dependency, or recurrent defect. Add
  regression and boundary evidence.
- **High-risk:** permissions, money, migrations, production data, deployment,
  publishing, or destructive work. Confirm authority and verify the closest real
  boundary.

Read [Verification Policy](../../core/verification-policy.md) before making a
completion claim.

## Route by unresolved need

Capabilities are optional and may be loaded in any order:

- Route to `product-design` when user, workflow, content, interaction, or visual
  direction is unclear enough to cause rework.
- Route to `solution-design` when architecture, API, state, dependency, security,
  platform, or implementation order is non-obvious.
- Route to `product-build` when the active slice is decision-ready.
- Use framework-specific skills only for concrete platform details.

Do not route routine work away from implementation. Load one specialist context
at a time unless a real conflict spans capabilities.

## Plan the active slice

Keep the product map coarse. Expand only the current slice using
[Planning Policy](../../core/planning-policy.md) and
[Active Slice Template](../../templates/active-slice.md).

Every implementation step names:

- the observable change;
- affected files or system boundary;
- existing pattern or chosen default;
- the check that proves the claim.

## Continue from evidence

After each slice:

1. Inspect verification results.
2. Classify failures before patching again.
3. Replan when an assumption fails, scope grows, or the same repair fails twice.
4. Update `project-state/current.yaml` only when durable recovery is useful.
5. Continue to the next highest-value slice unless success is achieved or a true
   blocker requires user input.

## Hard stops

Pause for destructive or hard-to-reverse actions, unknown authority, secrets,
production or paid external effects, direction-level ambiguity, or a proposed
completion claim without evidence. Read
[Autonomy Policy](../../core/autonomy-policy.md) for the boundary.

## Report

Keep updates compact:

- achieved or current observable result;
- verification actually run;
- current blocker or material risk;
- next action.

Do not report optional artifacts, maturity scores, or internal ceremony as product
progress.
