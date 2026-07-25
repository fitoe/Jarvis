# Operating Model

Jarvis controls delivery through evidence and feedback, not mandatory stage
transitions.

## Start from one observable result

Express the request as:

- **Outcome:** behavior a user or system should observe.
- **Scope:** smallest flow, service, page, or package affected.
- **Success:** evidence that can prove or falsify the outcome.

Ask only when materially different interpretations would change the product or
when the action needs authority. Carry other unknowns as visible assumptions.

## Inspect local truth

Before deciding how to work:

1. Read repository instructions and project documentation.
2. Inspect manifests, installed dependencies, nearby implementations, tests, and
   the current worktree.
3. Reuse existing product, architecture, and code conventions.
4. Use a Golden Path only when local truth does not answer the decision.

## Work economically

- batch independent read-only discovery and related searches;
- load only files and instructions needed by the active slice;
- do not reread unchanged context without a new question it can answer;
- keep command output focused on decisive evidence;
- batch coherent edits before the verification boundary;
- parallelize only independent work with stable integration points;
- create an artifact only for a real user, tool, recovery, or downstream consumer.

Optimize total delivery time and user waiting, not maximum tool parallelism.
Concurrent writes that can overlap remain sequential.

## Keep truth boundaries separate

- **Product truth:** approved users, jobs, scope, behavior, data, states, and
  authority.
- **Visual truth:** approved composition, hierarchy, typography, color, assets,
  components, and target viewports.
- **Implementation choices:** reversible technical means used to realize the
  product and visual truth.
- **Evidence:** observations that support one named claim while their inputs stay
  valid.

Generated output and provider suggestions remain proposals until accepted into
the relevant truth boundary. Visual truth cannot add product behavior, and an
implementation choice cannot silently redefine the outcome.

## Select a vertical slice

Choose the smallest coherent path from an input or user action to an observable
result. A slice should be useful, testable, and small enough to finish without
holding the whole product in context.

For a new product, prefer a walking skeleton through UI or API, business logic,
and data before building broad horizontal foundations.

## Run the feedback loop

1. Define the current slice; type claims only when their evidence could be
   confused.
2. Resolve only decisions that affect the slice.
3. Implement the smallest coherent change.
4. Run the nearest check that can falsify each claim.
5. If evidence passes, update state and select the next slice.
6. If evidence fails, classify the cause before editing again.

Failure classifications:

- misunderstood outcome;
- invalid assumption;
- unsuitable design or technical decision;
- implementation defect;
- unsuitable verification;
- unavailable authority, dependency, or environment.

Retry only when the next attempt changes a relevant condition. Replan when an
assumption fails, scope expands, a closer local pattern appears, or the same
equivalent failure occurs twice. Keep unaffected work moving when its truth is
independent.

## Finish honestly

Completion means the in-scope product claims have fresh evidence. Report what is
working, what was verified, what remains unverified, and the next material risk.
Do not convert optional polish or unrelated debt into hidden completion work.
