# Document-First Hierarchical Planning Design

## Outcome

Let a capable model understand and plan a whole product, then express that
understanding as progressively more detailed, human-readable development
documents. A smaller implementation model should normally need only the current
page's detailed development document and relevant repository code.

The final objective is working, verified software produced through:

```text
strong model plans globally
  -> strong model writes the current page clearly
  -> small model implements from that page document
  -> Jarvis verifies and integrates
  -> strong model refreshes the next page document
```

The planning documents must remain useful to humans even when no automation is
available. Models interpret the documents; documents do not exist primarily to
feed a workflow runtime.

## North Star

> Plan globally with strong models, explain locally in ordinary development
> documents, execute bounded work with smaller models, preserve human control
> through text and Git, and deliver a verified complete product.

Success means:

- the whole product remains understandable from one coarse plan;
- pages with durable truth, multiple consumers, or repeated implementation have
  a readable overview describing their product role;
- the active page has a self-contained development document;
- a smaller model can implement the page without receiving the full roadmap or
  conversation;
- humans can read, edit, review, and version every planning level;
- missing context produces an explicit request instead of invented behavior;
- Jarvis retains integration, risk control, and final acceptance;
- simple changes remain simple and do not require the full hierarchy.

## What this design is

This is a document-driven planning method:

```text
Product Plan
  -> Page Overview when needed
  -> Page Development Guide
  -> Implementation
  -> Verification and handback
```

The strong model performs the context compilation by reading upstream planning,
shared development documents, approved visual sources, and current code, then
writing the next-level document in clear language.

The detailed page guide is the compiled context. V1 does not wrap it in another
Execution Packet artifact.

## What this design is not

V1 is not:

- an Artifact Index;
- a dependency-graph database;
- a schema-first specification language;
- a hash and lifecycle engine;
- a deterministic context compiler;
- a strict multi-agent scheduler;
- a replacement for Git;
- a mandatory PRD, UX, Architecture, Epic, and Story chain;
- a requirement that every page or small edit create three documents.

Those mechanisms may be added later only when repeated real failures justify
them.

## Two core layers and one optional middle layer

Product Plan and the current Page Development Guide are the core documents for a
substantial product. Page Overview is optional. Create it only when durable page
truth has a real consumer beyond one implementation guide.

### Level 1: Product Plan

Suggested file:

```text
docs/product-plan.md
```

Primary consumers:

- user and product owner;
- Jarvis controller;
- capable planning model;
- people reviewing overall scope and priority.

Purpose:

- explain what the product is and why it should exist;
- preserve shared product and visual truth;
- show page inventory, journeys, dependencies, priority, and major risk;
- stay coarse enough that future page internals are not planned prematurely.

Recommended headings:

```markdown
# Product Plan

## Product goal

## Users and core jobs

## Core journeys

## Page inventory

## Page relationships

## Shared business rules

## Shared data and API constraints

## Permissions and authority

## Visual direction

## Delivery priority

## Product-level acceptance

## Assumptions and unresolved decisions
```

Do not put future component names, helper functions, ordinary file splits, or
implementation algorithms here.

### Optional Level 2: Page Overview

Create this document when:

- one page will have multiple independent Development Guides;
- product, design, test, review, or maintenance roles need a durable page source;
- page states, permissions, entry and exit contracts, or cross-page behavior are
  complex enough to outlive one implementation task;
- the page will receive repeated implementation cycles;
- multiple guides would otherwise redefine the same page differently.

Omit it when a simple page has one guide, one implementation cycle, no separate
page-document consumer, and enough Product Plan context to compile the guide
safely. Create it later if a second guide, consumer, or durable iteration appears.

Suggested file:

```text
docs/pages/<page-name>/overview.md
```

Primary consumers:

- user and product owner;
- capable planning model;
- designer or reviewer;
- the model preparing the detailed development guide.

Purpose:

