# Planning Policy

Treat plans as adaptive memory for the goal, not prerequisites for action. Keep
global truth coarse, explain only the current work in enough detail to act, and
let evidence reshape future detail.

## Choose the lightest planning depth

Routine edits may remain in conversation and code when nearby behavior and
repository patterns already make the change obvious. Do not create three
documents for copy, spacing, static configuration, or one contained fix.

Use hierarchical planning when work spans multiple pages, journeys, shared
rules, capabilities, or delivery sessions and those layers have real consumers.
For UI products, the available shape is:

```text
Product Plan
  -> Page Overview when durable page truth needs its own consumer-facing source
  -> Development Guide
  -> implementation
  -> verification and handback
```

Product Plan and Development Guide are available durable layers when they have
real consumers. Page Overview is optional. No layer exists merely because every
page is expected to produce the same document set.

## Compile work at the useful horizon

Before substantial multi-unit execution, compile the request into three depths:

```text
Final objective
  -> active domain or journey
  -> current coherent delivery unit
```

Keep the final objective stable enough to preserve scope, proof, authority, and
stop conditions. Give the active domain enough shape to batch related discovery,
implementation, fixtures, and verification without repeatedly rebuilding the
same context. Compile the current unit into an observable result, non-goals,
dependencies, acceptance claims, and evidence targets before material execution.

This is progressive compilation, not an exhaustive task tree. Keep inactive
domains and distant units coarse until evidence, dependency order, or a real
downstream consumer makes them active. Recompile the affected domain when user
direction or observation changes product truth; do not preserve stale subtasks
merely because they were listed earlier.

## Refine plans progressively from evidence

Begin with the goal, protected boundaries, current truth, costly unknowns, and
nearest proof gap in active context. Expand only the decision or slice needed to
select and execute the next move. Keep future pages, data, architecture, and
implementation as coarse hypotheses until a dependency, consumer, or evidence
makes them active.

More detail is not more confidence. Prefer a reversible probe when evidence can
resolve an expensive assumption faster than prose. When observation contradicts
the plan, update or retire the invalid assumption and refresh only affected
downstream context; do not preserve sunk planning.

Page is the default UI boundary, not a universal unit. A Development Guide may
instead cover a coherent page state, cross-page journey, shared component, API,
service integration, migration, or release boundary when that is the smallest
independently understandable and acceptable result.

## Level 1: Product Plan

Suggested path:

```text
docs/product-plan.md
```

The Product Plan owns product-wide truth:

- product goal, users, and core jobs;
- journeys and page inventory;
- page relationships and delivery priority;
- shared business, data, API, and authority rules;
- approved visual direction and sources;
- product-level acceptance;
- assumptions and unresolved product decisions.

Keep it coarse. Do not prematurely choose future component names, helpers,
ordinary file splits, or implementation algorithms.

## Optional Level 2: Page Overview

Suggested path:

```text
docs/pages/<page-name>/overview.md
```

Create a Page Overview when durable page truth will be consumed beyond one
implementation document, including when:

- one page will have multiple independent Development Guides;
- product, design, test, review, or maintenance roles need a stable page source;
- the page has complex states, permissions, entry and exit contracts, or
  cross-page behavior;
- the page will receive repeated implementation cycles;
- repeatedly compiling page truth into guides risks drift.

Omit Page Overview when a simple page has one current guide, one implementation
cycle, no separate reviewer or designer consumer, and enough page definition in
Product Plan to compile the guide safely. Add it later when a second consumer,
guide, or durable iteration appears.

When present, Page Overview owns durable page truth:

- page purpose and place in the journey;
- entry, exit, users, and permissions;
- content, data, actions, and complete states;
- responsive, platform, and visual structure;
- shared dependencies;
- in-scope and out-of-scope behavior;
- page-level acceptance and remaining uncertainty.

It should remain useful as a product and interaction document after one
implementation task ends. Avoid freezing reversible code details too early.

## Level 3: Development Guide

Suggested path:

```text
docs/pages/<page-name>/development.md
```

The Development Guide is the compiled implementation context for the current
page or delivery unit. It owns the current interpretation of approved product
and page truth against the present repository:

- current goal and explicit non-goals;
- necessary product and journey background;
- complete behavior, states, and failure handling;
- consumed data and API details;
- permissions and side-effect limits;
- visual and interaction constraints;
- existing code and patterns to reuse;
- suggested change area and do-not-change area;
- implementation guidance without speculative internals;
- acceptance criteria and exact verification expectations;
- conditions that require `needs-context`.

When Page Overview is omitted, the guide also contains page purpose, journey
position, entry and exit, complete page behavior, states, permissions, and page
acceptance. This is deliberate compilation, not a requirement to create a hidden
Overview first.

The worker normally receives this guide, repository instructions, and relevant
code. It should not need the Product Plan, Page Overview, planning conversation,
or unrelated page documents.

