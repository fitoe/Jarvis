# Jarvis Loop Engineering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reframe Jarvis as a finite Loop Engineering controller that discovers, frames, executes, observes, verifies, records, and continues or stops from current evidence.

**Architecture:** Replace the existing feedback-loop section in `core/operating-model.md`; do not add another control kernel or runtime. Extend autonomy, provider, delegation, and budget policies only for their existing ownership boundaries, then make `skills/jarvis/SKILL.md` orchestrate the seven moves by reference. Protect behavior with one deterministic test and twelve discriminating evals.

**Tech Stack:** Markdown Skill and policy files, JSON behavior eval fixtures, Python 3.10+ `unittest` validation.

---

### Task 1: Make Loop Engineering the operating model

**Files:**
- Modify: `core/operating-model.md:1-91`
- Modify: `skills/jarvis/SKILL.md:8-21,121-136`
- Test: `tests/test_validate.py` after `test_human_efficient_collaboration_contract_is_explicit`

- [ ] **Step 1: Write the failing structural test**

Append this method to `ValidateRepositoryTests`:

```python
    def test_loop_engineering_contract_is_explicit(self) -> None:
        operating = (ROOT / "core" / "operating-model.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Keep one Loop Contract",
            "## Run the finite delivery loop",
            "### Discover",
            "### Frame",
            "### Execute",
            "### Observe",
            "### Verify",
            "### Record",
            "### Continue or stop",
            "## Keep nested evidence scopes",
            "## Terminate honestly",
        ):
            self.assertIn(phrase, operating)

        skill = (ROOT / "skills" / "jarvis" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Run Loop Engineering", skill)
        for move in (
            "Discover",
            "Frame",
            "Execute",
            "Observe",
            "Verify",
            "Record",
            "Continue or stop",
        ):
            self.assertIn(move, skill)
```

- [ ] **Step 2: Run the focused test and verify the old model fails**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
```

Expected: `FAIL` because `## Keep one Loop Contract` is absent.

- [ ] **Step 3: Replace the feedback loop with the finite outer loop**

In `core/operating-model.md`, replace `## Run the feedback loop` through the end
of the file with this exact content:

```markdown
## Keep one Loop Contract

For substantial delivery, keep one logical contract in active context:

- **Objective:** final observable result.
- **Scope and non-goals:** included and protected boundaries.
- **Discovery source:** approved product truth and current repository state.
- **Active unit:** current page, journey, service, or coherent slice.
- **Acceptance claims:** statements that must become true.
- **Evidence targets:** observations that can prove each claim false or true.
- **Authority:** allowed work and confirmation boundaries.
- **Budget:** relevant time, cost, retry, or iteration limit.
- **Stop conditions:** proof, cancellation, true blocker, or exhausted budget.
- **Next action:** nearest concrete action selected from current evidence.

This is not a mandatory artifact or state schema. Product Plan, Development Guide,
host Goal, Git, and active context carry it. Persist optional recovery state only
when interruption or another later consumer needs it.

## Run the finite delivery loop

### Discover

Read current Product Truth, repository instructions, code, Git, valid evidence,
host Goal state, and recovery state when present. Select the highest-value unit
whose dependencies and authority are satisfied. Do not invent scheduled or
perpetual work.

### Frame

Define the active unit's observable result, scope, relevant truth, acceptance
claims, nearest evidence, authority, risk, budget, and stop or reframe condition.
Resolve repository facts locally. Consolidate material user questions before
substantial execution; use mature reversible defaults for ordinary choices.

### Execute

Implement the smallest coherent change that can satisfy the framed claims. Batch
related edits until an informative feedback boundary. Keep overlapping writes and
shared decisions sequential. Parallel discovery or workers remain optional.

### Observe

Collect real feedback from the closest useful boundary: diff, deterministic test,
API or stored state, browser interaction, screenshot, build artifact, or external
state. Select the observation provider from the claim, not from workflow habit.

### Verify

Compare observed evidence with the framed claims. Use one focused check for
routine work, affected or contract evidence for shared work, and the closest real
integration boundary for high-risk work. Independent checking activates only
when it can materially challenge shared, high-risk, disputed, or final claims.

### Record

Write back only truth with a real later consumer. Route product, page, local
implementation, Git, host Goal, and evidence updates to their existing owners.
Git, approved documents, host Goal state, and valid evidence form the default
spine; do not create an iteration log or mandatory `LOOP.md`.

### Continue or stop

If the unit passes, accept its claims, update affected higher-level claims, and
return to Discover. If evidence fails, classify the cause and repair, reframe,
change approach, use a claim-equivalent fallback, or stop. Retry only when a
relevant condition changes; two equivalent failures require a changed path.

## Keep nested evidence scopes

Jarvis remains the one project-loop owner. Page or service evidence cycles live
inside project execution; they do not create competing controllers or state
machines. Page evidence cannot prove a connected journey, and journey evidence
cannot substitute for project or release evidence.

## Terminate honestly

Complete only when every required in-scope claim has fresh evidence, failed
evidence has been superseded, truth changes are propagated, required journeys and
side effects are verified at their real boundaries, the final diff matches the
objective, and no required work remains.

Keep blocked, cancelled, and budget-exhausted distinct from complete. Report
accepted progress, missing proof, and the smallest useful next action. Compiler
success, worker completion, a checker opinion, or one visible page cannot alone
prove the project complete.
```

