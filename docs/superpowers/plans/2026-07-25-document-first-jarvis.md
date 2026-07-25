# Document-First Jarvis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `executing-plans` to
> implement this plan task-by-task. Keep work in one controller; do not delegate
> unless the user explicitly asks.

**Goal:** Make Jarvis use human-readable Product Plan and Development Guide core
documents, add Page Overview only for durable multi-consumer page truth, and give
bounded workers only the current guide plus relevant repository context.

**Architecture:** Keep Jarvis as the controller and retain optional recovery
state, risk control, verification, visual policy, and final acceptance. Replace
Slice Packet and Delegated Task Packet planning with Product Plan, optional Page
Overview, and Development Guide Markdown. Put detailed rules in `core/`; keep
`skills/jarvis/SKILL.md` compact and progressively load them.

**Tech Stack:** Markdown skill instructions and templates, JSON behavior evals,
Python standard-library validation and packaging tests.

---

### Task 1: Lock the new repository contract with failing tests

**Files:**

- Modify: `tests/test_validate.py`

- [x] Add a test asserting the repository requires
  `templates/product-plan.md`, `templates/page-overview.md`, and
  `templates/development-guide.md`, and no longer requires packet templates.
- [x] Add a test asserting Jarvis instructions contain Product Plan, Page
  Overview, Development Guide, and context-closure language without Slice
  Packet or Delegated Task Packet language.
- [x] Add a test asserting eval tags cover `document-first`,
  `context-closure`, `truth-ownership`, `shared-boundary`, and
  `read-only-dry-run`.
- [x] Run:

  ```powershell
  python -m unittest tests.test_validate.ValidateRepositoryTests -v
  ```

  Expected: new tests fail because the old packet contract still exists.

### Task 2: Replace packet planning with readable hierarchical planning

**Files:**

- Modify: `skills/jarvis/SKILL.md`
- Rewrite: `core/planning-policy.md`
- Modify: `core/delegation-policy.md`
- Delete: `core/slice-contract.md`
- Modify: `capabilities/product-design.md`
- Modify: `capabilities/solution-design.md`
- Modify: `capabilities/product-build.md`

- [x] Make substantial-product startup produce or refresh a coarse Product Plan.
- [x] Make Page Overview optional: retain it for multiple guides, consumers,
  complex durable behavior, or repeated implementation cycles.
- [x] Make the current page or delivery unit use a self-contained Development
  Guide as compiled implementation context.
- [x] Define truth ownership, controlled repetition, context closure, semantic
  refresh, coherent splitting, `needs-context`, and reverse feedback.
- [x] Let routine edits bypass the hierarchy.
- [x] Give delegated workers the Development Guide, repository instructions,
  and named code context; use an ordinary Markdown handback.
- [x] Escalate shared behavior and contract changes without escalating ordinary
  reuse.

### Task 3: Replace templates and repository wiring

**Files:**

- Create: `templates/product-plan.md`
- Create: `templates/page-overview.md`
- Create: `templates/development-guide.md`
- Delete: `templates/active-slice.md`
- Delete: `templates/slice-packet.json`
- Delete: `templates/delegated-task.json`
- Modify: `scripts/validate.py`
- Modify: `scripts/package_skills.py`
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Create: `examples/lead-operations/README.md`
- Create: `examples/lead-operations/docs/product-plan.md`
- Create: `examples/lead-operations/docs/pages/lead-list/overview.md`
- Create: `examples/lead-operations/docs/pages/lead-list/development.md`

- [x] Keep templates ordinary Markdown with stable headings and light source
  links, not machine schemas.
- [x] Keep `templates/delivery-state.json` and `scripts/state.py` optional for
  interrupted delivery; state remains controller state, not a planning level.
- [x] Update required repository paths and package documentation.
- [x] Package a complete Lead Operations Golden Example for instruction and
  read-only context evaluation.
- [x] Remove live references to deleted packet resources outside historical
  specs and Changelog history.

### Task 4: Add discriminating behavior evaluations

**Files:**

- Modify: `skills/jarvis/evals/evals.json`
- Modify: `evals/README.md`

- [x] Update existing planning and delegation cases to use Development Guides.
- [x] Add cases for two-core-layer planning, optional Page Overview, context
  closure, truth conflicts,
  shared reuse versus shared contract change, coherent split decisions,
  read-only dry run, and reverse feedback.
- [x] Keep structural validation separate from claims of behavioral improvement.

### Task 5: Verify source and packaged skill

- [x] Run focused tests until green:

  ```powershell
  python -m unittest tests.test_validate.ValidateRepositoryTests -v
  ```

- [x] Run repository gates:

  ```powershell
  python scripts/validate.py
  python scripts/package_skills.py --check
  python -m unittest discover -s tests -v
  ```

- [x] Regenerate `dist/jarvis` with `python scripts/package_skills.py` and rerun
  package check.
- [x] Run `git diff --check` and search live sources for obsolete packet terms.
- [x] Report behavioral benchmark as unverified until the planned Lead List
  read-only and implementation comparisons are actually run.

No commit, push, release, or external side effect is authorized by this plan.
