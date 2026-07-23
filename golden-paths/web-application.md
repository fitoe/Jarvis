# Web Application Golden Path

## Use when

A browser product combines authenticated UI, business workflows, server logic,
and persistent data.

## Defaults

- Use one cohesive typed web stack before splitting frontend and backend.
- Use a relational database when entities and transactions dominate.
- Keep authentication and authorization server-enforced.
- Validate inputs at external boundaries.
- Separate browser-visible errors from operational diagnostics.
- Start with one responsive viewport family; add others when product scope needs.

## First slice

Deliver one authenticated or public user action through route, UI, business rule,
and persistence. Include loading, success, and reachable failure behavior.

## Verify

Exercise the real local flow and inspect the resulting server or persisted state.
Add integration evidence for shared contracts.

## Escalate when

Identity provider, multi-tenancy, payments, regulated data, real-time behavior, or
independent service ownership changes the boundary.
