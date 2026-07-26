# Autonomous Goal and Browser Workbench Design

Date: 2026-07-26
Status: superseded by `2026-07-26-loop-engineering-jarvis-design.md`

Do not implement this design as a separate lifecycle. Its requirement intake,
Goal, browser, verification, and progress concepts are absorbed into Jarvis Loop
Engineering.

## Goal

Let Jarvis front-load material product questions, then autonomously deliver a
multi-step project from implementation through final acceptance with minimal
human intervention. Once a real page can run, keep that page visible in the
host's built-in browser so the user can watch coherent product progress.

This change defines controller behavior. It does not add a workflow engine,
progress dashboard, browser runtime, or replacement for host-provided Goal and
browser tools.

## Success criteria

- Jarvis investigates local truth before asking the user for information already
  available in the repository.
- Material unresolved questions are presented once as a consolidated intake,
  with a recommended default for each optional decision.
- When intake is sufficient for a multi-step delivery, Jarvis automatically uses
  the host's `create_goal` capability when available and starts execution without
  another approval round.
- Work proceeds in dependency order through coherent delivery units until every
  in-scope acceptance claim has fresh evidence or a true blocker occurs.
- The current runnable page remains open in one visible browser session and is
  refreshed at coherent product checkpoints, not after every edit.
- User interruption is limited to missing authority or secrets, irreversible or
  production effects, conflicting product direction, and blockers that prevent
  meaningful independent progress.
- Goal completion is reported only after final acceptance evidence. Host Goal
  state is updated consistently when the host exposes that capability.
- Every new behavioral rule has a discriminating evaluation scenario.

## Approaches considered

### A. Policy-driven controller behavior

Add thin intake, Goal lifecycle, and browser-workbench contracts to existing
`core/` policy owners, link them from the Jarvis control loop, and protect them
with behavior evals. Host tools perform Goal and browser actions. This is the
selected approach because it adds the requested behavior without creating a
second orchestration system.

### B. Mandatory fixed pipeline

Force every task through intake, Goal creation, planning, implementation, browser
verification, project verification, and closure. This is predictable but makes
routine work ceremonial and conflicts with Jarvis's proportional workflow.

### C. New orchestration runtime

Add a task runner that owns steps, state, browser refresh, and recovery. This
offers tighter runtime control but turns Jarvis from a skill into the workflow
system it is meant to replace. It is outside this change.

## Delivery lifecycle

Jarvis uses two user-visible phases for substantial multi-step delivery.

### Requirement lock

1. Inspect repository instructions, planning documents, code, routes,
   dependencies, tests, run commands, current Git state, and available host
   capabilities.
2. Separate facts discoverable locally from material product decisions only the
   user can make.
3. Send one consolidated intake containing the unresolved material questions.
   Each optional question includes a recommended default and its consequence.
4. Reconcile the answer once. Apply stated defaults to unanswered optional
   questions. Ask a follow-up only when the response introduces a new material
   conflict or leaves a Goal-start condition unsatisfied.
5. Lock the executable delivery contract: outcome, users, scope, non-goals,
   critical pages or journey, observable acceptance, authority, and first unit.

The consolidated intake replaces repeated approval prompts. It must not become a
generic questionnaire: omit decisions answered by repository truth, approved
product truth, or a mature reversible default.

### Autonomous delivery

After the Goal-start conditions pass, Jarvis creates the Goal and proceeds through
the dependency-ordered delivery units. It implements a coherent unit, gathers the
nearest useful evidence, integrates it, selects the next unit, and continues
without asking for phase-by-phase approval.

Shared decisions and overlapping writes remain sequential. Independent read-only
discovery may be batched. Routine one-step edits continue to bypass Goal creation
and the project lifecycle.

## Goal-start contract

Jarvis automatically calls `create_goal` only when all these conditions hold:

- the request is a substantial multi-step delivery that Jarvis should own;
- outcome, intended users, scope, and explicit non-goals are decision-ready;
- the critical page set or end-to-end journey is understood;
- success claims have observable evidence targets;
- repository and runtime discovery is sufficient to choose the first unit;
- material product decisions are answered or have accepted defaults;
- ordinary execution authority is present and known high-risk external effects
  are separated behind their own confirmation boundary;
- no unfinished host Goal already owns the work.

If the host does not expose Goal capabilities, Jarvis keeps the same delivery
contract in active context and continues; it reports Goal state as host-untracked,
not as created. If another Goal is active, Jarvis resumes, redirects, or asks for
direction according to the existing steering policy instead of creating a second
owner.

