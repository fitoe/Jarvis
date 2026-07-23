# Internal Tool Golden Path

## Use when

Known staff users need data entry, review, approval, operations, or reporting.

## Defaults

- Optimize for clear workflows, dense readable information, and safe operations.
- Reuse the organization's identity and role model.
- Prefer server-side authorization over hidden UI controls.
- Use conventional tables, forms, filters, and audit-friendly state transitions.
- Make destructive and bulk actions explicit and recoverable where possible.

## First slice

Deliver the highest-frequency staff task end to end with representative local or
isolated data.

## Verify

Exercise the workflow under an allowed role and a disallowed role when permission
is part of the claim. Inspect persisted results.

## Escalate when

Production writes, bulk mutation, approval authority, audit retention, or personal
data is involved.