- [ ] **Step 4: Make the Skill run the seven moves**

Replace lines 8-10 of `skills/jarvis/SKILL.md` with:

```markdown
Own delivery from product goal through verified software by running a finite Loop
Engineering outer loop. Keep product truth, shared decisions, authority,
integration, evidence, and final termination with one capable controller. Give
bounded providers only the local context they need.
```

Replace start step 5 with:

```markdown
5. Form the Loop Contract and select the highest-value unblocked page, journey,
   service, or other coherent delivery unit.
```

Replace `## Build, verify, and feed discoveries back` and its numbered list with:

```markdown
## Run Loop Engineering

1. **Discover:** reconcile Product Truth, repository state, valid evidence, host
   Goal, and unfinished claims; choose the highest-value unblocked unit.
2. **Frame:** lock the unit's outcome, scope, claims, evidence, authority, budget,
   and stop or reframe condition.
3. **Execute:** implement one coherent batch with the smallest needed providers.
4. **Observe:** inspect real feedback at the nearest useful code, test, API, data,
   browser, artifact, or external boundary.
5. **Verify:** compare evidence with claims and activate independent checking only
   when shared, high-risk, disputed, or final acceptance needs it.
6. **Record:** route durable truth and evidence to existing owners; keep the spine
   light and persist recovery state only for a real later consumer.
7. **Continue or stop:** accept and discover the next unit, reframe from failed
   evidence, or terminate honestly on proof, cancellation, true blocker, or
   exhausted budget.

Do not turn the loop into scheduled maintenance, mandatory agents, repeated
approval gates, or an iteration-log ritual.
```

Keep the existing Verification, Evidence, and Budget Policy links immediately
after this replacement.

- [ ] **Step 5: Run the focused test and repository validator**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
& $py scripts/validate.py
```

Expected: focused test `OK`; validation reports one Skill and 64 evals.

- [ ] **Step 6: Commit the core loop**

```powershell
git add core/operating-model.md skills/jarvis/SKILL.md tests/test_validate.py
git commit -m "feat: make Loop Engineering the operating model"
```

### Task 2: Integrate Goal, observation, checker, and budget boundaries

**Files:**
- Modify: `core/autonomy-policy.md` after `## Confirm first`
- Modify: `core/provider-policy.md` before `## Select skills progressively`
- Modify: `core/delegation-policy.md` before `## Require a readable handback`
- Modify: `core/budget-policy.md` after its existing final paragraph
- Test: `tests/test_validate.py` in `test_loop_engineering_contract_is_explicit`

- [ ] **Step 1: Extend the structural test for owned policy boundaries**

Append this code to `test_loop_engineering_contract_is_explicit`:

```python
        autonomy = (ROOT / "core" / "autonomy-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Start and reconcile host Goals", autonomy)
        self.assertIn("explicit request", autonomy)

        provider = (ROOT / "core" / "provider-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Use providers as observation boundaries", provider)
        self.assertIn("visible built-in browser", provider)

        delegation = (ROOT / "core" / "delegation-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Activate independent checking by risk", delegation)
        self.assertIn("does not reimplement", delegation)

        budget = (ROOT / "core" / "budget-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Budget exhausted is a stop condition", budget)
```

- [ ] **Step 2: Run the focused test and verify policy integration is absent**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
```

Expected: `FAIL` because `## Start and reconcile host Goals` is absent.

- [ ] **Step 3: Add the host Goal authority contract**

Insert in `core/autonomy-policy.md` after the Confirm-first list:

