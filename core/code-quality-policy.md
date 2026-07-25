# Code Quality Policy

Use these rules for every implementation slice.

Load `karpathy-guidelines` when installed before writing, reviewing, debugging,
or refactoring code. This policy remains the fallback when that skill is absent.

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

## Activate quality overlays only when relevant

- **Accessibility:** public UI, forms, keyboard flows, or assistive semantics.
- **Performance:** startup, large collections, heavy assets, or latency-sensitive APIs.
- **Security and privacy:** identity, untrusted input, secrets, or sensitive data.
- **Operability:** background jobs, integrations, or production services.
- **Compatibility:** public contracts, migrations, or multiple consumers.

An overlay adds only checks needed by its active claim. Do not make every quality
dimension a gate for every slice.

## After editing

- Remove imports, variables, and files made unused by this change.
- Run focused verification before broad checks.
- Inspect actual exit status and observable results.
- Report skipped checks as skipped and uncertain claims as unverified.

When a solution grows far beyond the behavior it provides, stop and simplify.
