# Delegation Policy

Jarvis owns project control. Subagents execute or verify bounded work; they do not
inherit the project goal, roadmap, authority, state, or final acceptance decision.

## Keep controller responsibilities centralized

Jarvis maintains the coarse product map, critical path, dependencies, shared
contracts, Product Truth, Visual Truth, material risks, budgets, integration
state, and claim-evidence map. It selects the next slice, resolves cross-cutting
decisions, integrates results, and decides slice, journey, or product completion.

## Decide direct, delegated, or parallel execution

Delegate when a task has a clear observable result, bounded ownership, enough
local truth, and a checkable handback. Work directly when delegation costs more
than it saves or when the controller must first resolve architecture, product
direction, authority, or an unstable shared contract.

Run subagents concurrently only when tasks:

- have independent outputs and stable integration points;
- use disjoint write sets or isolated worktrees;
- do not race on shared runtime state or external side effects;
- can be accepted without another task finishing first.

Sequence work when agents would edit the same boundary, depend on an unsettled
contract, or could invalidate each other's evidence. Parallelism is an
optimization, not a completion requirement.

## Send the least sufficient context

Create a Delegated Task Packet only when work is delegated. Follow
[Delegated Task Template](../templates/delegated-task.json), set the role to
`implement` or `verify`, and include:

- why the task matters and its observable result;
- in-scope behavior, owned paths, and do-not-touch boundaries;
- only relevant truth, source files, patterns, decisions, and contracts;
- authority, side-effect, dependency, and budget limits;
- selected skills, claims, checks, and integration handoff.

The packet is a dispatch shape, not a mandatory file. Put it directly in the
subagent prompt unless recovery, auditing, or another real consumer needs it
persisted.

Do not send full conversation history, the whole roadmap, completed-slice logs,
unrelated files, secrets, or the controller's private reasoning. A verification
agent receives the claim, acceptance criteria, and raw artifacts—not the
implementer's conclusion or intended answer.

When [Visual Source Policy](visual-source-policy.md) activates complex visual
decomposition, populate `inputs.visual_context` only for section work. Include
the full-page overview, authoritative section source, adjacent boundaries,
shared tokens and components, cross-section constraints, owned integration
boundary, and both section and full-page verification expectations. Jarvis keeps
the Visual Map, shared shell, continuous assembly, and final visual acceptance.

## Require a useful handback

The worker returns `done`, `partial`, `needs-context`, or `blocked`, plus changed
files, checks and actual results, new assumptions or decisions, fresh evidence,
side effects, and remaining risk. It must not broaden scope, cross ownership, or
exercise authority absent from the packet.

Jarvis inspects the result, reconciles overlapping changes and evidence, and runs
the nearest integration check. Worker self-checks are enough for low-risk bounded
work when the controller can cheaply verify them. Use an independent verifier for
shared contracts, high-risk behavior, fidelity-sensitive UI, or disputed claims
when independence can reveal a real failure. Do not require fixed implementer,
spec-reviewer, and code-reviewer chains for every task.

Final acceptance stays with Jarvis. It closes work only when the in-scope claim
map has fresh evidence at the declared slice, journey, or product level.