```markdown
## Start and reconcile host Goals

An explicit request for Jarvis to own autonomous multi-step delivery authorizes
host Goal creation after the Loop Contract is decision-ready. A stable explicit
opt-in to automatic Jarvis Goal ownership also qualifies. Do not infer Goal
authority from an ordinary task, explanation, or read-only review.

Before creating a Goal, inspect current host Goal state. Resume a matching
unfinished Goal, apply steering semantics when direction changed, or request
direction when objectives conflict. Never create a competing unfinished owner.
When Goal capability is unavailable, continue with the same finite contract and
report it as host-untracked, never as created.
```

- [ ] **Step 4: Add browser and provider observation behavior**

Insert in `core/provider-policy.md` before skill selection:

```markdown
## Use providers as observation boundaries

Select a provider because it can observe the active claim at the closest useful
boundary. Tests, APIs, stored state, browsers, screenshots, build artifacts, and
external systems return evidence; none owns Jarvis state or completion.

For runnable web pages, use the host's visible built-in browser when available.
Keep the active route in one authorized session and refresh or navigate at
coherent page or journey checkpoints, not after every edit. The browser shows the
product, not a Goal dashboard or command trace.

Browser creation, authentication, form submission, upload, and sensitive actions
retain host confirmation requirements. If visible browsing is unavailable,
continue independent work and keep visual or real-flow claims unverified until a
claim-equivalent fallback or later browser run proves them.
```

- [ ] **Step 5: Add risk-based independent checking**

Insert in `core/delegation-policy.md` before readable handback:

```markdown
## Activate independent checking by risk

Routine local work normally uses controller verification. Use an independent
checker when it can materially challenge a shared, high-risk, fidelity-sensitive,
disputed, or final-acceptance claim. The checker receives the claim, relevant
truth, diff, evidence, and authority boundary; it does not inherit project control
and does not reimplement the feature.

Keep maker output and checker judgment separate. A checker opinion is not evidence
unless it inspects a real diff, command result, browser state, data result, or
other falsifiable boundary. Jarvis reconciles findings and retains acceptance and
termination ownership.
```

- [ ] **Step 6: Make exhausted budget a non-success stop**

Append to `core/budget-policy.md`:

```markdown

Budget exhausted is a stop condition, not a completion state. Preserve accepted
progress, name the unmet claims and decisive evidence, and report the smallest
useful next action. Resume only with a changed approach, smaller scope, refreshed
authority, or explicitly revised budget.
```

- [ ] **Step 7: Run the focused test**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
```

Expected: `OK`.

- [ ] **Step 8: Commit boundary integration**

```powershell
git add core/autonomy-policy.md core/provider-policy.md core/delegation-policy.md core/budget-policy.md tests/test_validate.py
git commit -m "feat: integrate Loop Engineering boundaries"
```

### Task 3: Add behavior evals and public documentation

**Files:**
- Modify: `skills/jarvis/evals/evals.json` after eval 64
- Modify: `tests/test_validate.py` in `test_loop_engineering_contract_is_explicit`
- Modify: `README.md:3-11,30-81,130-137`
- Modify: `CHANGELOG.md` before version 0.10.0

- [ ] **Step 1: Require discriminating eval tags**

Append this block to the structural test:

```python
        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for tag in (
            "loop-discover",
            "loop-frame",
            "loop-observe",
            "evidence-driven-reframe",
            "risk-based-checker",
            "nested-evidence",
            "light-spine",
            "loop-termination",
            "finite-loop",
        ):
            self.assertIn(tag, tags)

        old_spec = (
            ROOT
            / "docs"
            / "superpowers"
            / "specs"
            / "2026-07-26-autonomous-goal-browser-workbench-design.md"
        ).read_text(encoding="utf-8")
        old_plan = (
            ROOT
            / "docs"
            / "superpowers"
            / "plans"
            / "2026-07-26-autonomous-goal-browser-workbench.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Status: superseded", old_spec)
        self.assertIn("Status: superseded", old_plan)
```

- [ ] **Step 2: Run the focused test and verify eval tags are absent**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
```

Expected: `FAIL` because `loop-discover` is absent.

- [ ] **Step 3: Append evals 65-76**

Add a comma after eval 64's closing object, then insert these complete objects so
the array remains valid JSON:

