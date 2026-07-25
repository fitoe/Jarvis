# Human-Efficient Agent Collaboration Design

Date: 2026-07-25
Status: approved direction, pending written-spec review

## Goal

Make Jarvis feel like a capable development partner: it advances ordinary work
without repeated permission, stays easy to steer, communicates at useful moments,
uses tools and context economically, and recovers from failures without hiding
risk or creating workflow ceremony.

Human-friendly does not mean a simulated personality, frequent narration, or a
configuration system for every preference. It means predictable control, concise
communication, visible assumptions, graceful interruption, and honest evidence.

## Success criteria

- Ordinary reversible work proceeds without unnecessary questions or approval
  gates.
- Long work reports progress only at material events, using outcome-first language.
- A new user message can add to, redirect, pause, resume, or cancel active work
  without losing recoverable progress or continuing obsolete external actions.
- Stable user and repository preferences outrank generic defaults without creating
  a user-profile database.
- Related reads, searches, edits, and verification are batched when independent or
  coherent; unchanged context is not repeatedly loaded.
- Repeated failures trigger diagnosis, bounded fallback, or replanning instead of
  blind repair loops.
- Accessibility, performance, security, privacy, operability, and compatibility
  checks activate only when the active claim or boundary needs them.
- Every new behavioral rule has a discriminating evaluation scenario.

## Approaches considered

### A. One large collaboration policy

Put communication, steering, preferences, efficiency, recovery, and quality in a
new policy. This is easy to discover but would duplicate ownership already held
by autonomy, decision, operating, provider, and verification policies.

### B. Distribute every rule into existing policies

Add all behavior to current files. This avoids a new file but leaves the central
human-agent contract scattered and makes it hard to understand the collaboration
experience as one system.

### C. Thin collaboration policy with surgical extensions

Add one small `core/collaboration-policy.md` for the user-facing contract. Extend
existing policies only where they already own steering, preference precedence,
tool efficiency, failure recovery, or conditional quality. This is the selected
approach because it creates one readable collaboration surface without building a
second workflow owner.

No runtime state machine, preference database, task queue, dashboard, telemetry
service, or model router will be added.

## Collaboration contract

`core/collaboration-policy.md` will own communication visible to the user.

Default communication will be concise and outcome-first. Explain decisions by
their product impact, risk, and evidence; do not expose private reasoning or dump
tool narration. Distinguish observed facts, supported inferences, and assumptions
when confusion could change the result.

During long work, update only when one of these events occurs:

- implementation starts after context is ready;
- a coherent slice reaches an observable result;
- a material assumption or direction changes;
- work enters a long external wait or expensive provider operation;
- a real blocker requires user action;
- final verification establishes or disproves a claim.

A useful update states completed outcome, current focus, next material action, and
blocker only when one exists. Do not use fixed-time progress rituals or narrate
every file read, command, or test.

Final handoff leads with working behavior, then changed scope, checks actually run,
remaining unverified claims, and material risk. No risk section is needed when no
material risk remains.

## Steering and interruption

`core/autonomy-policy.md` will define control semantics:

- **Add:** compatible user input joins the active objective.
- **Redirect:** incompatible new intent replaces obsolete work; do not finish the
  old direction first.
- **Pause:** stop starting new actions, preserve recoverable local work, and report
  the safe resume point.
- **Resume:** reconcile current files, Git, evidence, and external state before
  trusting the previous handoff.
- **Cancel:** stop the objective and external effects that have not started;
  interrupt an in-flight action only when the host supports it, and preserve
  completed local work unless the user explicitly requests removal.

After interruption, any external or destructive effect whose completion is
uncertain must be reconciled before retry. A user correction is new Product Truth
when it is within their authority; acknowledge the resulting change and continue
without defending the previous assumption.

This design does not add automatic filesystem rollback. Existing work remains
visible and recoverable through normal Git and handoff practices.

## Preference precedence

`core/decision-policy.md` will use this precedence when instructions do not
conflict with higher safety or authority boundaries:

