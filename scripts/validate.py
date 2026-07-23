from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILLS = (
    "product-delivery",
    "product-design",
    "solution-design",
    "product-build",
)

REQUIRED_PATHS = (
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "core/operating-model.md",
    "core/decision-policy.md",
    "core/autonomy-policy.md",
    "core/planning-policy.md",
    "core/code-quality-policy.md",
    "core/verification-policy.md",
    "golden-paths/README.md",
    "recipes/README.md",
    "templates/delivery-state.yaml",
    "templates/active-slice.md",
)

STATE_KEYS = (
    "goal",
    "success_claims",
    "mode",
    "current_slice",
    "assumptions",
    "decisions",
    "blockers",
    "evidence",
    "next_action",
)

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            clean_target = target.split("#", 1)[0].strip()
            if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(f"broken link in {path.relative_to(root)}: {target}")
    return errors


def validate_eval_file(path: Path, skill_name: str) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid eval file {path}: {exc}"]

    if payload.get("skill_name") != skill_name:
        errors.append(f"{path}: skill_name must be {skill_name}")

    evals = payload.get("evals")
    if not isinstance(evals, list) or len(evals) < 3:
        errors.append(f"{path}: expected at least 3 evals")
        return errors

    ids: set[int] = set()
    for index, case in enumerate(evals, start=1):
        prefix = f"{path}: eval {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, int) or case_id in ids:
            errors.append(f"{prefix} must have a unique integer id")
        else:
            ids.add(case_id)
        for field in ("prompt", "expected_output"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{prefix} missing {field}")
        expectations = case.get("expectations")
        if not isinstance(expectations, list) or len(expectations) < 2:
            errors.append(f"{prefix} needs at least 2 expectations")
    return errors


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for skill_name in SKILLS:
        skill_root = root / "skills" / skill_name
        skill_file = skill_root / "SKILL.md"
        eval_file = skill_root / "evals" / "evals.json"
        if not skill_file.is_file():
            errors.append(f"missing skill: {skill_file.relative_to(root)}")
            continue

        text = skill_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("name") != skill_name:
            errors.append(f"{skill_file.relative_to(root)}: name must be {skill_name}")
        description = frontmatter.get("description", "")
        if len(description) < 80:
            errors.append(f"{skill_file.relative_to(root)}: description is too weak")
        line_count = len(text.splitlines())
        if line_count > 180:
            errors.append(
                f"{skill_file.relative_to(root)}: {line_count} lines exceeds 180"
            )
        if not eval_file.is_file():
            errors.append(f"missing evals: {eval_file.relative_to(root)}")
        else:
            errors.extend(validate_eval_file(eval_file, skill_name))

    state_path = root / "templates" / "delivery-state.yaml"
    if state_path.is_file():
        state_text = state_path.read_text(encoding="utf-8")
        for key in STATE_KEYS:
            if not re.search(rf"(?m)^{re.escape(key)}\s*:", state_text):
                errors.append(f"delivery-state.yaml missing key: {key}")

    errors.extend(validate_markdown_links(root))
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repo(root)
    if errors:
        print("Jarvis validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = len(SKILLS)
    eval_count = sum(
        len(json.loads((root / "skills" / name / "evals" / "evals.json").read_text(encoding="utf-8"))["evals"])
        for name in SKILLS
    )
    print(f"Jarvis validation passed: {skill_count} skills, {eval_count} evals")
    return 0


if __name__ == "__main__":
    sys.exit(main())
