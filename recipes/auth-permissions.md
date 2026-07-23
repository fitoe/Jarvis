# Authentication and Permissions

## Use when

Identity, sessions, roles, ownership, tenant boundaries, or protected operations
affect the slice.

## Avoid when

The project has a mature auth boundary and the change is unrelated presentation.

## Default solution

- Reuse the existing identity provider and session model.
- Authenticate at the request boundary and authorize at the protected operation.
- Default to deny when required identity or scope is absent.
- Keep client visibility rules as UX, never as the security boundary.
- Avoid storing new credentials or secrets in source or client code.

## Common failures

Role checks without ownership checks, cross-tenant identifiers, stale permissions,
open redirect behavior, and tests that mock away the protected boundary.

## Verify

Exercise an allowed identity and the nearest disallowed identity. Inspect both
response and unchanged protected state.

## Escalate when

Authority is unverified, production identities are required, provider configuration
changes, or permission semantics are directionally unclear.