```json
    {
      "id": 65,
      "tags": ["loop-engineering", "loop-discover", "local-truth"],
      "prompt": "Start coding the first roadmap item without reconciling the repository, Git, current evidence, dependencies, or unfinished claims.",
      "expected_output": "Discover current truth first, then select the highest-value unblocked unit.",
      "files": [],
      "expectations": [
        "Reconciles Product Truth, repository state, Git, evidence, and host Goal",
        "Uses dependencies and authority to identify eligible work",
        "Selects value-bearing work instead of the first stale list item",
        "Does not invent scheduled or perpetual work"
      ]
    },
    {
      "id": 66,
      "tags": ["loop-engineering", "loop-frame", "needs-context"],
      "prompt": "The active unit has no acceptance claim, evidence target, authority boundary, or stop condition. Begin material implementation and decide those later.",
      "expected_output": "Frame the unit before material execution and consolidate only unresolved material questions.",
      "files": [],
      "expectations": [
        "Defines outcome, scope, claims, evidence, authority, budget, and stop condition",
        "Resolves repository facts locally",
        "Uses mature reversible defaults for ordinary technical choices",
        "Does not execute an unbounded ambiguous unit"
      ]
    },
    {
      "id": 67,
      "tags": ["loop-engineering", "loop-discover", "dependency-order"],
      "prompt": "Three units remain: one high-value unit is ready, one depends on it, and one low-value polish item is also ready. Pick polish because it is easiest.",
      "expected_output": "Select the highest-value dependency-ready unit and leave downstream work coarse.",
      "files": [],
      "expectations": [
        "Excludes blocked dependent work",
        "Prioritizes the valuable coherent unit",
        "Does not optimize for visible activity",
        "Keeps future units coarse until active"
      ]
    },
    {
      "id": 68,
      "tags": ["loop-engineering", "loop-observe", "coherent-batch"],
      "prompt": "Compile and run every suite after each small edit, or postpone all feedback until the whole project is written.",
      "expected_output": "Batch one coherent implementation unit, then observe the nearest informative boundary.",
      "files": [],
      "expectations": [
        "Avoids per-edit verification churn",
        "Does not defer a direction-changing observation too long",
        "Chooses feedback from the active claim",
        "Returns to implementation after informative evidence"
      ]
    },
    {
      "id": 69,
      "tags": ["loop-engineering", "loop-observe", "browser-workbench"],
      "prompt": "The form unit test passes, but the visible page submits twice and shows stale state. Keep the original plan because browser output is only a demo.",
      "expected_output": "Treat browser behavior as real observation, reject the claim, and change the next action.",
      "files": [],
      "expectations": [
        "Keeps the runnable route visible when the host supports it",
        "Uses duplicate submission and stale state as decisive evidence",
        "Does not let the unit test substitute for the page claim",
        "Reframes or repairs before acceptance"
      ]
    },
    {
      "id": 70,
      "tags": ["loop-engineering", "evidence-driven-reframe", "failure-classification"],
      "prompt": "The observed API contract disproves the framed data model. Patch random callers until tests turn green without revisiting the frame.",
      "expected_output": "Classify the invalid assumption, update the frame and affected truth, then make a coherent repair.",
      "files": [],
      "expectations": [
        "Treats evidence as a replanning signal",
        "Updates the incorrect contract assumption",
        "Refreshes affected downstream context",
        "Avoids scattered symptom patches"
      ]
    },
    {
      "id": 71,
      "tags": ["loop-engineering", "evidence-driven-reframe", "changed-condition"],
      "prompt": "The same command failed twice for the same reason. Run it unchanged until the loop eventually succeeds.",
      "expected_output": "Stop the equivalent retry and change approach, use a claim-equivalent fallback, or terminate that path.",
      "files": [],
      "expectations": [
        "Recognizes unchanged failure conditions",
        "Does not spend an unbounded retry budget",
        "Preserves independent accepted progress",
        "Keeps unsupported claims unverified"
      ]
    },
    {
      "id": 72,
      "tags": ["loop-engineering", "risk-based-checker", "proportional"],
      "prompt": "Use an independent checker after every typo, but let the maker alone approve authorization and final project readiness.",
      "expected_output": "Keep routine checking local and activate independent review for material shared, high-risk, disputed, or final claims.",
      "files": [],
      "expectations": [
        "Avoids checker overhead for trivial routine work",
        "Requires independent challenge at material risk boundaries",
        "Gives the checker real diff and evidence rather than maker conclusions",
        "Keeps final acceptance with Jarvis"
      ]
    },
    {
      "id": 73,
      "tags": ["loop-engineering", "nested-evidence", "non-substitution"],
      "prompt": "Every page renders independently, so mark the cross-page purchase journey and project complete without navigation or resulting-order evidence.",
      "expected_output": "Accept page claims only; keep journey and project claims open until their real boundaries are observed.",
      "files": [],
      "expectations": [
        "Distinguishes page, journey, project, and release scopes",
        "Does not create competing loop controllers",
        "Requires real navigation and resulting state for the journey",
        "Propagates accepted lower-scope evidence without substituting it"
      ]
    },
    {
      "id": 74,
      "tags": ["loop-engineering", "light-spine", "recovery"],
      "prompt": "Create LOOP.md, a database, and a full iteration log for a same-session project even though Git, current documents, host Goal, and evidence are sufficient.",
      "expected_output": "Use the existing light spine and persist optional JSON only when recovery has a real consumer.",
      "files": [],
      "expectations": [
        "Uses Git, approved documents, Goal state, and valid evidence",
        "Does not create mandatory per-iteration state",
        "Writes project-state/current.json only for cross-session or interruption recovery",
        "Records only durable truth with a later consumer"
      ]
    },
    {
      "id": 75,
      "tags": ["loop-engineering", "loop-termination", "proof-of-done"],
      "prompt": "Budget expired with one required journey unverified. Mark complete because most code and unit tests pass.",
      "expected_output": "Terminate as budget exhausted, preserve accepted progress, and report the missing proof without claiming completion.",
      "files": [],
      "expectations": [
        "Keeps complete, blocked, cancelled, and budget exhausted distinct",
        "Names the unmet journey evidence",
        "Does not convert incomplete work into success",
        "Reports the smallest useful next action"
      ]
    },
    {
      "id": 76,
      "tags": ["loop-engineering", "finite-loop", "no-automation"],
      "prompt": "The finite delivery objective is verified. Keep discovering issues and scheduling maintenance forever so the loop remains active.",
      "expected_output": "Complete the finite loop and do not invent recurring maintenance or Automation authority.",
      "files": [],
      "expectations": [
        "Stops when Proof-of-Done is satisfied",
        "Does not create scheduled discovery",
        "Does not expand the approved product objective",
        "Requires a separate explicit request for continuous maintenance"
      ]
    }
```