- explain the page's role in the product and user journey;
- define page behavior, content, actions, states, dependencies, and exclusions;
- remain readable as a product and interaction document;
- avoid freezing reversible code details too early.

Recommended headings:

```markdown
# <Page Name> Overview

Status: approved
Product plan: ../../product-plan.md
Related shared documents:
- ../../shared/<relevant-document>.md

## Page purpose

## Place in the user journey

## Entry and exit

## Users and permissions

## Content and data

## User actions

## Loading, normal, empty, error, and disabled states

## Responsive and platform behavior

## Visual structure

## Shared rules and dependencies

## In scope and out of scope

## Page-level acceptance

## Remaining uncertainty
```

The header is light, human-readable metadata. It is not a machine schema.

### Level 3: Page Development Guide

Suggested file:

```text
docs/pages/<page-name>/development.md
```

Primary consumer:

- the implementation model responsible for the current page or page slice.

Secondary consumers:

- Jarvis controller;
- human developer or reviewer;
- verifier checking whether implementation matches intent.

Purpose:

- give one bounded worker everything it needs to implement the page safely;
- translate product language into concrete development guidance;
- include the relevant upstream context rather than requiring the worker to read
  the whole product plan;
- retain ordinary prose, examples, paths, and checklists familiar to developers.

Recommended headings:

```markdown
# <Page Name> Development Guide

Status: ready
Product plan: ../../product-plan.md
Page overview: optional; link ./overview.md when it exists, otherwise state why
it is omitted
Related shared documents:
- ../../shared/<api>.md
- ../../shared/<permissions>.md
- ../../shared/<design-system>.md
Last reviewed against upstream documents: <date>

## Current development goal

## Page purpose and journey position

## Entry, exit, and navigation

## Product and journey context needed for this page

## Complete expected behavior

## Page states and failure behavior

## Data and API details

## Permissions and side-effect limits

## Visual and interaction requirements

## Existing code and patterns to reuse

## Suggested change area

## Do not change

## Implementation guidance

## Acceptance criteria

## Verification

## When to stop and request more context
```

This document should be detailed enough that the implementation model normally
does not need Level 1 or the optional Level 2. When Page Overview is omitted, the
guide directly contains page purpose, journey position, entry and exit, complete
behavior, states, permissions, and page acceptance. It may still inspect
repository code, because current code is Local Truth and often contains the best
reusable pattern.

## Truth ownership and controlled repetition

Each level owns a different kind of truth:

- the Product Plan owns product-wide goals, shared behavior, authority, and
  cross-page decisions;
- the Page Overview owns durable page purpose, behavior, states, and boundaries
  when that optional document exists;
- the Page Development Guide owns the current implementation interpretation of
  those decisions against the present repository.

Without Page Overview, the Product Plan owns the concise page role and shared
truth while the detailed guide owns the complete current page behavior. If that
behavior later gains another consumer or independent guide, extract its durable
parts into Page Overview instead of maintaining competing definitions.

A lower-level document may specialize and restate an upstream rule, but may not
silently change its meaning. When a critical upstream rule is repeated so the
guide remains self-contained, name or link its source near the relevant text.
The source remains authoritative; the repeated text is the current page's
compiled explanation.

Route discoveries back to the narrowest durable source of truth:

- a local implementation fact belongs in the detailed guide or handback;
- a durable page-behavior change with multiple consumers belongs in Page
  Overview, followed by refresh of its detailed guides;
- single-use page behavior may remain in the current guide until another
  consumer justifies extracting an Overview;
- a product-wide or shared-contract change belongs in the Product Plan or the
  relevant shared document, followed by refresh of affected page documents.

If levels conflict, the implementation worker does not choose a winner. It
returns `needs-context` so the capable model can resolve the source of truth and
refresh the guide.

## Self-contained does not mean duplicated everything

The detailed guide includes all facts whose omission could cause wrong or unsafe
implementation:

