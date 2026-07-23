# Jarvis Foundation Implementation Plan

> **For agentic workers:** implement this plan in the current repository using
> the lightest safe workflow. Keep work local until validation and public-content
> review pass.

**Goal:** Publish a usable V0.1 Jarvis skill suite with four thin entry points,
shared adaptive policy, mature defaults, and deterministic validation.

**Architecture:** One repository owns all shared policy. Four `SKILL.md` files
route into that policy without forming a mandatory stage chain. Golden Paths and
Recipes load progressively. Standard-library Python validates repository shape.

**Tech Stack:** Markdown, YAML templates, JSON evaluation fixtures, Python 3.10+,
GitHub Actions.

---

### Task 1: Establish repository contract

**Files:** `README.md`, `AGENTS.md`, `LICENSE`, `.gitignore`, design spec.

- [ ] Describe outcome, scope, architecture, safety boundary, and non-goals.
- [ ] Record coding and proportional-verification rules.
- [ ] Verify files contain no secrets or machine-specific configuration.

### Task 2: Implement shared delivery kernel

**Files:** `core/*.md`, `templates/*`.

- [ ] Define the feedback loop and vertical-slice state transition.
- [ ] Define autonomy, decision, planning, code-quality, and verification policy.
- [ ] Provide one durable state template and one active-slice template.

### Task 3: Implement four thin skills

**Files:** `skills/*/SKILL.md`.

- [ ] Give each skill one clear responsibility and trigger description.
- [ ] Route to shared policy and conditional resources.
- [ ] Keep each entry point below 180 lines and avoid duplicated policy.

### Task 4: Add adaptive defaults

**Files:** `golden-paths/*.md`, `recipes/*.md`.

- [ ] Cover common product archetypes without forcing a universal stack.
- [ ] Cover common feature families with applicability and escalation rules.
- [ ] Prefer repository patterns over every packaged default.

### Task 5: Add evaluation and validation

**Files:** `evals/evals.json`, `scripts/validate.py`, `tests/test_validate.py`,
`.github/workflows/validate.yml`.

- [ ] Add realistic routine, shared, high-risk, visual, and recovery scenarios.
- [ ] Validate required files, frontmatter, skill size, local links, templates,
  and evaluation schema.
- [ ] Run `python scripts/validate.py` and
  `python -m unittest discover -s tests -v`; expect exit code 0.

### Task 6: Publish

- [ ] Inspect Git status and staged diff.
- [ ] Scan tracked content for common secret patterns.
- [ ] Commit the verified V0.1 foundation.
- [ ] Create public `fitoe/Jarvis` and push `main`.
- [ ] Verify GitHub reports `PUBLIC` visibility and the pushed commit.
