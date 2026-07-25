from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if __package__:
    from scripts.state import validate_state
else:
    from state import validate_state


SKILLS = ("jarvis",)

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
    "core/product-validation.md",
    "core/budget-policy.md",
    "core/evidence-policy.md",
    "core/side-effect-policy.md",
    "core/provider-policy.md",
    "core/delegation-policy.md",
    "core/visual-source-policy.md",
    "capabilities/product-design.md",
    "capabilities/solution-design.md",
    "capabilities/product-build.md",
    "golden-paths/README.md",
    "recipes/README.md",
    "examples/lead-operations/README.md",
    "examples/lead-operations/docs/product-plan.md",
    "examples/lead-operations/docs/pages/lead-list/overview.md",
    "examples/lead-operations/docs/pages/lead-list/development.md",
    "templates/delivery-state.json",
    "templates/product-plan.md",
    "templates/page-overview.md",
    "templates/development-guide.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "NOTICE.md",
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
    if not isinstance(evals, list) or not evals:
        errors.append(f"{path}: expected at least 1 eval")
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
        tags = case.get("tags")
        if not isinstance(tags, list) or not tags or not all(
            isinstance(tag, str) and tag for tag in tags
        ):
            errors.append(f"{prefix} needs non-empty tags")
    return errors


def validate_trigger_evals(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid trigger eval file {path}: {exc}"]
    if not isinstance(payload, list) or not payload:
        return [f"{path}: expected a non-empty array"]

    queries: set[str] = set()
    values: set[bool] = set()
    for index, item in enumerate(payload, start=1):
        prefix = f"{path}: trigger eval {index}"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        query = item.get("query")
        if not isinstance(query, str) or not query.strip():
            errors.append(f"{prefix} missing query")
        elif query in queries:
            errors.append(f"{prefix} duplicates a query")
        else:
            queries.add(query)
        should_trigger = item.get("should_trigger")
        if not isinstance(should_trigger, bool):
            errors.append(f"{prefix}.should_trigger must be boolean")
        else:
            values.add(should_trigger)
    if values != {True, False}:
        errors.append(f"{path}: include both trigger and non-trigger cases")
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
        if not eval_file.is_file():
            errors.append(f"missing evals: {eval_file.relative_to(root)}")
        else:
            errors.extend(validate_eval_file(eval_file, skill_name))

        trigger_file = skill_root / "evals" / "trigger-evals.json"
        if not trigger_file.is_file():
            errors.append(f"missing trigger evals: {trigger_file.relative_to(root)}")
        else:
            errors.extend(validate_trigger_evals(trigger_file))

    state_path = root / "templates" / "delivery-state.json"
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            errors.extend(
                f"delivery-state.json: {error}" for error in validate_state(state)
            )
        except json.JSONDecodeError as exc:
            errors.append(f"invalid delivery-state.json: {exc}")

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
    skill_lines = {
        name: len((root / "skills" / name / "SKILL.md").read_text(encoding="utf-8").splitlines())
        for name in SKILLS
    }
    line_report = ", ".join(f"{name}={count} lines" for name, count in skill_lines.items())
    print(f"Jarvis validation passed: {skill_count} skill, {eval_count} evals; {line_report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
