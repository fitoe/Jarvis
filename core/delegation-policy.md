# Delegation Policy

Jarvis owns project control. Workers implement or verify bounded work; they do
not inherit the product goal, roadmap, authority, shared decisions, integration,
or final acceptance.

## Decide direct, delegated, or parallel execution

Delegate when a task has one clear observable result, stable ownership, enough
local truth, and checkable acceptance. Work directly when coordination costs more
than it saves or the capable model must first resolve product direction,
architecture, authority, or an unstable shared contract.

Run workers concurrently only when tasks:

- have independent observable results and stable integration points;
- use disjoint write sets or isolated workspaces;
- do not race on shared runtime state or external side effects;
- can be accepted without another task completing first.

Sequence work when agents would edit the same boundary, depend on an unsettled
contract, or invalidate each other's evidence. Parallelism is an optimization,
not a completion requirement.

## Give the worker the Development Guide

For substantial page or delivery-unit work, the current Development Guide is the
primary delegated context. Give the worker:

- the Development Guide;
- repository instructions;
- named code paths and existing patterns relevant to the task;
- linked contract or visual sources only when the guide cannot safely restate
  their consumed detail;
- a short clarification of owned paths and acceptance when delegation covers a
  narrower claim than the guide.

Do not create a second JSON packet around the guide. Do not send the full Product
Plan, Page Overview, conversation history, unrelated roadmap details, completed
work logs, secrets, or controller reasoning.

Before dispatch, run the context-closure check in
[Planning Policy](planning-policy.md). If the worker cannot identify goal,
non-goals, complete behavior, authority, change boundaries, acceptance, and
escalation conditions from the guide and named code, the capable model refreshes
the guide first.

Routine delegated work that needs no durable guide may use one concise prompt
containing the same bounded facts. Do not create planning artifacts solely
because another worker is involved.

## Keep shared decisions centralized

Ordinary consumption of an existing shared component or API may remain local.
Return work to Jarvis when implementation would:

- redefine shared behavior or a contract for other consumers;
- change product-wide authority, permissions, data meaning, or visual truth;
- require cross-page coordination not described by the guide;
- conflict with current repository or upstream planning truth;
- make acceptance impossible at the delegated boundary.

The worker returns `needs-context` with the missing rule, blocked behavior, safe
work already completed, and smallest additional decision needed. It does not
invent the shared answer.

## Preserve visual integration context

When [Visual Source Policy](visual-source-policy.md) activates complex visual
decomposition, keep prompts small without stripping necessary visual truth.
Section work receives the full-page overview, authoritative section source,
adjacent boundaries, shared tokens and components, cross-section constraints,
owned integration boundary, and both section and full-page verification
expectations.

Jarvis keeps the Visual Map, shared shell, continuous assembly, and final visual
acceptance. Individual section evidence cannot prove assembled-page parity.

## Activate independent checking by risk

Routine local work normally uses controller verification. Use an independent
checker when it can materially challenge a shared, high-risk, fidelity-sensitive,
disputed, or final-acceptance claim. The checker receives the claim, relevant
truth, diff, evidence, and authority boundary; it does not inherit project control
and does not reimplement the feature.

Keep maker output and checker judgment separate. A checker opinion is not evidence
unless it inspects a real diff, command result, browser state, data result, or
other falsifiable boundary. Jarvis reconciles findings and retains acceptance and
termination ownership.

## Require a readable handback

The worker returns an ordinary development summary:

```markdown
## Completed

## Changed files

## Checks and actual results

## Decisions or assumptions discovered

## Acceptance criteria covered

## Remaining risk or incomplete work

## Context requested
```

The handback names material differences between documentation and code,
unexpected dependencies, and newly discovered shared constraints. Jarvis
inspects the diff, routes durable discoveries to the owning planning document,
refreshes affected Development Guides, and runs the nearest integration check.

Worker completion remains input to acceptance. Use an independent verifier only
when it can reveal a material shared, high-risk, fidelity-sensitive, or disputed
failure. Final page, journey, and product acceptance stay with Jarvis.
