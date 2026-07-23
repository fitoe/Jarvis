# Code Quality Policy

Use these rules for every implementation slice.

## Before editing

- State assumptions only when ambiguity could change the implementation.
- Find the closest existing implementation and follow its conventions.
- Define the user or system behavior that the change must produce.
- Identify the smallest check able to falsify that claim.

## While editing

- Write the minimum code that satisfies the active slice.
- Keep every changed line traceable to the requested outcome.
- Reuse existing components, services, types, and dependencies.
- Avoid abstractions for one use, speculative configuration, compatibility layers
  without consumers, and unrelated cleanup.
- Match local style even when another style is personally preferable.

## After editing

- Remove imports, variables, and files made unused by this change.
- Run focused verification before broad checks.
- Inspect actual exit status and observable results.
- Report skipped checks as skipped and uncertain claims as unverified.

When a solution grows far beyond the behavior it provides, stop and simplify.
