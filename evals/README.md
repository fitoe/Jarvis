# Evaluation Scenarios

Jarvis owns realistic behavior prompts under `skills/jarvis/evals/evals.json`.
Expectations describe observable behavior rather than exact wording.

`skills/jarvis/evals/trigger-evals.json` contains both realistic should-trigger
and near-miss should-not-trigger queries. It protects Jarvis from taking over
one-step edits, explanations, read-only reviews, and unrelated creative work.

Repository validation checks scenario structure only. `scripts/run_evals.py`
provides two executable layers:

- `behavior` runs a selected prompt through Codex in a read-only sandbox, then
  gives the response and event trace to a schema-constrained judge;
- `benchmark` runs the same prompt, model, sandbox, timeout, and judge once with
  Jarvis and once with no Jarvis Skill, then records paired pass and elapsed-time
  differences;
- `canary` copies a small project fixture into an isolated Git workspace, lets
  Codex implement it, and decides success only from deterministic acceptance
  commands. A fixture may allow one bounded repair that receives the failed
  acceptance evidence; unchanged retries are not allowed.

Run a focused behavioral scenario:

```powershell
python scripts/run_evals.py behavior --ids 22 --output .jarvis-evals/behavior-22.json
```

Run a paired Jarvis-versus-baseline benchmark:

```powershell
python scripts/run_evals.py benchmark --ids 22 --model gpt-5.6-sol --output .jarvis-evals/benchmark-22.json
```

Compare real fixture delivery with deterministic acceptance:

```powershell
python scripts/run_evals.py canary-benchmark --ids 2 --model gpt-5.6-terra --output .jarvis-evals/canary-benchmark-2.json
```

On Windows, a nested Codex sandbox may write only beneath roots already
authorized by the host session. If the default system-temporary workspace is
read-only, pass `--keep-workspaces <authorized-isolated-root>`. Keep that root
outside the Jarvis repository so project instructions and eval answers cannot
enter either candidate context. Do not replace this with `danger-full-access`.

Run the representative delivery canaries:

```powershell
python scripts/run_evals.py canary --output .jarvis-evals/canaries.json
```

Inspect safe local provider capabilities without pretending to validate host-only
Image 2, Goal, or subagent behavior:

```powershell
python scripts/run_evals.py probe --output .jarvis-evals/capabilities.json
```

Behavior candidates run from blank workspaces; delivery candidates run from
independent copies of the same fixture. Both use temporary
`CODEX_HOME` directories. The Jarvis candidate receives a standalone runtime
copy without `evals/`; the baseline receives no Jarvis Skill. User MCP, plugin,
Skill registrations, repository files, expected outputs, expectations, and the
judge schema are absent from both behavior-candidate contexts. Only the judge receives
the expected behavior after candidate execution.

These runs consume model capacity and therefore remain an explicit benchmark,
not a per-edit CI gate. A passing judged response supports only instruction
behavior; a passing canary additionally proves its fixture's observable
acceptance commands. Neither result proves every project class. Run
agent-vs-baseline benchmarks before claiming a general delivery improvement.

The browser canary intentionally uses isolated Playwright and a local browser
executable because a nested `codex exec` benchmark cannot inherit the desktop
host's built-in browser session. This does not change product delivery routing:
active page work still prefers the host's visible built-in browser when exposed.
The runner streams concise Codex events and prints a heartbeat every 30 seconds
during silent agent or acceptance work, while retaining full output in its report.

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
- substantial products use readable Product Plan and current Development Guide
  documents;
- simple single-guide pages omit Page Overview while reusable, complex, or
  repeatedly implemented pages keep it;
- routine edits bypass the hierarchy;
- Development Guides pass a read-only context-closure check before bounded work;
- lower-level documents cannot silently redefine upstream product or page truth;
- ordinary shared reuse stays local while shared behavior changes escalate;
- guides split by coherent claim and risk boundary rather than token count;
- implementation discoveries return to the narrowest durable truth owner;
- readable handback replaces mandatory JSON completion packets;
- complex visual decomposition activates from inspectability, not fixed size;
- semantic sections retain global style and adjacent-boundary context;
- section evidence cannot replace assembled full-page visual evidence.
