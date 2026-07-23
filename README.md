# Jarvis

Jarvis is a goal-driven skill for taking a product idea to verified,
working software without turning delivery into a chain of document gates.

It uses feedback control:

```text
observe -> choose the smallest valuable slice -> plan just enough -> build
        -> verify the product claim -> adapt -> continue
```

## Architecture

Jarvis exposes one installable skill and loads three internal capabilities only
when the active slice needs them:

| Component | Responsibility |
|---|---|
| `jarvis` | Own the outcome, select slices, preserve state, and continue |
| Product Design | Resolve product, interaction, and visual uncertainty |
| Solution Design | Choose technical boundaries and implementation paths |
| Product Build | Implement and verify working vertical slices |

This avoids cross-skill routing and trigger conflicts while preserving progressive
loading. Shared policy lives in `core/`; capability modules in `capabilities/`;
product defaults in `golden-paths/`; feature defaults in `recipes/`.

## Principles

- Existing repository truth beats generic best practice.
- Work in small vertical slices that produce observable product behavior.
- Plan the roadmap coarsely and the active slice precisely.
- Make reversible, low-impact decisions automatically and record assumptions.
- Ask only about direction, authority, secrets, production effects, and hard-to-
  reverse choices.
- Use the smallest check that can falsify the completion claim.
- Treat failed checks and disproved assumptions as replanning signals.
- Invalidate durable evidence when its code dependencies change.
- Reconcile external side effects before retrying them after interruption.
- Generate an artifact only when another person or tool will consume it.
- For new visual surfaces, settle product truth, generate GPT Image 2 references,
  and implement against one persistent project design language.

## Repository layout

```text
skills/jarvis/  One installable skill, evals, and trigger tests
capabilities/   Product Design, Solution Design, and Product Build modules
core/           Shared operating, decision, planning, quality, and test policy
golden-paths/   Defaults for common product archetypes
recipes/        Defaults for common feature families
templates/      Durable state, Slice Packet, and human-readable slice templates
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

V0.3 adds an Image 2-first path for material new UI, one persistent project
visual baseline, Product Design plugin translation, and same-viewport comparison
without making routine UI edits pass a new design gate. Real agent-vs-baseline
runs remain required before claiming behavioral improvement.

## License

MIT
