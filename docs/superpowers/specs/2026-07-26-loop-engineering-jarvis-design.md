# Jarvis Loop Engineering Design

Date: 2026-07-26
Status: approved direction, pending written-spec review

## Goal

Reframe Jarvis around Loop Engineering: a finite, evidence-driven outer loop that
discovers the next valuable unit, frames its proof, executes it, observes real
feedback, verifies the result, records durable truth, and continues until the
project goal is proven complete.

Jarvis remains the public Skill and product controller. Loop Engineering becomes
its internal operating method. Host Goal creation, browser visibility, planning
documents, skills, tools, worktrees, and subagents are loop primitives selected
only when the active claim needs them.

## Industry alignment

The selected model follows the emerging 2026 meaning of Loop Engineering rather
than using the term as a rename for iterative coding. Addy Osmani describes it as
designing the system that prompts agents, discovers work, checks results, records
state, and chooses what happens next. IBM describes the inner cycle as Goal,
Action, Observation, and Adjustment, supported by scheduling, context, tools,
worktrees, skills, subagents, and a persistent spine.

Sources:

- [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/)
- [IBM: What is loop engineering?](https://www.ibm.com/think/topics/loop-engineering)

Jarvis adopts the finite delivery subset. Scheduled discovery and perpetual
maintenance loops are not part of the first implementation.

## Success criteria

- Jarvis explains and operates delivery as one finite outer loop, not a sequence
  of mandatory document or approval stages.
- The loop selects the next unblocked, valuable delivery unit from current product
  truth, repository state, and evidence.
- Every active unit has an observable result, bounded scope, evidence target,
  authority boundary, and stop or reframe condition before material execution.
- Implementation observes the closest real feedback boundary and changes its next
  action from that evidence.
- Routine work stays lightweight; independent checking activates at shared,
  high-risk, or final-acceptance boundaries where it improves trust.
- Durable state remains light: Git, approved documents, host Goal state, and valid
  evidence are the spine; JSON recovery state appears only for cross-session or
  interrupted delivery.
- The loop terminates honestly on proof, cancellation, a true blocker, or budget
  exhaustion. It never converts incomplete work into success.
- The previous automatic-Goal and browser-workbench design is absorbed into this
  model rather than implemented as a competing lifecycle.
- Every new behavioral rule has a discriminating eval scenario.

## Approaches considered

### A. Rename the existing feedback loop

Change README terminology while leaving controller behavior unchanged. This is
small but superficial: it does not define discovery, framing, state writeback,
termination, or the outer-loop relationship to host capabilities.

### B. Add a workflow runtime

Build a scheduler or state machine that owns tasks, agents, browser refresh, and
retries. This gives strong runtime control but expands Jarvis into the workflow
system it is meant to replace. It also makes routine work unnecessarily heavy.

### C. Make Loop Engineering the policy-level operating model

Reorganize the existing Jarvis control kernel around a finite outer loop. Reuse
host and repository primitives and activate them proportionally. This is selected:
it matches current industry usage while preserving Jarvis's small, portable Skill
architecture.

## Core loop

Jarvis runs seven moves:

```text
Discover -> Frame -> Execute -> Observe -> Verify -> Record -> Continue or Stop
```

### Discover

Read current product truth, repository instructions, code, Git, valid evidence,
host Goal state, recovery state when present, and uncompleted acceptance claims.
Find work from the user objective and current delivery map; do not invent a
backlog or run scheduled maintenance.

Choose the highest-value unit whose dependencies and authority are satisfied.
Prefer a coherent vertical slice over broad horizontal foundations. If all
remaining units are blocked, enter the blocker decision rather than selecting
busywork.

### Frame

Define only what the current unit needs:

- observable outcome;
- owned scope and protected boundaries;
- relevant product and implementation truth;
- acceptance claims and nearest evidence;
- authority and active risk;
- retry, reframe, budget, and stop conditions.

Resolve repository facts locally. Consolidate unresolved material user questions
before starting substantial execution and apply mature reversible defaults to
ordinary technical decisions.

### Execute

Implement the smallest coherent change that can satisfy the framed claims. Batch
related edits until an informative feedback boundary. Keep overlapping writes and
shared decisions sequential. Parallel discovery or workers are optional tools,
not defining properties of the loop.

### Observe

Collect real feedback from the closest useful boundary: diff, deterministic test,
API or stored state, browser interaction, screenshot, build artifact, or external
state. The provider depends on the claim.

The built-in browser is an Observation provider. When a page becomes runnable,
keep its active route visible in one authorized browser session and refresh at
coherent page or journey checkpoints. Browser visibility is not a progress
dashboard and does not define the loop itself.

### Verify

Compare observed evidence with the framed claims. Verification protects user and
system outcomes, not the implementation's preferred story.

- Routine: the controller uses one focused check or real-page observation.
- Shared: run affected regression or contract evidence; use an independent
  checker when self-review cannot reliably falsify the claim.
- High-risk: verify authority and the closest real integration boundary, with an
  independent checker before acceptance.
- Final project acceptance: independently inspect the diff, evidence map, missing
  claims, and stop conditions. The checker reviews; it does not reimplement.

Checker use is risk-based because checking every iteration increases cost and
coordination without proportional evidence.

### Record

Write back only truth with a real later consumer:

- product-wide discoveries to Product Plan or their shared source;
- durable page truth to Page Overview when reuse justifies it;
- local implementation truth to the current Development Guide or handoff;
- accepted code to Git;
- current host Goal status when that capability is available;
- evidence while its named dependencies remain unchanged.

Git, approved documents, host Goal state, and valid evidence form the default
spine. `project-state/current.json` remains optional and is written only when
cross-session recovery or interruption has a real consumer. No mandatory
`LOOP.md`, iteration log, or event database is added.

### Continue or Stop

If the unit's claims pass, accept the unit, update affected higher-level claims,
and return to Discover. Page evidence can support a Journey but cannot prove it;
Journey evidence can support project readiness but cannot substitute for release
evidence.

If evidence fails, classify the cause, then choose repair, local redesign,
reframe, bounded fallback, or stop. Retry only when a relevant condition changes.
Two equivalent failures require a changed approach or termination of that path.

## Loop Contract

One active finite delivery loop carries this logical contract in working context:

- **Objective:** final observable result.
- **Scope and non-goals:** included and protected boundaries.
- **Discovery source:** approved product truth and repository state from which the
  next unit is selected.
- **Active unit:** current page, Journey, service, or other coherent slice.
- **Acceptance claims:** statements that must become true.
- **Evidence targets:** observations that can prove each claim false or true.
- **Authority:** allowed local work and confirmation boundaries.
- **Budget:** relevant time, cost, retry, or iteration limit.
- **Stop conditions:** proof, cancellation, true blocker, or exhausted budget.
- **Next action:** the nearest concrete action selected from current evidence.

This is a logical contract, not a mandatory new artifact or JSON schema. Existing
Product Plan, Development Guide, host Goal, and active context carry it unless a
real recovery consumer requires persistence.

## Nested evidence scopes

Jarvis may reason about three nested scopes without creating multiple competing
controllers or state machines:

```text
Project Loop
  Journey evidence scope
    Page or service unit evidence scope
```

The Project Loop remains the single outer owner. Smaller scopes are bounded
feedback cycles inside its Execute, Observe, and Verify moves. Each scope can
accept its own claims, but only the outer loop selects the next project unit and
decides final termination.

## Goal and human control

An explicit request for Jarvis to own autonomous multi-step delivery authorizes
automatic host Goal creation after the Loop Contract is decision-ready. A stable
explicit opt-in to automatic Jarvis Goal ownership also qualifies. Ordinary tasks
do not silently create host Goals, and an unfinished Goal is reconciled rather
than duplicated.

The human supplies product intent and authority, not routine prompts between loop
moves. Interrupt only for:

- missing permission, account, secret, or organizational authority;
- an unauthorized destructive, irreversible, paid, production, publishing, or
  external effect;
- conflicting product directions with materially different outcomes;
- a true dependency or environment blocker that prevents meaningful independent
  progress.

Pause, resume, redirect, cancel, and correction retain their existing meanings.
Progress updates correspond to material loop transitions: framing complete, first
observable result, accepted unit or Journey, material reframe, blocker, and final
termination. Do not narrate each command or iteration.

## Termination and Proof-of-Done

The loop may terminate as:

- **Complete:** every required in-scope claim has fresh evidence, the final diff
  matches the objective, failed evidence has been superseded, truth changes are
  propagated, required Journeys have real-boundary evidence, side effects are
  reconciled, and no required work remains.
- **Blocked:** a true blocker prevents all meaningful in-scope progress and the
  host's blocked semantics are satisfied.
- **Cancelled:** the user cancels; unstarted effects stop and recoverable work is
  preserved unless removal is explicitly requested.
- **Budget exhausted:** the active limit is reached. The work remains incomplete;
  report accepted progress, missing proof, and the smallest useful next action.

Compiler success, green unit tests, worker completion, a checker opinion, or a
visible page alone cannot prove the whole project complete.

## Failure controls

- Never repeat an equivalent attempt without a changed condition.
- Never delete or weaken a valid test merely to make the loop converge.
- Never lower an acceptance claim without updated Product Truth.
- Never let maker output become its own independent evidence.
- Never replace browser, persistence, authorization, or release evidence with a
  structurally easier check.
- Never continue an unbounded loop without a current objective, budget, and stop
  condition.

When a provider is unavailable, continue independent work and use a bounded
fallback only if it proves the same claim. Otherwise preserve the claim as
unverified.

## Relationship to the superseded design

The autonomous Goal and browser-workbench design is not implemented as a separate
lifecycle:

- requirement intake becomes Discover and Frame;
- automatic Goal creation becomes Loop initialization;
- dependency-ordered delivery becomes repeated Discover and Execute;
- browser workbench becomes an Observation provider;
- final verification becomes Proof-of-Done and the Complete stop condition;
- lightweight progress becomes material loop-transition reporting.

Its design and implementation-plan documents remain as historical decision input
but are marked superseded and must not be executed directly.

## Evaluation

Behavior evals will discriminate at least these cases:

- Discover uses repository truth before asking the user;
- insufficient framing prevents material execution;
- the loop selects the next valuable unblocked unit rather than a fixed ceremony;
- one coherent implementation batch reaches an informative Observation boundary;
- browser evidence changes the next action instead of serving as decoration;
- failed evidence triggers classification and reframe;
- two equivalent failures stop mechanical retry;
- routine work avoids an unnecessary independent checker;
- shared, high-risk, and final boundaries activate appropriate independent review;
- page evidence does not substitute for Journey or project evidence;
- Record writes only durable truth with a consumer;
- interrupted delivery recovers from the light spine;
- complete, blocked, cancelled, and budget-exhausted remain distinct;
- a finite delivery loop does not invent scheduled maintenance or perpetual work.

Deterministic tests will require the Loop Engineering contract, Skill linkage,
supersession markers, and behavior-eval tags. Repository validation, standalone
packaging, and the unit suite remain the structural final gate.

Structural checks and JSON fixtures do not prove qualitative loop behavior. A
representative run must exercise unit selection, real observation, evidence-driven
reframing, risk-based checking, state writeback, and honest termination before the
project claims Loop Engineering works end to end.

## Non-goals

- renaming the public Skill from `jarvis`;
- a scheduler, recurring Automation, issue watcher, or perpetual maintenance loop;
- a workflow runtime, mandatory state machine, task queue, or event log;
- a mandatory `LOOP.md` or JSON record for every iteration;
- a browser Goal dashboard or command trace;
- mandatory subagents, worktrees, maker/checker pairs, or broad suites for routine
  work;
- automatic deployment, publishing, production writes, or external messaging;
- claiming independent verification when maker and checker share the same
  unsupported conclusion.

## Implementation boundary

Prefer replacing and tightening the existing feedback-loop language in
`core/operating-model.md` over adding a second control kernel. Add a small Loop
Contract policy only if the operating model would otherwise become unclear.
Integrate Goal, browser, verification, state, budget, provider, and delegation
behavior by reference to their existing owners; do not duplicate those policies
inside `skills/jarvis/SKILL.md`.

Update README and CHANGELOG terminology, add discriminating behavior evals, and
add one deterministic validator regression. Do not add runtime code, templates,
state fields, public skills, capabilities, Recipes, or Golden Paths unless the
implementation exposes a real missing consumer.
