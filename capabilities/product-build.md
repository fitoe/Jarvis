# Product Build Capability

Turn the active slice into verified behavior across frontend, backend, data,
integrations, automation, or configuration.

## Before editing

1. Read repository instructions and inspect the worktree.
2. Confirm observable result and success claims.
3. Find the closest existing implementation.
4. Identify the smallest check that can falsify each claim.
5. Resolve only ambiguity that materially changes implementation.

Follow [Code Quality Policy](../core/code-quality-policy.md).

## Implement the smallest coherent change

- Reuse existing components, services, types, and dependencies.
- Match local architecture and style.
- Avoid one-use abstractions and speculative flexibility.
- Touch only files required by the active slice.
- Remove only code made unused by this change.
- Keep mock behavior separate from real integration claims.

Load one [Feature Recipe](../recipes/README.md) only when the project lacks a
closer pattern.

## Visual implementation

Follow [Visual Source Policy](../core/visual-source-policy.md). When approved
visual evidence exists and fidelity is part of success, treat it as the visual
source of truth while product behavior remains authoritative. Preserve page type,
hierarchy, density, typography, color, assets, states, and action priority.

Use the Product Design plugin's `Product Design:image-to-code` and visual QA when
available, without transferring Jarvis ownership. Capture source and
implementation at the same viewport and state, compare them together, and repair
the largest visible gaps within budget. Record simplifications instead of calling
them parity. Do not require a generated mock for a small edit that already has a
clear project pattern.

When the source is too complex for reliable one-pass inspection, use the
conditional decomposition defined by Visual Source Policy. Implement semantic
sections against the shared visual language, assemble them continuously, and
require both section-level and full-page comparison before accepting parity.

Treat other skills, plugins, models, and services the same way. Follow
[Capability Provider Policy](../core/provider-policy.md); accept their bounded
output, then verify the active Jarvis claim.

## Adapt rather than patch blindly

Stop and replan when a material assumption fails, scope crosses a new boundary,
a closer project pattern invalidates the approach, the same failure survives two
repairs, or verification cannot prove the intended claim.

Return changed behavior, changed files, checks actually run, stale or missing
evidence, remaining risk, and next action.
