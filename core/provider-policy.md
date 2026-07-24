# Capability Provider Policy

Jarvis is the control plane. Skills, plugins, models, CLIs, and services are
bounded providers of design, implementation, verification, or external effects.

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

A provider may propose decisions and return artifacts or observations. It may
not broaden product scope, override product truth, expand authority, own Jarvis
state, or declare the slice complete. Persist provider output only when code,
later prompts, recovery, or another real consumer needs it.

When a provider is unavailable or lacks a required capability, use a bounded
fallback if it can support the same claim. Otherwise mark that claim unverified
and continue only with work whose truth is unaffected. Record provider identity
or version when a later run could invalidate durable evidence.
