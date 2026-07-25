# Hierarchical Context Compilation Design

## Outcome

Extend Jarvis so a frontier model can understand and plan a multi-page product,
while a smaller implementation model can complete one bounded delivery unit from
one self-contained context packet.

Success means:

- Jarvis preserves one coarse, traceable product map for the whole effort;
- each page has a stable contract describing its product role and boundaries;
- the active page or smaller slice receives a generated execution packet with
  the least sufficient transitive context;
- an implementation worker does not need the full roadmap, conversation, or
  unrelated page specifications;
- upstream changes make affected packets detectably stale;
- every material requirement can be traced through task, code, claim, and fresh
  evidence;
- existing routine and non-UI Jarvis work remains lightweight.

## Assumptions

- A page is the default planning unit for UI-heavy products, but not the only
  delivery unit. A cross-page journey, shared contract, service, migration, or
  bounded page state may be the correct unit.
- Product Map and Page Contract are authored or approved planning truth.
- Page Execution Packet is a generated materialized view, not an independently
  maintained source of truth.
- Markdown remains the human- and model-facing format. Small structured metadata
  blocks provide stable IDs, revisions, dependencies, and validation inputs.
- Jarvis remains the only owner of the project goal, global state, authority,
  integration, and final acceptance.
- Existing Slice Packet and Delegated Task Packet concepts should evolve rather
  than be replaced by another workflow system.

## Design principles

### Three logical levels, two authored levels

The planning model has three logical levels:

1. Product Map: whole-product outcomes, journeys, inventory, shared contracts,
   dependencies, and risks.
2. Page Contract: one page's job, states, actions, data, navigation, visual truth,
   dependencies, and page-level claims.
3. Page Execution Packet: generated context for one active delivery unit.

Only the first two are canonical authored specifications. The third is compiled
from them and current repository truth. This avoids three manually synchronized
copies of the same facts.

### Least sufficient dependency closure

An execution packet does not contain all project context. It contains the
smallest dependency closure needed to implement and verify its declared claims:

- relevant Product Truth and Visual Truth;
- the active Page Contract or slice contract;
- referenced shared contracts and material decisions;
- current source files, local patterns, and integration seams;
- ownership, authority, budget, and verification boundaries.

Unrelated pages, completed-slice history, full logs, secrets, and private
reasoning stay outside the packet.

### Explicit provenance and invalidation

Every compiled packet records its source artifact revisions and content hashes.
If an input changes, Jarvis marks the packet stale in the artifact index before
dispatch or acceptance. Packet content remains immutable after generation; a
changed input produces a new packet revision.

### Claims, not document completion

Artifacts organize context. They do not prove product behavior. Completion still
depends on fresh evidence for named product, functional, visual, quality, or
release claims.

## Artifact model

### Product Map

The Product Map is the coarse global control artifact for a substantial product
effort. It is durable only when recovery, coordination, or downstream context
compilation needs it.

Required content:

- stable product identifier and revision;
- goal, value hypothesis, and product-level success claims;
- target users and core jobs when material;
- journey inventory and relationships;
- page or delivery-unit inventory;
- critical path and dependency graph;
- shared Product Truth, Visual Truth, and global invariants;
- shared API, data, authorization, and design-system contract references;
- material decisions, assumptions, authority limits, and risks;
- status of each page or delivery unit without its detailed implementation plan.

The Product Map must stay coarse. It must not preselect future helper names,
component splits, algorithms, or ordinary file-level implementation details.

Illustrative metadata:

```yaml
artifact: product-map
id: PRODUCT-CRM
revision: 12
status: approved
goal: Let sales staff complete the lead-to-deal journey.
journeys:
  - JOURNEY-LEAD-TO-DEAL
pages:
  - PAGE-DASHBOARD
  - PAGE-LEAD-LIST
  - PAGE-LEAD-DETAIL
shared_contracts:
  - CONTRACT-AUTH-001
  - CONTRACT-LEAD-API-002
  - CONTRACT-DESIGN-SYSTEM-001
```

### Page Contract

A Page Contract is the canonical product and interaction contract for one page.
It explains what the page must accomplish without freezing reversible code
details too early.

Required content:

- stable page identifier, revision, status, and owning journey;
- page job and observable result;
- route, entry conditions, exit paths, and navigation relationships;
- permitted users and authorization behavior;
- real content and data requirements;
- actions and their success or failure behavior;
- reachable loading, empty, partial, error, disabled, and permission states;
- responsive platform and viewport requirements when material;
- approved visual source and must-preserve constraints when visual fidelity
  applies;
