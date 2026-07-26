# Jarvis

Jarvis is a goal-driven Skill for taking a product idea to verified working
software through finite Loop Engineering, without turning delivery into a chain
of document or approval gates.

```text
Discover -> Frame -> Execute -> Observe -> Verify -> Record -> Continue or Stop
```

## Architecture

Jarvis exposes one installable skill and loads three internal capabilities only
when the current delivery unit needs them:

| Component | Responsibility |
|---|---|
| `jarvis` | Own the outcome, planning hierarchy, integration, and acceptance |
| Product Design | Resolve product, interaction, and visual uncertainty |
| Solution Design | Choose technical boundaries and implementation paths |
| Product Build | Implement and verify working vertical slices |

This avoids competing public workflow owners and trigger conflicts while
preserving progressive loading. Shared policy lives in `core/`; capability
modules in `capabilities/`; product defaults in `golden-paths/`; feature defaults
in `recipes/`.

Jarvis remains the project controller. A capable model maintains a readable
Product Plan and one self-contained Development Guide for current implementation.
It adds Page Overview only when durable page truth has multiple guides,
consumers, or implementation cycles. Bounded workers receive the guide plus
relevant repository code, not the full roadmap or conversation.

## Principles

- Existing repository truth beats generic best practice.
- Run one finite project loop; select the next valuable unblocked unit from
  current truth and evidence.
- Frame claims, evidence, authority, budget, and stop conditions before material
  execution.
- Let real observations change the next action; never loop on unchanged failure
  conditions.
- Keep Git, approved documents, host Goal, and valid evidence as the light spine.
- Activate independent checking by risk, not after every routine edit.
- Work in coherent pages or delivery units that produce observable behavior.
- Plan product and future pages coarsely; detail only current work.
- Keep Product Plan, optional Page Overview, and Development Guide human-readable.
- Omit Page Overview for a simple page with one guide and no separate durable
  page-document consumer; extract it later when reuse appears.
- Treat Development Guide as compiled local context, not input to another packet.
- Make lower-level documents expand rather than redefine upstream truth.
- Run a context-closure check before bounded implementation begins.
- Return `needs-context` instead of guessing product behavior, authority, or a
  shared contract.
- Make reversible, low-impact decisions automatically and record assumptions.
- Ask only about direction, authority, secrets, production effects, and hard-to-
  reverse choices.
- Communicate at material delivery events, accept correction without friction,
  and keep pause, resume, redirect, and cancel behavior predictable.
- Batch independent discovery and coherent implementation work; load providers
  and quality overlays only when the active claim needs them.
- Use the smallest check that can falsify the completion claim.
- Treat failed checks and disproved assumptions as replanning signals.
- Invalidate durable evidence when its code dependencies change.
- Reconcile external side effects before retrying them after interruption.
- Generate an artifact only when another person or tool will consume it.
- For new visual surfaces, settle product truth, generate GPT Image 2 references,
  and implement against one persistent project design language.
- Generate related pages together when useful, and require human approval of the
  resulting visual baseline before page-level UI implementation.
- Use GPT Image 2 for new UI design generation; use Figma only for existing
  user-supplied sources unless the user explicitly requests Figma creation.
- Decompose only visually complex sources into semantic sections; preserve the
  full-page source and require section plus assembled-page comparison.
- Keep Product Truth, Visual Truth, implementation choices, and evidence separate.
- Treat skills, plugins, models, and services as bounded providers; Jarvis retains
  goal, authority, state, budget, and completion ownership.
- Compose software work with `efficient-development-workflow`, apply
  `karpathy-guidelines` to code work, and select other installed skills only from
  the active slice's needs.
- Classify completion claims so product, functional, visual, quality, and release
  evidence cannot substitute for one another.
- Delegate only bounded work with explicit ownership and integration points;
  use the current Development Guide and ordinary handback, not JSON task packets.
- Route durable implementation discoveries back to Product Plan, optional Page
  Overview, or Development Guide according to truth ownership.
- Subagent completion never replaces Jarvis acceptance.

## Repository layout

```text
skills/jarvis/  One installable skill, evals, and trigger tests
capabilities/   Product Design, Solution Design, and Product Build modules
core/           Shared operating, decision, planning, quality, and test policy
golden-paths/   Defaults for common product archetypes
recipes/        Defaults for common feature families
examples/       Lead Operations example where the optional Page Overview is useful
templates/      Product Plan, optional Page Overview, Development Guide, and state
evals/          Evaluation guidance
scripts/        State, packaging, and repository validation tools
tests/          Validator regression tests
docs/           Approved design and implementation plan
```

## Validate

Requires Python 3.10 or newer. No third-party packages.

```powershell
python scripts/validate.py
python scripts/package_skills.py --check
python -m unittest discover -s tests -v
```

Durable state uses JSON so it can be validated and reconciled without third-party
dependencies:

```powershell
python scripts/state.py init project-state/current.json --goal "Ship the core flow"
python scripts/state.py reconcile project-state/current.json --repo . --write
```

## Package for installation

Build one standalone skill directory. Shared policy remains single-source in the
repository and is copied only into ignored build output:

```powershell
python scripts/package_skills.py
```

Copy or link `dist/jarvis` into the skill directory used by your agent
environment. The package contains its required references, state tool, and eval
fixtures; no repository-relative links remain.

## Status

V0.11 makes Loop Engineering the Jarvis operating model: one finite outer loop
discovers, frames, executes, observes, verifies, records, and terminates from
evidence. Goal, browser, skills, workers, and recovery state remain proportional
loop primitives, not mandatory stages. Structural and fixture checks do not prove
qualitative convergence; representative Loop runs remain required.

## License

MIT
