# Capability Provider Policy

Jarvis is the control plane. Skills, plugins, models, CLIs, services, and
subagents are bounded providers of design, implementation, verification, or
external effects.

Before material provider work that can affect outcome, authority, cost, or
evidence, define only what affects the active slice:

- input truth and claim;
- expected output and evidence;
- authority and budget limits;
- capability needed, such as reference-image input or real-environment access.

Keep this contract in the active working context. Do not create a provider
manifest, handoff document, or registry unless another consumer needs it.

Inspect a provider capability only when the claim depends on it. Prefer the
project's configured provider. Do not install or invent a second workflow when a
small direct fallback can satisfy the claim.

Do not reload unchanged provider instructions without a new capability question.
Prefer a direct local solution when provider setup cost exceeds the value of the
bounded claim. Batch independent provider discovery, but keep overlapping writes
and shared decisions sequential.

For new UI design generation, bind the provider to GPT Image 2. Do not infer
permission to use Figma from installed Figma skills, an available Figma MCP, or
generic repository design guidance. Use Figma only to read an existing source
the user supplied or explicitly selected, unless the user explicitly requests a
Figma creation or editing workflow.

A provider may propose decisions and return artifacts or observations. It may
not broaden product scope, override product truth, expand authority, own Jarvis
state, or declare the slice complete. Persist provider output only when code,
later prompts, recovery, or another real consumer needs it.

When a provider is unavailable or lacks a required capability, use a bounded
fallback if it can support the same claim. Otherwise mark that claim unverified
and continue only with work whose truth is unaffected. Record provider identity
or version when a later run could invalidate durable evidence.

## Select skills progressively

For software planning, implementation, debugging, review, or refactoring, load
`efficient-development-workflow` when installed. It governs process size,
risk-based verification, and outcome-focused tests.

Before writing, reviewing, debugging, or refactoring code, also load
`karpathy-guidelines` when installed. It governs assumptions, simplicity,
surgical edits, and verifiable success.

For the remaining need:

1. Honor skills explicitly named by the user.
2. Inspect available skill descriptions for the active slice's missing
   capability.
3. Load the smallest non-overlapping set that materially improves the result.
4. Read each selected skill before using it, then keep its output inside the
   Jarvis goal, authority, budget, and evidence model.

Do not load skills by category, preload possible future skills, or let several
workflow skills own the same task. If no relevant skill is installed, use local
project truth and the smallest safe fallback; do not install one without user
authority.
