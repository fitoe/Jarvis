---
name: product-build
description: Implement and verify a decision-ready product slice across frontend, backend, data, API, automation, or infrastructure code. Use whenever working software must be created or changed. Follow existing project patterns, make the smallest coherent change, test product claims at the nearest useful boundary, and replan when evidence disproves assumptions.
---

# Product Build

Turn the active slice into verified behavior. Implementation includes frontend,
backend, data, integrations, automation, and configuration; visual fidelity is a
conditional capability, not the default path.

## Before editing

1. Read repository instructions and inspect the worktree.
2. Confirm the active slice has an observable result and success claims.
3. Find the closest existing implementation.
4. Identify the smallest check that can falsify each claim.
5. Resolve only ambiguity that would materially change the implementation.

Read [Code Quality Policy](../../core/code-quality-policy.md).

## Implement the smallest coherent change

- Reuse existing components, services, types, and dependencies.
- Match local architecture and style.
- Avoid abstractions for one use and speculative flexibility.
- Touch only files required by the active slice.
- Remove only code made unused by the current change.
- Keep mock behavior explicitly separate from real integration claims.

For unfamiliar feature behavior, load one relevant
[Feature Recipe](../../recipes/README.md). Treat it as a default, not a required
layer stack.

## Visual implementation

When an approved visual source exists and fidelity is part of success:

- preserve page type, hierarchy, density, states, and action priority;
- inspect the source before coding;
- use same-viewport screenshots for a visual claim;
- fix the largest visible mismatch first;
- record simplifications rather than calling them parity.

Do not require pixel-level extraction for ordinary project-convention UI. Increase
fidelity work only when the source, user, or completion claim requires it.

## Verify from claims

Run focused checks first. Add regression coverage for shared behavior or a defect
that can recur. Use real integration boundaries for permissions, persistence,
money, production effects, or release claims.

Read [Verification Policy](../../core/verification-policy.md). Inspect command
output and observable state before reporting success.

## Adapt rather than patch blindly

Stop and replan when:

- a material assumption is false;
- scope crosses a new shared or external boundary;
- a closer project pattern invalidates the approach;
- the same failure survives two repair attempts;
- verification cannot prove the intended claim.

Return changed behavior, changed files, checks actually run, remaining risk, and
the next valuable slice. Route back to `product-design` or `solution-design` only
for the specific decision that became invalid.