- referenced shared contracts and page dependencies;
- in-scope and out-of-scope behavior;
- page-level claims and acceptance criteria;
- unresolved high-cost decisions or authority blockers.

Illustrative metadata:

```yaml
artifact: page-contract
id: PAGE-LEAD-LIST
revision: 5
status: approved
belongs_to:
  - JOURNEY-LEAD-TO-DEAL
depends_on:
  - CONTRACT-AUTH-001@3
  - CONTRACT-LEAD-API-002@7
  - CONTRACT-DESIGN-SYSTEM-001@4
entry_points:
  - PAGE-DASHBOARD
exit_points:
  - PAGE-LEAD-DETAIL
claims:
  - CLAIM-LEAD-LIST-001
  - CLAIM-LEAD-LIST-002
```

Page Contract is not mandatory for a routine page edit whose behavior and local
pattern are already clear. Jarvis creates it when the page is new, materially
different, delegated across contexts, or likely to require durable recovery.

### Page Execution Packet

Page Execution Packet is the self-contained, generated context supplied to an
implementation model. It represents one active delivery unit, which may be a
whole page or a smaller coherent page slice.

Required metadata:

- packet ID, schema version, generated time, and immutable packet revision;
- target page and delivery-unit identifiers;
- Product Map and Page Contract revisions;
- every compiled input with path or stable ID, revision, and content hash;
- generation result: `ready` or `blocked`;
- lifecycle status in the artifact index: `ready`, `dispatched`, `stale`,
  `completed`, or `superseded`;
- owned write paths, allowed read references, and do-not-touch boundaries;
- dependency and integration relationships;
- authority, side-effect, dependency, and budget limits;
- selected implementation and verification skills;
- claims and exact verification expectations.

Required body content:

- why the unit matters and its observable result;
- complete in-scope behavior and explicit exclusions;
- relevant Product Truth and Visual Truth;
- material shared contract excerpts with provenance;
- API requests, responses, errors, and state lifecycle needed by this unit;
- current relevant files and nearby working patterns;
- approved source, viewport, assets, tokens, components, adjacent boundaries,
  and must-not-invent rules when visual fidelity applies;
- ordered implementation path where each step names its observable change and
  proof;
- replanning and `needs-context` triggers;
- required handback shape.

Illustrative metadata:

```yaml
artifact: page-execution-packet
schema_version: 1
id: PACKET-PAGE-LEAD-LIST-20260725-03
revision: 3
page_id: PAGE-LEAD-LIST
delivery_unit: SLICE-LEAD-LIST-FILTERING
status: ready
generated_at: 2026-07-25T14:30:00+08:00
derived_from:
  - ref: product/product-map.md
    revision: 12
    hash: sha256:4d967c2f...
  - ref: product/pages/lead-list/page-contract.md
    revision: 5
    hash: sha256:81fc31ab...
ownership:
  write_paths:
    - src/features/leads/list/**
  read_refs:
    - src/features/leads/detail/**
    - src/components/table/**
  do_not_touch:
    - src/auth/**
    - src/api/generated/**
```

## Delivery-unit selection

Jarvis uses a page as the default unit only when the page is independently
understandable, implementable, and verifiable. It selects a smaller vertical
slice when one page combines materially different concerns, such as static UI,
validation, quotation, payment submission, and production side effects.

Jarvis may instead select a cross-page journey when splitting by page would hide
the actual observable claim, such as registration across identity entry, email
verification, session creation, and first authenticated navigation.

Valid delivery-unit kinds include:

- page;
- page state or page capability;
- user journey;
- shared UI component;
- API or data contract;
- service or integration;
- migration or release boundary.

The packet schema remains common across kinds. Page-specific fields activate
only when the unit is a page or page slice.

## Context compiler

### Inputs

The compiler reads only sources required by the selected unit:

- current Product Map;
- active Page Contract or non-page slice definition;
- referenced shared contracts and material decisions;
- approved visual sources and implementation-relevant visual records;
- current repository files and nearby patterns;
- repository instructions and selected skill constraints;
- applicable authority, budget, side-effect, and verification policy.

### Compilation

The compiler:

1. resolves stable references and revisions;
2. computes the transitive closure of material dependencies;
3. rejects unresolved required references;
4. extracts only requirements and constraints consumed by the active claims;
5. adds current local repository truth and ownership boundaries;
6. produces ordered implementation and verification context;
7. records hashes for every durable input;
8. validates completeness, contradictions, size, and dispatch readiness;
9. emits a packet without changing its canonical sources.

