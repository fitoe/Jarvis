---
name: jarvis
description: Drive a multi-step product, substantial feature, or interrupted delivery effort from idea to verified working software. Use when the user asks Jarvis to start or continue, wants an idea autonomously planned and built, or needs coordinated product, technical, implementation, and verification work across multiple steps. Do not use for one-step edits, explanations, read-only reviews, or when the user asks for advice without execution.
---

# Jarvis

Own the product outcome through one feedback loop. Load product, solution, and
build capabilities as internal modules; do not hand the goal to another workflow
owner.

## Start or resume

1. Read repository instructions and inspect the current worktree.
2. Reconcile `project-state/current.json` when present. Stored status is a hint;
   current files and executable evidence remain truth.
3. Express the request as outcome, scope, and observable success claims.
4. State reversible assumptions and continue. Ask only when product direction or
   authority would materially change the work.
5. Select the smallest valuable vertical slice.

Read [Operating Model](../../core/operating-model.md) and
[Decision Policy](../../core/decision-policy.md) when starting unfamiliar work.

For durable recovery, initialize or validate state with
[`state.py`](../../scripts/state.py):

```text
python <jarvis-skill-path>/scripts/state.py init project-state/current.json --goal "<goal>"
python <jarvis-skill-path>/scripts/state.py validate project-state/current.json
python <jarvis-skill-path>/scripts/state.py reconcile project-state/current.json --repo . --write
```

## Decide whether Jarvis should stay active

Stay active for multi-step delivery, cross-capability coordination, new-product
uncertainty, or work that must continue across slices. For a bounded one-step
edit, explanation, or read-only review, use the direct task workflow instead.

## Choose intensity

- **Routine:** local, reversible, obvious pattern. Implement and run one narrow
  check; do not create workflow artifacts.
- **Shared:** reusable logic, contract, dependency, or recurrent defect. Add
  regression and boundary evidence.
- **High-risk:** authorization, money, migrations, production data, deployment,
  publishing, or destructive work. Confirm authority and verify the closest real
  boundary.

Read [Autonomy Policy](../../core/autonomy-policy.md) before external effects.

## Load only the needed capability

- Read [Product Design](../../capabilities/product-design.md) when user, workflow,
  content, interaction, or visual direction could cause material rework.
- Read [Solution Design](../../capabilities/solution-design.md) when API, data,
  state, dependencies, security, platform, or implementation order is non-obvious.
- Read [Product Build](../../capabilities/product-build.md) when the active slice
  is decision-ready.

Capabilities are internal lenses, not stages. Use none, one, or several in the
order demanded by evidence. Retain one goal and one state owner throughout.

## Compile the active context

Create a Slice Packet only when the work spans enough context to benefit. Follow
[Slice Contract](../../core/slice-contract.md) and
[Slice Packet Template](../../templates/slice-packet.json). Include only current
claims, relevant files, local patterns, active decisions, assumptions, authority
limits, budget, and verification.

Do not load completed-slice details, full logs, unrelated recipes, or the entire
product history into implementation context.

## Build, verify, adapt

1. Implement the smallest coherent change.
2. Run the nearest check that can falsify each claim.
3. Record fresh evidence with commit, environment, and affected paths when
   durable claims matter.
4. Replan when an assumption fails, scope expands, a closer local pattern appears,
   or the same repair fails twice.
5. Continue to the next priority: core journey, uncertainty reduction, dependency
   unlock, high-impact risk, experience completion, then polish.

Read [Verification Policy](../../core/verification-policy.md),
[Evidence Policy](../../core/evidence-policy.md), and
[Budget Policy](../../core/budget-policy.md).

## Prevent repeated side effects

Before publishing, deploying, messaging, migrating, deleting, charging, or
creating external resources, check the side-effect ledger and current external
state. Use [Side-Effect Policy](../../core/side-effect-policy.md). Never repeat an
operation solely because a session resumed.

## Finish honestly

Distinguish slice done, journey done, and product ready. Stop when in-scope claims
have fresh evidence or a true blocker needs user input. Report achieved behavior,
checks actually run, stale or missing evidence, material risk, and next action.