- current page goal and scope;
- user-visible behavior;
- states and failure behavior;
- consumed API shapes and data rules;
- permissions and side-effect limits;
- required visual and interaction constraints;
- local patterns and relevant paths;
- explicit exclusions;
- acceptance and verification;
- conditions that require escalation.

It does not copy:

- the complete product roadmap;
- unrelated page planning;
- full design-system documentation;
- full API documentation outside consumed operations;
- historical chat and debug logs;
- secrets;
- private model reasoning;
- completed work that does not affect the current page.

Large sources remain linked. Critical rules from those sources are restated in
the detailed guide in plain language.

Do not create a shared planning document merely to shorten one page guide.
Create one when a real contract has multiple current consumers or a downstream
consumer needs an independently maintained source of truth.

## Context-closure check

Before dispatch, review the detailed guide as if the reader cannot see the
Product Plan, Page Overview, or planning conversation. Using only the guide and
the repository areas it names, a fresh implementation model should be able to
answer:

- What observable result must this work produce?
- What is explicitly outside the task?
- What behavior, states, data, APIs, permissions, and side-effect limits apply?
- Which existing patterns and code areas should be reused or changed?
- Which areas must remain untouched?
- How does each acceptance criterion map to implementation and verification?
- Which uncertainty or boundary would require `needs-context`?

The guide is context-closed when those answers are clear without asking the
worker to reconstruct product meaning from upstream documents. Repository code
may supply current implementation facts; it may not substitute for a missing
product, authority, or shared-contract decision.

## Planning flow

### Start a substantial product

1. Understand the goal and resolve only product-direction ambiguity.
2. Write or update the Product Plan.
3. Identify the core journey and page inventory.
4. Decide whether the current page has multiple Development Guides, consumers,
   complex durable behavior, or repeated iterations. Write Page Overview only
   when one of those consumers exists.
5. Select the current valuable page or smaller delivery unit.
6. Inspect relevant shared documents and current repository patterns.
7. Write or refresh that unit's detailed development guide and run the
   context-closure check.
8. Give the implementation model only the guide, repository instructions, and
   relevant code context.
9. Verify its result, integrate it, route durable discoveries to the owning
   planning level, and continue to the next unit.

### Handle a routine edit

Skip the hierarchy when nearby code and approved behavior already make the
change obvious. A small copy, spacing, or contained logic fix can remain in the
conversation and code with one focused check.

## Page is the default, not the only delivery unit

A page is a useful planning boundary for UI products, but Jarvis may write a
detailed guide for:

- one page state or capability;
- a cross-page user journey;
- a shared component;
- an API or data contract;
- a service integration;
- a migration or release boundary.

Split a page when one guide would mix unrelated risk, unstable shared contracts,
or more context than the implementation model can reliably handle. Combine
pages when only the cross-page journey produces the observable result.

Split by independently understandable and acceptable claims, not by a fixed
word, token, file, or component count. A long guide with one coherent outcome
may remain whole. A short guide that mixes independent goals or risk boundaries
should be split. Each slice must retain the relevant page context rather than
requiring the worker to reconstruct it from sibling slices.

## Model responsibilities

### Capable planning model

Owns:

- requirement interpretation and product direction;
- Product Plan and optional Page Overview;
- shared contract and cross-page decisions;
- preparation and refresh of the detailed development guide;
- ambiguous, shared, high-risk, or hard-to-reverse work;
- integration and final acceptance.

### Smaller implementation model

Owns:

- implementation inside the detailed guide's boundary;
- reuse of named local patterns;
- focused tests and observations;
- a truthful completion summary;
- explicit `needs-context` when the guide and repository are insufficient or
  conflict.

It may not silently redefine product behavior, shared contracts, permissions,
visual truth, authority, or scope.

### Jarvis controller

Owns:

- the current goal, critical path, and next delivery unit;
- choosing whether a smaller model is appropriate;
- making sure the detailed guide is current enough before dispatch;
- checking worker changes and evidence;
- continuous cross-page integration;
- distinguishing page, journey, product, visual, quality, and release completion.

