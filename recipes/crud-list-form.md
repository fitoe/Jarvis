# CRUD, Lists, and Forms

## Use when

Users list, view, create, edit, filter, or remove structured records.

## Avoid when

The action is a workflow transition, immutable event, or high-integrity financial
operation that should not be modeled as generic CRUD.

## Default solution

- Define one authoritative record shape and boundary validation.
- Reuse existing query, form, table, and mutation patterns.
- Implement only reachable loading, empty, success, validation, and failure states.
- Preserve filters and pagination when returning from detail when users benefit.
- Refresh or update local state using the project's existing consistency model.
- Confirm delete when accidental activation is plausible.

## Common failures

Duplicate validation, stale list state, hidden server errors, unbounded queries,
and UI-only permission checks.

## Verify

Exercise the in-scope create or update path, inspect persisted data, and confirm the
list or detail reflects it. Add a regression check for shared validation.

## Escalate when

Bulk mutation, approval workflow, audit history, concurrency, authorization, or
production data changes the risk.
