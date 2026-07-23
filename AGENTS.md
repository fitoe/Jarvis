# Repository Guidelines

Jarvis is a goal-driven product-delivery skill suite. Keep it smaller than the
workflow systems it replaces.

## Development rules

- Follow `karpathy-guidelines`: state material assumptions, prefer the simplest
  implementation, make surgical changes, and verify observable results.
- Follow `efficient-development-workflow`: choose checks by risk and avoid
  mandatory documents, plans, branches, agents, or full suites for routine work.
- Explain why guidance exists. Avoid accumulating `MUST` rules to patch isolated
  failures; add or improve an evaluation scenario instead.
- Keep shared policy in `core/` and domain lenses in `capabilities/`. Do not copy
  them into `SKILL.md`.
- Treat skill size as a review signal, not a CI gate. Load capabilities, Golden
  Paths, and Recipes only when the active product or feature needs them.
- Artifacts are optional unless a real downstream consumer needs them.
- Every new behavioral rule needs a failing or discriminating eval scenario.
- Prefer changing a capability or Recipe over broadening the control kernel.

## Verification

Run before committing:

```powershell
python scripts/validate.py
python scripts/package_skills.py --check
python -m unittest discover -s tests -v
```

Report skipped checks as skipped. Never claim behavior that the checks did not
prove.
