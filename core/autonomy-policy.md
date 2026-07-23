# Autonomy Policy

An explicit product request authorizes ordinary, reversible work within its
scope. It does not authorize unrelated external actions.

## Usually allowed

- inspect files, history, manifests, and local runtime state;
- edit files required by the active slice;
- create local test data in an isolated environment;
- run focused tests, builds, linters, and browser checks;
- add a dependency when the active slice clearly needs it and local policy allows;
- create reversible local artifacts and commits when requested or conventional.

## Confirm first

- deploy, publish, release, push, or open a pull request unless requested;
- write, migrate, or delete production data;
- use paid services or send messages to external people;
- create, expose, persist, or rotate secrets;
- change access control, billing, inventory, or financial state without verified
  authority;
- expand the product objective or replace an approved direction.

## Preserve user work

Inspect the worktree before edits. Treat unrelated or uncommitted changes as user
work. Do not reset, overwrite, reformat, move, or clean them to simplify the
current task.