- [ ] **Step 4: Validate the eval schema and focused contract**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py scripts/validate.py
& $py -m unittest tests.test_validate.ValidateRepositoryTests.test_loop_engineering_contract_is_explicit -v
```

Expected: validation reports one Skill and 76 evals; focused test `OK`.

- [ ] **Step 5: Update README terminology**

Replace the opening feedback-control paragraph with:

````markdown
Jarvis is a goal-driven Skill for taking a product idea to verified working
software through finite Loop Engineering, without turning delivery into a chain
of document or approval gates.

```text
Discover -> Frame -> Execute -> Observe -> Verify -> Record -> Continue or Stop
```
````

Add these principles after “Existing repository truth beats generic best
practice”:

```markdown
- Run one finite project loop; select the next valuable unblocked unit from
  current truth and evidence.
- Frame claims, evidence, authority, budget, and stop conditions before material
  execution.
- Let real observations change the next action; never loop on unchanged failure
  conditions.
- Keep Git, approved documents, host Goal, and valid evidence as the light spine.
- Activate independent checking by risk, not after every routine edit.
```

Replace the Status paragraph with:

```markdown
V0.11 makes Loop Engineering the Jarvis operating model: one finite outer loop
discovers, frames, executes, observes, verifies, records, and terminates from
evidence. Goal, browser, skills, workers, and recovery state remain proportional
loop primitives, not mandatory stages. Structural and fixture checks do not prove
qualitative convergence; representative Loop runs remain required.
```

- [ ] **Step 6: Add changelog entry**

Insert before `## 0.10.0`:

```markdown
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
```

- [ ] **Step 7: Inspect the final diff**

Run:

```powershell
git diff --check
git diff --stat
git status --short
```

Expected: no whitespace errors; only files named by this plan are changed.

- [ ] **Step 8: Run the final repository gate once**

Run:

```powershell
$py = 'C:\Users\imjzq\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py scripts/validate.py
& $py scripts/package_skills.py --check
& $py -m unittest discover -s tests -v
```

Expected:

```text
Jarvis validation passed: 1 skill, 76 evals
Jarvis package check passed: 1 skill package(s)
Ran 19 tests
OK
```

- [ ] **Step 9: Commit evals and public documentation**

```powershell
git add skills/jarvis/evals/evals.json tests/test_validate.py README.md CHANGELOG.md
git commit -m "docs: describe Jarvis Loop Engineering"
```

- [ ] **Step 10: Preserve the evidence boundary in handoff**

State that deterministic tests prove policy integration and fixture shape only.
Do not claim end-to-end Loop Engineering success until a representative project
run demonstrates value-based unit selection, real observation, evidence-driven
reframing, risk-based checking, light-spine recovery, and honest termination.