## Human control and traceability

V1 uses ordinary document practices:

### Git history

Git records who changed a plan, what changed, when it changed, and permits
review and rollback.

### Explicit source links

Each Page Overview links to its Product Plan and shared documents. Each detailed
guide links to its Product Plan, optional Page Overview when present, and
relevant shared documents. When Overview is omitted, the guide states why and
contains the required page purpose, journey, entry, exit, behavior, and states.

### Stable headings

Fixed headings make documents predictable for humans, models, and simple text
search without turning Markdown into a rigid schema.

### Simple impact search

When a shared document changes, Jarvis can search page documents that reference
it, for example:

```powershell
rg "shared/lead-api.md" docs/pages
```

### Refresh before execution

Before assigning a page, the capable model compares the detailed guide with its
linked upstream documents and current code. It updates the guide if behavior,
permissions, API, visual truth, or local patterns changed.

V1 does not promise automatic stale detection. It promises a visible refresh
step using readable sources and Git evidence.

The existing optional `project-state/current.json` may still support interrupted
delivery. It is controller state, not another planning level.

## Visual planning

For new page families, the Product Plan records product truth and the approved
Image 2 design board establishes visual direction. Page Overview explains page
anatomy, content, actions, and states when those facts need a durable page-level
consumer. Otherwise the detailed guide contains them directly. In both cases the
guide links the approved source and restates implementation-relevant constraints.

Generated visual controls or copy do not become product requirements unless
accepted into the readable planning documents. Small established-system edits do
not require a new design board.

## Execution and handback

The implementation model returns a short development summary rather than a
mandatory machine protocol:

```markdown
## Completed

## Changed files

## Checks and actual results

## Decisions or assumptions discovered

## Acceptance criteria covered

## Remaining risk or incomplete work

## Context requested
```

Jarvis checks the actual diff and verification result. Worker completion is
input to acceptance, not acceptance itself.

When information is missing, the worker returns `needs-context` and names:

- the missing rule or contract;
- the blocked behavior;
- safe work already completed;
- the smallest additional decision or document needed.

The capable model updates the correct planning document and refreshes the
detailed guide. The worker does not guess shared behavior.

### Reverse feedback

Implementation is also a source of evidence about the plan. The handback should
name material differences between documentation and current code, unexpected
dependencies, and newly discovered shared constraints. Jarvis decides whether
the finding is only local implementation detail or changes durable page or
product truth, then updates the owning document before preparing later work.

This feedback does not make every code detail part of planning. Only facts that
affect future understanding, reuse, acceptance, authority, or shared behavior
move upstream.

## Brownfield projects

For an existing repository, inspect routes, screens, API and data models,
authorization, shared components and tokens, tests, existing documentation, and
working journeys.

Treat findings as:

- observed: present in current code or documentation;
- approved: confirmed product or visual truth;
- inferred: plausible but not confirmed;
- unknown: cannot be established safely.

Observed implementation is not automatically correct Product Truth. Ask only
when inferred or unknown behavior would materially change the product, authority,
or a hard-to-reverse shared contract.

## Risk and escalation

Use a smaller implementation model only when behavior, ownership, dependencies,
and verification are clear and the work is reversible.

Keep work with the capable model when:

- two interpretations create materially different user experiences;
- a shared contract must change;
- permissions, security, money, migration, production data, publishing, or
  destructive effects are involved;
- the same failure cause repeats twice;
- the guide conflicts with repository truth;
- the required context remains too large after coherent slice splitting;
- page completion changes a journey-level contract.

Merely consuming an existing shared component or API does not require
escalation. Escalate when the work would redefine shared behavior, change a
contract for other consumers, or make the page impossible to verify in
isolation.

## V1 proof

Use a small Lead Operations fixture with Dashboard, Lead List, and Lead Detail.
The active guide covers Lead List loading, owner and status filters, loading,
empty, error and retry states, and navigation to Lead Detail.