Goal creation is a lifecycle event, not a request for another user confirmation.
Goal completion requires fresh evidence for every in-scope acceptance claim and
no required work remaining. A hard blocker updates Goal state only when the host's
blocked semantics are satisfied; ordinary test failures do not mark it blocked.

## Browser workbench contract

The browser workbench shows the product being built, not agent telemetry.

- Start the project's existing development server when the current page first
  becomes runnable.
- Open the active route in a visible host-provided built-in browser and reuse the
  same session so navigation state, isolated test data, and authorized login state
  remain available.
- Refresh or navigate when a coherent page state or user-visible capability is
  ready. Do not refresh for each file change, command, or incomplete component.
- Exercise loading, success, empty, error, recovery, interaction, and responsive
  states only when they are in scope for that page.
- For cross-page journeys, follow the real navigation sequence and inspect the
  resulting application state.
- Keep textual progress in the host conversation. Do not build a separate browser
  progress dashboard.

Browser creation, authentication, form submission, upload, or another sensitive
operation still follows host confirmation rules. Reuse an existing authorized
session when possible. Browser unavailability does not stop independent code work;
it leaves visual or real-flow claims unverified until a bounded fallback or later
browser check can prove them.

Live visibility means the user can watch the active page and coherent refreshes.
It does not promise streaming DOM updates when the application lacks hot reload or
when the host browser cannot remain headed.

## Progress and interruption

Progress updates occur only at material lifecycle events:

- requirement lock completed;
- Goal created and autonomous delivery started;
- first runnable page opened;
- a page or critical journey became observable;
- a material assumption changed or a true blocker appeared;
- final acceptance changed completion status.

Updates state completed outcome, current focus, next material action, and blocker
only when one exists. They do not expose command-by-command traces or private
reasoning.

During autonomous delivery, Jarvis handles ordinary implementation defects,
failed checks, browser errors, and reversible design choices itself. It interrupts
the user only for:

- missing permission, account, secret, or organizational authority;
- irreversible, destructive, paid, production, publishing, or external effects
  not already authorized;
- conflicting product directions that would produce materially different user
  outcomes;
- a true environment or dependency blocker that prevents meaningful independent
  progress.

## Failure and recovery

Classify a failure before changing the implementation. Retry only when the next
attempt changes a relevant condition. Two equivalent failures trigger diagnosis,
replanning, or a bounded fallback rather than another blind retry.

Preserve completed compatible work when replanning. Continue independent units
when their product truth and evidence do not depend on the blocked boundary.
Before retrying an interrupted external effect, reconcile its real state using the
existing side-effect policy.

If a browser claim cannot be verified, distinguish page code completed from page
verified. Do not use unit or structural tests to claim visible browser behavior.

## Verification

Behavior evals will discriminate at least these cases:

- insufficient product information causes one consolidated intake and no Goal;
- repository discovery answers known questions instead of asking the user;
- complete intake triggers automatic Goal creation without another approval;
- a routine one-step edit bypasses Goal creation;
- an existing active Goal is reconciled rather than duplicated;
- delivery units execute in dependency order without repeated approval gates;
- the first runnable page opens in one visible browser session;
- coherent checkpoints refresh the page without per-edit browser churn;
- ordinary failures are repaired autonomously while true authority blockers ask;
- browser unavailability permits independent progress but prevents unsupported
  visual or journey claims;
- final evidence completes the Goal, while incomplete required work does not.

Deterministic repository tests will require the new policy headings, Skill links,
and evaluation tags. Final implementation verification remains the repository's
validation script, standalone package check, and unit suite.

Structural checks and JSON eval fixtures prove policy presence, not qualitative
agent behavior or host integration. Representative behavior evals and a real
headed-browser delivery run remain necessary before claiming the workflow works
end to end.

## Non-goals

- a browser-based Goal dashboard or tool-log viewer;
- a new task queue, workflow runtime, scheduler, or telemetry service;
- Goal creation for routine one-step edits, explanations, or read-only reviews;
- continuous refresh after every edit;
- bypassing browser, authentication, production, or external-effect confirmation
  rules imposed by the host;
- claiming real-time visibility on hosts without a headed browser;
- mandatory full-suite verification after each page or delivery unit.

## Implementation boundary

Keep shared behavior in `core/`. Extend the existing autonomy, operating,
collaboration, and provider boundaries only where they already own the rule; add a
small dedicated policy only if Goal and browser lifecycle ownership would
otherwise be ambiguous. `skills/jarvis/SKILL.md` links policy rather than copying
it. Add discriminating evals and one validator regression test.

Do not add runtime code unless implementation proves an instruction-only contract
cannot invoke an already available host capability. Any required host feature
beyond `create_goal`, Goal updates, a development server, and a visible browser is
a separate product decision.
