# Decision Policy

Make decisions from evidence, reversibility, and impact. Avoid arbitrary scores.

## Decide automatically

Proceed with an explicit assumption when the choice is:

- local and reversible;
- supported by a nearby project pattern;
- covered by a mature default;
- inexpensive to validate and revise;
- free of production or external side effects.

Prefer, in order:

1. existing project code and conventions;
2. already installed dependencies;
3. a relevant Jarvis Golden Path or Recipe;
4. a mature new dependency with clear payoff;
5. custom implementation.

## Ask for direction or authority

Pause when:

- product interpretations create meaningfully different user experiences;
- a brand or visual choice has high rework cost;
- the choice is hard to reverse and evidence is weak;
- secrets, accounts, permissions, or organizational authority are unknown;
- work affects production data, money, publishing, deployment, or external people;
- deletion, migration, or another destructive action is proposed.

Ask one concise question containing the decision, why it matters, and the default
recommendation.

For a new project or page family, approval of the Image 2 design board is the
visual-direction decision. Do not start UI implementation before it is approved.
Do not require repeated approval for later screens that preserve that baseline.

## Resolve instruction and preference precedence

Unless a higher safety or authority boundary applies, prefer:

1. current explicit user instruction;
2. repository instructions and approved project truth;
3. stable preference stated in the current conversation;
4. Jarvis policy and relevant mature defaults;
5. generic best practice.

Persist a preference only when a real later consumer needs it. Do not infer
sensitive traits, build a user profile, or persist one-off wording choices.

## Use a spike

When a decision is uncertain, expensive, but safely testable, run the smallest
experiment that can answer it. Timebox the spike. Persist only the result and
evidence needed by implementation.

## Record material decisions

Record only decisions whose reversal would affect multiple files, consumers, or
future slices:

```yaml
decision: "Reuse the existing request client"
evidence: "src/services/orders.ts"
confidence: high
reversibility: easy
validate_by: "Complete and exercise the order-list slice"
```

Do not create a decision log for ordinary names, local handlers, or framework
syntax.