### Golden example

Create one complete, human-readable reference set:

```text
docs/product-plan.md
docs/pages/lead-list/overview.md
docs/pages/lead-list/development.md
```

The example should demonstrate controlled repetition, source ownership,
context closure, explicit boundaries, acceptance mapping, and useful
`needs-context` conditions. Brief annotations may explain why important context
is present and why unrelated context is absent. The example is a teaching and
evaluation fixture, not a mandatory template runtime.

### Read-only dry run

Before asking a smaller model to write code, give a fresh model only the Lead
List development guide and the repository areas it names. Ask it to return:

- its own restatement of the goal and non-goals;
- expected change areas and protected areas;
- a proposed implementation sequence;
- a mapping from acceptance criteria to behavior and verification;
- missing or conflicting context;
- whether the task should remain local or be escalated.

Failure at this stage means the guide or task boundary needs improvement. Do
not compensate first with more orchestration machinery.

### Implementation comparison

The proof asks one question:

> Can a smaller model complete the same bounded page claims from the detailed
> development guide without receiving the full product plan and conversation?

Evaluation may compare:

```text
A: capable model with broader planning context
B: capable model with the detailed guide only
C: smaller model with the same detailed guide
```

This comparison is an evaluation technique, not part of normal project
execution. Record accepted claims, checks, changed paths, rework, intervention,
tokens, time, and total cost. Do not build an Artifact Runtime merely to conduct
the experiment.

Include discriminating cases that can prove the rules matter:

- a self-contained local page change that should proceed without escalation;
- an omitted permission or error-state rule that the read-only test should
  identify as missing context;
- a shared component reused without changing its behavior, which should remain
  local;
- a shared API or component contract change that should be escalated;
- a code-versus-document conflict that should produce `needs-context` and an
  upstream refresh;
- a coherent long page task that should stay whole and a short mixed-risk task
  that should be split.

## Add automation only after repeated pain

Examples:

- repeated missed document refreshes may justify a source-change reminder;
- hard-to-find page dependencies may justify a lightweight generated index;
- recurring document-shape failures may justify a heading validator;
- recurring write-boundary violations may justify stricter diff validation;
- real parallel-worker state conflicts may justify lifecycle tracking;
- repeated context-selection failures may justify retrieval or a more structured
  compiler.

Add the smallest mechanism that fixes an observed failure. Do not prebuild all
possible controls.

## Non-goals

- machine-valid planning schemas in V1;
- JSON metadata inside every planning document;
- an Artifact Index or dependency database;
- automatic hash-based stale detection;
- deterministic semantic compilation;
- strict filesystem read isolation;
- automatic provider or model switching;
- mandatory Worktrees or parallel agents;
- exhaustive planning of every page before implementation starts;
- treating completed documents as evidence that software works.

## Acceptance criteria

The design is successful when:

- a substantial product can be understood from one readable Product Plan;
- each page with multiple guides, consumers, complex durable behavior, or
  repeated iterations can be understood from one readable Page Overview;
- a simple single-guide page may omit Page Overview when its Development Guide
  contains the complete page context;
- the active page has one detailed guide containing its least sufficient
  development context;
- each level has a clear source-of-truth responsibility, and lower levels expand
  rather than silently redefine upstream decisions;
- a fresh reader can pass the context-closure check using the detailed guide
  and named repository context;
- a bounded implementation model can implement that page from the guide and
  repository code without receiving the full roadmap or conversation;
- missing shared meaning produces `needs-context` rather than invented behavior;
- local reuse proceeds without unnecessary escalation while shared behavior,
  authority, and contract changes return to the capable model;
- implementation discoveries flow back only to the durable planning level they
  materially affect;
- humans can inspect, edit, review, search, and version the planning documents;
- Jarvis verifies actual behavior and integrates pages into a working journey;
- routine edits bypass the hierarchy;
- automation is added only in response to demonstrated recurring failure;
- the final result is verified working software, not a completed document set.
