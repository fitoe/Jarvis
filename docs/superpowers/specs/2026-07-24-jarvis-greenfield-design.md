# Jarvis Greenfield Design

## Outcome

Create a public, reusable skill suite that can take an idea to working product
software while keeping process proportional to uncertainty, change radius, and
external impact.

Success means:

- one entry point can start or resume delivery from a product goal;
- routine work reaches implementation without mandatory planning artifacts;
- unfamiliar or risky work receives just-in-time product and technical analysis;
- implementation follows simple, surgical coding rules;
- completion claims map to fresh evidence at the closest useful boundary;
- interrupted work resumes from one small state file;
- skill behavior is protected by scenario evaluations.

## System shape

Use one repository with four thin skill entry points and a shared policy kernel.
The entry points are capabilities, not ordered stages. `product-delivery` owns
the loop. It routes to `product-design`, `solution-design`, or `product-build`
only when the active slice benefits from that context.

## Operating loop

1. Convert the request into outcome, scope, and observable success.
2. Inspect repository instructions, current behavior, nearby patterns, and risk.
3. Choose the smallest valuable vertical slice.
4. Resolve only decisions that materially affect that slice.
5. Implement the smallest coherent change.
6. Verify the user or system claim with the closest falsifying check.
7. Update durable state and either adapt, continue, or stop on a true blocker.

## Adaptive policy

Workflow intensity uses three factual axes:

- uncertainty: whether different interpretations change the product;
- change radius: local behavior versus shared contracts or reusable logic;
- execution impact: reversible local work versus production or external effects.

Routine work uses one narrow check. Shared work adds regression and contract
evidence. High-risk work confirms authority and uses the closest integration or
release boundary.

## Planning model

Plans are hypotheses, not commitments. Keep a coarse product map and expand only
the active slice. Each slice names its observable result, relevant boundaries,
existing patterns, implementation steps, verification, assumptions, and risks.

Golden Paths provide product-level defaults when a new repository lacks local
truth. Recipes provide feature-level defaults. Both declare when they apply,
when they do not, failure modes, verification, and escalation triggers.

## Code quality

The shared code-quality policy incorporates the practical core of
`karpathy-guidelines`: surface material ambiguity, prefer the simplest solution,
touch only necessary code, avoid speculative abstractions, and define evidence
before claiming completion.

## Testing model

Testing starts from product claims. A claim selects the smallest check that
could prove it false. Unit, integration, browser, visual, security, and release
checks are tools, not mandatory levels. Repeated failures, invalid assumptions,
or scope expansion trigger replanning instead of more patching.

## State and artifacts

Default durable state is one small file containing goal, success claims, current
slice, assumptions, decisions, blockers, evidence, and next action. Specialized
briefs, contracts, visual sources, and reports are created only for real
consumers.

## Safety boundary

Pause for destructive or hard-to-reverse actions, unknown authority, secrets,
production data, paid or external effects, direction-level ambiguity, and
completion claims lacking evidence. Everything else can proceed as an explicit,
reversible assumption.

## Evaluation

Treat skill instructions as behavioral code. Scenario evaluations cover routine
changes, new-product walking skeletons, shared API work, authorization boundaries,
visual fidelity, and interrupted-session recovery. Fix a failing scenario before
adding a broad rule.

## Initial non-goals

- workflow runtime or custom agent engine;
- mandatory dashboards or progress overlays;
- exhaustive framework-specific architecture;
- automated deployment or production mutation;
- migration of the previous four repositories.
