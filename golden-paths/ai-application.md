# AI Application Golden Path

## Use when

Model generation, retrieval, tool use, classification, or agent behavior is a
core user-facing capability.

## Defaults

- Separate deterministic product logic from model-dependent behavior.
- Persist prompts, model choice, and evaluation inputs as versioned configuration
  when they materially affect output.
- Design timeout, retry, cancellation, cost, and partial-result behavior.
- Keep secrets server-side and treat retrieved or user content as untrusted input.
- Use representative evaluations; do not infer quality from one demo.

## First slice

Deliver one narrow user job with fixed representative inputs, visible failure
handling, and a measurable output expectation.

## Verify

Combine deterministic contract checks with a small representative evaluation set.
Report model, data, and environment limits.

## Escalate when

External tool actions, sensitive data, autonomous side effects, high usage cost,
or safety-critical output enters scope.
