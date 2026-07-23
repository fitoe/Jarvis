# API Service Golden Path

## Use when

The product surface is an HTTP, RPC, event, or integration API rather than a
browser UI.

## Defaults

- Define behavior at the external contract boundary.
- Validate inputs and return stable error semantics.
- Keep authorization next to the protected operation.
- Use idempotency where retries can duplicate side effects.
- Add observability for failures that operators must diagnose.
- Prefer one deployable service until ownership or scaling requires separation.

## First slice

Deliver one request through validation, business logic, persistence or integration,
and a stable response.

## Verify

Run an integration test against the real local boundary and inspect side effects.

## Escalate when

Public compatibility, external consumers, rate limits, sensitive data, webhooks,
queues, or production migration enters scope.