## Truth ownership and controlled repetition

Lower levels may specialize and restate upstream truth but may not silently
change its meaning:

- Product Plan or a dedicated shared document owns product-wide and shared truth.
- Page Overview owns durable behavior for one page when that optional document
  exists.
- Development Guide owns current implementation interpretation and local facts.

Without Page Overview, Product Plan owns the page's concise product role and the
Development Guide contains the complete current page behavior. If that behavior
later gains another consumer or independent guide, extract its durable parts into
Page Overview rather than maintaining competing Development Guides.

Restate any critical upstream fact whose omission could cause wrong or unsafe
implementation. Name or link its source near the relevant text. Links alone are
not enough when a worker must know the rule to complete the current task.

Do not copy complete roadmaps, unrelated pages, full design systems, unused API
operations, chat history, logs, secrets, or private reasoning. Create a separate
shared document only when a real contract has multiple current consumers or a
downstream consumer needs an independently maintained source of truth.

If documents conflict, the worker returns `needs-context`; it does not decide
which product rule wins.

## Context-closure check

Before dispatch, review the Development Guide as a fresh reader who cannot see
upstream planning. Using only the guide and named repository context, the reader
must be able to answer:

- What observable result must this work produce?
- What is outside the task?
- What behavior, states, data, APIs, permissions, and side-effect limits apply?
- Which code and patterns should be reused or changed?
- Which areas must remain untouched?
- How does each acceptance criterion map to implementation and verification?
- Which uncertainty or boundary requires `needs-context`?

Repository code may supply implementation facts. It may not substitute for a
missing product, authority, or shared-contract decision.

For an important or unfamiliar worker boundary, run a read-only dry run before
coding. Ask a fresh model to restate goal and non-goals, identify expected and
protected change areas, outline implementation, map acceptance to verification,
and report missing or conflicting context. Improve the guide when this fails;
do not add orchestration machinery first.

Use the [Lead Operations Golden Example](../examples/lead-operations/README.md)
as a reference for controlled repetition and one context-closed active page. It
is a teaching and evaluation fixture, not a mandatory workflow stage.

## Prepare only the active detail

1. Understand the product goal and resolve only direction-level ambiguity.
2. Decide whether a Product Plan has a real cross-unit, cross-session, or
   downstream consumer; write or refresh it only then.
3. Identify only enough of the core journey, likely page inventory, shared
   rules, and priority to choose the active unit.
4. Decide whether the current page has a real Page Overview consumer. Write or
   refresh one only when the optional-layer criteria apply.
5. Select the current valuable page or coherent delivery unit.
6. Inspect linked sources and current repository patterns.
7. Write or refresh its Development Guide only when implementation, delegation,
   review, or recovery has a durable reader. Otherwise keep the same bounded
   context active without creating a document.
8. Run the context-closure check before dispatch and proceed only when
   decision-ready.
9. Verify the result, integrate it, and route durable discoveries upstream.
10. Refresh the next active guide instead of fully detailing all future work.

## Split by coherent claims, not size

Keep one guide when it describes one coherent outcome, even if long. Split when
one guide mixes independently acceptable goals, unrelated risks, unstable shared
contracts, conflicting ownership, or context too broad for reliable execution.

Do not use fixed word, token, pixel, file, or component thresholds. Each slice
retains all context needed for its own result; it must not require the worker to
reconstruct product meaning from sibling slices.

Combine pages when only the cross-page journey produces the observable result.
Keep shared contract decisions with the capable model before dependent work
spreads.

## Refresh semantically before execution

Before assigning work, compare the guide with linked upstream documents,
approved visual sources, and current code. Refresh it when behavior, permissions,
API, visual truth, local patterns, or acceptance changed.

A date or status line is visible evidence of review, not automatic freshness.
V1 does not require hashes, lifecycle states, an Artifact Index, or deterministic
stale detection.

## Feed implementation discoveries back

Route a discovery to the narrowest durable owner:

- local implementation fact: Development Guide or handback;
- durable page behavior with multiple consumers: Page Overview, then refresh its
  Development Guides;
- single-use page behavior: keep it in active context or an existing Development
  Guide until another consumer justifies extracting an Overview;
- shared or product-wide rule: Product Plan or shared source, then refresh every
  affected page guide.

Do not promote every code detail into planning. Move facts upstream only when
they affect future understanding, reuse, acceptance, authority, or shared
behavior.

## Artifacts and automation

Documents remain human-readable and Git-versioned. Stable headings and ordinary
source links support review, search, and model interpretation without turning
Markdown into a machine schema.

Add automation only after repeated observed pain. A recurring missed refresh may
justify a reminder; recurring document-shape failures may justify a heading
check; recurring boundary violations may justify focused diff validation. Do not
prebuild packet runtimes, dependency databases, model routers, or mandatory
worktree systems.
