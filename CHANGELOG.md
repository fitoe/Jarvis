# Changelog

## 0.11.0 - 2026-07-26

- Make finite Loop Engineering the Jarvis operating model: Discover, Frame,
  Execute, Observe, Verify, Record, then Continue or Stop.
- Define a logical Loop Contract, nested evidence scopes, light Spine, explicit
  termination states, and changed-condition retry behavior.
- Integrate authorized host Goal creation, visible browser observation, and
  risk-based independent checking without adding a workflow runtime.
- Add behavior evals for discovery, framing, observation, reframing, checking,
  evidence scope, recovery, termination, and finite-loop boundaries.
- Supersede the separate automatic-Goal and browser-workbench lifecycle.

## 0.10.0 - 2026-07-25

- Add a concise human-agent collaboration contract with milestone-based progress
  updates and outcome-first handoff.
- Define add, redirect, pause, resume, cancel, correction, and preference
  precedence behavior.
- Batch independent discovery and avoid repeated provider or context loading.
- Stop equivalent failure retries, preserve independent progress, and use bounded
  fallback only when it supports the same claim.
- Activate accessibility, performance, security, privacy, operability, and
  compatibility checks only from relevant claims.
- Add discriminating behavior evaluations for collaboration, steering, execution
  economy, recovery, and conditional quality.

## 0.9.0 - 2026-07-25

- Replace Slice Packet and Delegated Task Packet planning with human-readable
  Product Plan, Page Overview, and Development Guide documents.
- Make Page Overview optional: omit it for simple single-guide pages and create
  it for multiple guides, consumers, complex durable behavior, or repeated
  implementation cycles.
- Make Development Guide the self-contained context boundary for current page or
  delivery-unit implementation.
- Add truth ownership, controlled repetition, context-closure review, semantic
  refresh, coherent splitting, `needs-context`, and reverse feedback rules.
- Replace JSON packet templates with Markdown planning templates while retaining
  optional JSON only for interrupted controller state.
- Package a complete Lead Operations Golden Example where the optional Page
  Overview has multiple durable consumers.
- Add behavior evaluations for document-first planning, shared-boundary
  escalation, read-only dry runs, truth conflicts, splitting, and handback.
- Keep behavioral improvement unclaimed until agent-vs-baseline Lead List runs
  provide evidence.

## 0.8.1 - 2026-07-24

- Bind new UI design generation to GPT Image 2 by default.
- Prevent installed Figma skills, Figma MCP availability, or generic repository
  guidance from silently replacing the configured Image 2 workflow.
- Limit Figma to reading user-supplied or explicitly selected existing designs
  unless the user explicitly requests Figma creation or editing.

## 0.8.0 - 2026-07-24

- Require Image 2 design before new page-level UI, key visual states, and material
  visual redesigns, with narrow exceptions for established-system edits.
- Support multi-page design boards as efficient, consistent project baselines.
- Require one human Visual Baseline approval before UI implementation, without
  adding repeated per-page approval gates.
- Extract only constraints consumed by implementation or verification.
- Keep approved boards authoritative; use crops or high-resolution details only
  to improve inspectability without silently redesigning the product.

## 0.7.0 - 2026-07-24

- Activate complex visual decomposition by inspectability and fidelity risk,
  without adding image-size gates or burdening ordinary UI work.
- Preserve a full-page source and compact Visual Map across semantic sections.
- Keep approved-source crops authoritative and regenerated detail views
  supplementary.
- Give delegated section work global style, adjacent-boundary, integration, and
  dual-scale verification context.
- Require continuous assembly and both section-level and full-page visual QA.
- Add behavior evaluations for activation, bypass, source authority, context,
  decomposition quality, and final acceptance.

## 0.6.0 - 2026-07-24

- Make Jarvis explicitly own global planning, dependencies, quality, integration,
  and final acceptance.
- Add a least-context Delegated Task Packet for bounded subagent work.
- Parallelize only tasks with stable integration points and isolated or disjoint
  writes.
- Keep authority centralized and require useful worker handback evidence.
- Use independent verification proportionally instead of fixed reviewer chains.
- Add behavior evaluations for project control, safe and unsafe parallelism,
  context minimization, integration, and final acceptance.

## 0.5.0 - 2026-07-24

- Use `efficient-development-workflow` as the installed process governor for
  software tasks.
- Use `karpathy-guidelines` as the installed code-work governor.
- Select user-named and domain skills progressively from the active slice.
- Prevent unrelated skill preloading, overlapping workflow ownership, and
  unauthorized skill installation.
- Add behavior evaluations for fixed governors and automatic domain routing.

## 0.4.0 - 2026-07-24

- Separate Product Truth, Visual Truth, implementation choices, and evidence.
- Add a bounded provider contract for skills, plugins, models, CLIs, and services.
- Distinguish product, functional, visual, quality, and release claims.
- Add product-uncertain and visual-fidelity overlays without creating stages.
- Treat missing Image 2 reference-image support as degraded style evidence.
- Add Shadow Mode comparison guidance and behavior evaluations for these rules.

## 0.3.0 - 2026-07-24

- Add a conditional GPT Image 2 visual-source policy for new UI surfaces.
- Preserve one approved visual baseline across later project screens and prompts.
- Use `Product Design:image-to-code` as the preferred translation and QA provider
  while Jarvis retains product and delivery ownership.
- Add same-viewport comparison, product-truth boundaries, and visual-source fields
  to the Slice Packet.
- Add behavior evaluations for generation, reuse, source priority, and hallucinated
  functionality.

## 0.2.0 - 2026-07-24

- Replace four public skill entry points with one `jarvis` skill.
- Move product, solution, and build guidance into internal capability modules.
- Add Slice Contract and Slice Packet context boundary.
- Add product validation and delivery budget policies.
- Add evidence freshness and side-effect idempotency policies.
- Replace YAML state template with validated JSON state and reconciliation CLI.
- Consolidate behavior evaluations and add positive/negative trigger fixtures.
- Treat skill size as a review signal instead of a validation failure.

## 0.1.0 - 2026-07-24

- Establish initial four-skill feedback-control foundation.
- Add Golden Paths, Feature Recipes, packaging, structural validation, and CI.