Compilation may use a capable model for semantic selection, but deterministic
code owns reference resolution, hashes, schema validation, and stale detection.
Generated semantic summaries retain their source IDs so a reviewer can inspect
the canonical text.

### Context budget

The compiler treats context size as a budget, not a target. If the least
sufficient packet becomes too large or mixes independent claims, Jarvis splits
the delivery unit. It must not delete authorization, shared-contract, failure,
or verification context merely to fit a smaller model.

### Validation

A packet is `ready` only when:

- all required references resolve;
- recorded hashes match current inputs;
- no included requirement contradicts its canonical source;
- ownership and do-not-touch boundaries are explicit;
- each success claim has a falsifying check or an explicit missing-evidence
  declaration;
- dependencies and integration outputs are named;
- no secret, unrelated history, or unauthorized side effect is included;
- the selected model can reasonably execute the bounded unit.

## Dependency and stale-state model

Jarvis maintains a compact artifact index and dependency graph when durable
multi-page work needs them.

Example relationships:

```text
PRODUCT-CRM
  contains PAGE-LEAD-LIST

PAGE-LEAD-LIST
  depends_on CONTRACT-AUTH-001@3
  depends_on CONTRACT-LEAD-API-002@7
  verified_by CLAIM-LEAD-LIST-001

PACKET-PAGE-LEAD-LIST-03
  derived_from PAGE-LEAD-LIST@5
  derived_from CONTRACT-LEAD-API-002@7
```

An upstream change invalidates only downstream packets whose recorded dependency
revision or hash changed. The artifact index records those immutable packets as
stale; their files are not rewritten. Changing an unrelated page does not
invalidate the active packet. Changing a shared API contract invalidates every
dependent packet that consumes the changed behavior.

Staleness is checked:

- before dispatch;
- after a worker requests additional context;
- before integration acceptance;
- when resuming from durable state.

Evidence freshness remains separate. A packet can be current while its evidence
is missing, or stale while old evidence still exists but no longer supports the
current claim.

## Traceability

Material artifacts and claims use stable IDs. Recommended namespaces:

```text
GOAL-*
JOURNEY-*
PAGE-*
REQ-*
DECISION-*
CONTRACT-*
SLICE-*
PACKET-*
TASK-*
CLAIM-*
EVIDENCE-*
```

The intended trace is:

```text
Goal -> Journey -> Page -> Requirement -> Delivery Unit -> Task
     -> Code Change -> Claim -> Evidence
```

Not every local implementation detail receives an ID. IDs apply when reversal,
dependency analysis, durable recovery, delegation, or evidence attribution needs
them.

## Model routing and authority

The controller or frontier planning model owns:

- requirement interpretation and product direction;
- Product Map and Page Contract creation or amendment;
- shared contracts and cross-page decisions;
- delivery-unit selection and dependency ordering;
- packet compilation and dispatch readiness;
- integration, evidence reconciliation, and final acceptance.

An implementation model owns only the packet's bounded change. It may inspect
allowed repository paths, implement the declared claims, run specified checks,
and return evidence. It may not silently change Product Truth, Visual Truth,
shared contracts, authority, scope, or global state.

Model size is selected from task properties, not a permanent label. Routine,
well-specified, reversible implementation can use a smaller model. Shared,
ambiguous, security-sensitive, financial, migration, production, or disputed
work remains with a capable model regardless of packet size.

## Worker handback and missing context

Workers return one of:

- `done`: all in-scope claims implemented and declared checks run;
- `partial`: useful bounded work completed, remaining work explicit;
- `needs-context`: implementation cannot safely continue without one named
  missing input or decision;
- `blocked`: external dependency, authority, or environment prevents progress.

A `needs-context` handback includes:

```yaml
status: needs-context
missing:
  - CONTRACT-LEAD-API-002 does not define expired-cursor behavior.
blocked_claims:
  - CLAIM-LEAD-LIST-002
safe_work_completed:
  - Static page structure and non-paginated loading state.
requested_context:
  - Pagination error response and recovery behavior.
```

Jarvis resolves the missing source, updates canonical truth when needed, compiles
a new packet revision, and redispatches. The worker must not guess a shared or
hard-to-reverse contract.

All handbacks also include changed files, checks with actual results, assumptions
or decisions, evidence, side effects, and remaining risk. Worker completion is
input to Jarvis acceptance, not final acceptance itself.

## Relationship to existing Jarvis artifacts

The existing concepts remain valid:

- Delivery state remains the durable controller state.
- Slice Packet evolves into the generated Execution Packet shape for substantial
  active work.