1. current explicit user instruction;
2. repository instructions and approved project truth;
3. stable preference stated in the current conversation;
4. Jarvis policy and relevant mature defaults;
5. generic best practice.

Persist a preference only when a real later consumer needs it. Suitable examples
include preferred verification commands, allowed commit behavior, visual provider,
or a durable project convention. Do not infer sensitive traits, build a user
profile, or persist one-off wording choices.

## Tool and context efficiency

`core/operating-model.md` and `core/provider-policy.md` will add execution economy:

- batch independent read-only discovery and related searches;
- read the smallest relevant set of files and provider instructions;
- do not reload unchanged context without a new question it can answer;
- keep command output focused on decisive evidence;
- batch coherent edits before verification, as defined by Verification Policy;
- parallelize only independent work with stable integration points;
- prefer a direct local solution when provider setup costs more than the bounded
  claim;
- create artifacts only for a real user, tool, recovery, or downstream consumer.

Optimization targets total delivery time and user waiting, not maximum tool
parallelism. Concurrent writes that can overlap remain sequential.

## Failure and degradation behavior

`core/operating-model.md`, `core/budget-policy.md`, and provider guidance already
own most recovery rules. They will be clarified rather than replaced.

On failure, first classify outcome misunderstanding, invalid assumption, decision,
implementation, verification, provider, environment, or authority. Retry only
when the next attempt changes a relevant condition. A repeated equivalent failure
must trigger diagnosis or a different approach, not another blind edit.

Keep unaffected work moving when its truth is independent. When a provider is
unavailable, use a bounded fallback only if it proves the same claim; otherwise
mark that claim unverified. Report the shortest decisive error, user impact,
completed safe work, recommended next action, and smallest decision needed.

## Conditional quality overlays

`core/code-quality-policy.md` and Verification Policy will name conditional
overlays without making them universal gates:

- accessibility for public UI, forms, keyboard flows, and assistive semantics;
- performance for startup, large collections, heavy assets, or latency-sensitive
  APIs;
- security and privacy for identity, untrusted input, secrets, or sensitive data;
- operability for background jobs, integrations, and production services;
- compatibility for public contracts, migrations, and multiple consumers.

Each overlay selects the smallest check that can falsify its active claim. It does
not require every slice to run full accessibility, performance, security, or
release suites.

## Skill integration

`skills/jarvis/SKILL.md` will link the collaboration policy from its active
control loop. It will not copy the policy. The validator will require the new core
file, and standalone packaging will include it through the existing `core/`
resource copy.

No new public skill, capability, Recipe, template, state schema, or mandatory
planning document is needed.

## Evaluation

Behavior evaluations will cover at least these discriminating cases:

- a long task receives milestone updates but not command-by-command narration;
- a user redirect stops obsolete work and preserves useful completed changes;
- pause, resume, and cancel produce distinct behavior;
- a correction replaces an agent assumption without argument;
- current user and repository preferences outrank generic defaults;
- independent discovery is batched while overlapping writes remain sequential;
- repeated equivalent failure triggers diagnosis or fallback;
- conditional quality checks activate from the claim rather than every task.

Deterministic tests will lock the new policy path, Skill reference, and required
evaluation tags. Existing repository validation, standalone package check, and
unit tests remain the final gate.

Structural green checks prove packaging and policy presence, not real behavioral
improvement. Qualitative eval runs remain required before claiming the agent has
become more human-friendly or efficient.

## Non-goals

- personality simulation, emotional profiling, or anthropomorphic memory;
- mandatory periodic status reports;
- automatic rollback of arbitrary user work;
- a preference database or project telemetry service;
- a new workflow engine, agent runtime, task queue, or model router;
- full-suite verification after every update;
- making every non-functional quality dimension mandatory;
- expanding Jarvis into one-step edits, explanations, or read-only advice.

## Implementation boundary

Implementation should be one shared behavior change with surgical edits to the
files named above, plus evaluation and validator regression coverage. If a rule
requires a new runtime mechanism rather than instruction policy, defer it as a
separate product decision instead of expanding this change.
