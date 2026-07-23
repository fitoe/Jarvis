---
name: solution-design
description: Convert a decision-ready product slice into a concrete technical implementation path. Use when APIs, data, state, dependencies, permissions, integration, platform constraints, performance, or file boundaries are non-obvious. Prefer local patterns and mature defaults, plan only the active slice, and leave routine code details to implementation.
---

# Solution Design

Decide how the active slice should work without designing an architecture for
the entire product.

## Build local truth

Inspect manifests, directories, nearby implementations, request and state layers,
data models, tests, configuration, and platform targets. Existing working patterns
outrank Jarvis defaults.

For a new project without useful local truth, select the closest profile from
[Golden Paths](../../golden-paths/README.md). For a known feature family, load
only its entry from [Feature Recipes](../../recipes/README.md).

## Decide only material boundaries

Resolve decisions that affect speed, consistency, shared contracts, security,
performance, or reversibility:

- files and modules that own behavior;
- data shape and persistence;
- API or integration boundary;
- state ownership and lifecycle;
- dependency choice;
- permissions and external effects;
- mock-to-real boundary;
- verification seam.

Do not pre-plan local handlers, helper names, component internals, or ordinary
framework syntax.

## Classify uncertainty

- Supported by local evidence: decide and cite it.
- Reversible with a mature default: decide, record assumption, continue.
- Uncertain but safely testable: run a small timeboxed spike.
- Hard to reverse or externally risky: ask for direction or authority.

Read [Decision Policy](../../core/decision-policy.md).

## Produce an implementation path

For the active slice, return:

- observable result and product claims;
- relevant existing patterns;
- file or system-boundary map;
- ordered implementation steps;
- material decisions and assumptions;
- failure and recovery behavior;
- smallest verification for each claim;
- replanning triggers.

Use [Active Slice Template](../../templates/active-slice.md) when durable handoff
is needed. Avoid separate decision, feature, state, API, mock, and verification
documents unless different consumers genuinely need them.

Route to `product-design` when technical facts invalidate the product direction.
Route to `product-build` when implementation can proceed without choosing a
competing architecture.
