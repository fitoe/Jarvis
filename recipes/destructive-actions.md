# Destructive Actions

## Use when

Work deletes, replaces, migrates, publishes, or irreversibly changes data or
external state.

## Avoid when

The operation is a reversible local edit with no shared consumer.

## Default solution

- Resolve exact targets with read-only checks.
- Confirm authority and scope before execution.
- Prefer soft delete, backup, transaction, dry run, or other recovery mechanism
  when appropriate.
- Make retries idempotent or detect partial completion.
- Define success, rollback, and cleanup before acting.
- Use isolated or disposable data for verification.

## Common failures

Broad path or query targets, unverified backups, partial migrations, retrying
non-idempotent operations, and treating a command exit code as final external state.

## Verify

Inspect the exact intended target before action and the resulting external state
after action. Verify rollback or recovery when the completion claim includes it.

## Escalate when

The user has not explicitly authorized the action, target scope is ambiguous, or
recovery cannot be demonstrated.