- Delegated Task Packet remains a smaller dispatch view derived from an Execution
  Packet when only part of the unit is delegated.
- Product Truth, Visual Truth, implementation choice, and evidence remain
  separate truth boundaries.
- Existing direct routine workflow bypasses durable artifacts when no consumer
  needs them.

The design adds two explicit canonical planning artifacts, Product Map and Page
Contract, plus deterministic provenance and invalidation around the existing
packet model. It does not introduce another controller, orchestration runtime, or
mandatory document chain for every change.

## Proposed durable layout

```text
project-state/
  current.json
  artifact-index.json
  dependency-graph.json

product/
  product-map.md
  contracts/
    auth.md
    design-system.md
    lead-api.md
  pages/
    lead-list/
      page-contract.md
    lead-detail/
      page-contract.md

packets/
  page-lead-list/
    0003.md

evidence/
  lead-list/
    latest.json
```

Only files with real recovery, delegation, review, or automation consumers are
persisted. A routine Packet may remain in the active conversation.

## Failure handling

- Missing Product Map for substantial multi-page work: create the smallest coarse
  map before page planning.
- Missing Page Contract for a new or materially different page: resolve page
  product truth before compilation.
- Unresolved shared reference: block only dependent claims and request or derive
  the missing contract.
- Stale input hash: refuse dispatch or acceptance and recompile.
- Packet too large: split the delivery unit without dropping safety or contract
  context.
- Contradictory canonical sources: keep the conflict visible and return it to the
  controller; do not choose silently during compilation.
- Repository changed after compilation: compare recorded relevant file identity
  before integration, then recompile or reverify affected claims.
- Worker crosses ownership: reject or isolate the out-of-scope change before
  acceptance.
- Repeated repair failure: reclassify the cause and return to Page Contract,
  shared contract, or product decision instead of adding patches.

## Evaluation strategy

Every new behavioral rule receives a discriminating scenario. Required scenario
families:

1. Multi-page product creates a coarse Product Map and page inventory without
   detailing every future implementation.
2. One page receives a Page Contract containing its journey role, states,
   dependencies, and claims.
3. A small-model worker receives one self-contained packet and no unrelated
   roadmap or history.
4. A shared API revision marks only consuming page packets stale.
5. An unrelated page revision does not invalidate the active packet.
6. Packet compilation rejects an unresolved authorization contract.
7. Packet size pressure causes slice decomposition instead of deleting critical
   context.
8. A worker returns `needs-context` rather than inventing shared behavior.
9. Page-level completion remains unaccepted when cross-page journey evidence is
   missing.
10. Visual section packets retain full-page and adjacent-boundary context.
11. Routine established-page edits bypass the three-level durable artifact flow.
12. A high-risk page cannot be routed to a small model solely because its packet
    is compact.

Structural tests should validate schemas, references, hashes, dependency edges,
status transitions, and packaging. Behavioral comparisons remain necessary
before claiming that model tiering improves delivery cost, time, or quality.

## Compatibility and migration

Existing Jarvis users and state files continue to work. New fields must be
optional until a durable multi-page effort activates hierarchical compilation.
Existing Slice Packets can be treated as ad hoc execution packets without
provenance until regenerated.

Migration must not rewrite existing project artifacts automatically. Jarvis can
create Product Map and Page Contract from current approved truth when a live
project first needs compilation, then ask only about product-direction conflicts
that cannot be resolved from local evidence.

## Non-goals

- replacing Git, issues, or project-management systems;
- persisting every conversation decision;
- assigning IDs to local variables, helpers, or ordinary code details;
- copying the full Product Map into every page packet;
- making page boundaries mandatory for backend or cross-page work;
- guaranteeing that a small model can execute ambiguous or high-risk work;
- introducing vector retrieval as a source of product truth;
- building a general workflow runtime or distributed scheduler;
- requiring Product Map, Page Contract, and Packet for routine one-step edits.

## Acceptance criteria

The design is implemented successfully when:

- a substantial multi-page request can produce one coarse Product Map and one
  approved Page Contract for the active page;
- Jarvis can compile a schema-valid self-contained Execution Packet from those
  artifacts and current local truth;
- the packet records deterministic provenance and becomes stale when a consumed
  source changes;
- a bounded worker can implement from the packet and return a valid handback
  without receiving the whole product context;
- Jarvis can trace an active page claim back to its requirement and forward to
  current evidence;
- routine work still takes the direct path without mandatory artifacts;
- repository validation, packaging checks, unit tests, and new behavior scenarios
  pass without unsupported claims about real-world model performance.
