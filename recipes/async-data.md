# Async Data and Remote APIs

## Use when

The slice reads or mutates remote data, calls another service, or manages cached
asynchronous state.

## Avoid when

The value is deterministic local state with no external lifecycle.

## Default solution

- Reuse the project's request and cache layer.
- Define the smallest typed boundary needed by the consumer.
- Distinguish initial loading, background refresh, empty data, retryable failure,
  and terminal failure only when reachable.
- Keep cancellation, deduplication, retry, and cache behavior consistent with the
  existing layer.
- Place mock and real implementations behind the same consumer-facing boundary.

## Common failures

Duplicate clients, silent error swallowing, retry storms, race conditions, stale
mutations, and reporting mock success as real integration.

## Verify

Exercise one successful boundary call and the most material failure or stale-state
case. Inspect payload and resulting state, not only call count.

## Escalate when

API semantics are unknown, authentication is missing, streaming or offline support
is required, or external rate and cost limits matter.
