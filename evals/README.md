# Evaluation Scenarios

Jarvis owns realistic behavior prompts under `skills/jarvis/evals/evals.json`.
Expectations describe observable behavior rather than exact wording.

`skills/jarvis/evals/trigger-evals.json` contains both realistic should-trigger
and near-miss should-not-trigger queries. It protects Jarvis from taking over
one-step edits, explanations, read-only reviews, and unrelated creative work.

Initial evaluations are fixtures for qualitative runs and future benchmark
automation. Repository validation checks their schema. Run agent-vs-baseline
benchmarks before claiming that an instruction change improves delivery behavior.

Scenario coverage:

- routine work remains lightweight;
- new products start with a vertical slice;
- existing project patterns outrank generic defaults;
- shared and high-risk boundaries receive proportional evidence;
- visual fidelity is conditional on the completion claim;
- mock behavior is not reported as real integration;
- interrupted work is checked against current repository truth.
- changed dependencies invalidate durable evidence;
- uncertain external side effects are reconciled before retry;
- repeated repairs trigger replanning rather than infinite loops.
