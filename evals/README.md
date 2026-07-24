# Evaluation Scenarios

Jarvis owns realistic behavior prompts under `skills/jarvis/evals/evals.json`.
Expectations describe observable behavior rather than exact wording.

`skills/jarvis/evals/trigger-evals.json` contains both realistic should-trigger
and near-miss should-not-trigger queries. It protects Jarvis from taking over
one-step edits, explanations, read-only reviews, and unrelated creative work.

Initial evaluations are fixtures for qualitative runs and future benchmark
automation. Repository validation checks their schema. Run agent-vs-baseline
benchmarks before claiming that an instruction change improves delivery behavior.

Use Shadow Mode before trusting autonomous execution on varied projects:

1. Give baseline and Jarvis the same raw task and repository state.
2. Keep expected answers and prior diagnoses out of both contexts.
3. Compare task completion, human intervention, rework, elapsed time, visual
   drift, code quality, and unsafe or repeated side effects.
4. Classify failures by outcome, assumption, decision, implementation, provider,
   verification, or authority.
5. Change a general decision rule or provider contract only after the failure is
   reproducible; add a hard gate only for repeated high-impact risk.

Structural validation and green CI do not count as behavioral improvement.

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
- product and visual truth remain separate;
- provider capability does not become workflow ownership;
- claim types receive non-substitutable evidence;
- product uncertainty and visual fidelity overlay normal risk intensity;
- behavior claims require agent-vs-baseline or Shadow Mode evidence.
- software work composes with the process and code-quality governors;
- explicitly named skills outrank automatic domain selection;
- domain skills are selected from active need without skill swarms.
- Jarvis retains global planning, integration, and final acceptance;
- delegated work receives least-sufficient context and bounded ownership;
- only independent tasks run concurrently;
- worker and verifier evidence is integrated before completion.
- complex visual decomposition activates from inspectability, not fixed size;
- semantic sections retain global style and adjacent-boundary context;
- section evidence cannot replace assembled full-page visual evidence.
