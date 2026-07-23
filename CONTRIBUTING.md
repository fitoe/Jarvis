# Contributing

Jarvis instructions are behavioral code. Improve observed delivery outcomes, not
document volume.

## Rule budget

- Add a control-kernel rule only for a repeated, cross-domain failure.
- Prefer a capability, Golden Path, Recipe, example, or tool when the concern is
  narrower.
- Add or update a discriminating behavior eval for every behavioral rule change.
- Include near-miss trigger cases when changing the skill description.
- Remove or merge rules that no longer change behavior.
- Treat line count and file count as review signals, not quality gates.

## Pull request evidence

Describe:

- observed problem or failing scenario;
- smallest policy or tool change;
- focused verification performed;
- behavior benchmark result, or an explicit statement that it remains unverified.

Run:

```powershell
python scripts/validate.py
python scripts/package_skills.py --check
python -m unittest discover -s tests -v
```

Do not claim skill behavior improved from structural checks alone.
