# Jarvis

Jarvis is a goal-driven skill suite for taking a product idea to verified,
working software without turning delivery into a chain of document gates.

It uses feedback control:

```text
observe -> choose the smallest valuable slice -> plan just enough -> build
        -> verify the product claim -> adapt -> continue
```

## Architecture

Jarvis ships four thin skill entry points from one source repository:

| Skill | Responsibility |
|---|---|
| `product-delivery` | Own the outcome, select slices, route work, and continue |
| `product-design` | Resolve product, interaction, and visual uncertainty |
| `solution-design` | Choose technical boundaries and implementation paths |
| `product-build` | Implement and verify working vertical slices |

Shared policy lives in `core/`. Product archetype defaults live in
`golden-paths/`. Feature-level defaults live in `recipes/`. Skills load only the
material needed for the current slice.

## Principles

- Existing repository truth beats generic best practice.
- Work in small vertical slices that produce observable product behavior.
- Plan the roadmap coarsely and the active slice precisely.
- Make reversible, low-impact decisions automatically and record assumptions.
- Ask only about direction, authority, secrets, production effects, and hard-to-
  reverse choices.
- Use the smallest check that can falsify the completion claim.
- Treat failed checks and disproved assumptions as replanning signals.
- Generate an artifact only when another person or tool will consume it.

## Repository layout

```text
skills/         Four installable skill entry points
core/           Shared operating, decision, planning, quality, and test policy
golden-paths/   Defaults for common product archetypes
recipes/        Defaults for common feature families
templates/      Minimal durable state and active-slice templates
evals/          Cross-skill workflow scenarios
scripts/        Deterministic repository validation
tests/          Validator regression tests
docs/           Approved design and implementation plan
```

## Validate

Requires Python 3.10 or newer. No third-party packages.

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Package for installation

Build four standalone skill directories. Shared policy remains single-source in
the repository and is copied only into ignored build output:

```powershell
python scripts/package_skills.py
```

Copy or link directories from `dist/` into the skill directory used by your
agent environment. Each package contains its required references and eval
fixtures; no repository-relative links remain.

## Status

V0.1 establishes the operating model, four entry points, adaptive defaults, and
evaluation fixtures. Real task runs should drive later changes; avoid adding
rules without a failing scenario.

## License

MIT
