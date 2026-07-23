from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "0.2"
MODES = {"routine", "shared", "high-risk"}
EVIDENCE_STATUSES = {"fresh", "stale", "unverified"}
SIDE_EFFECT_STATUSES = {"planned", "confirmed", "failed", "reversed"}
REQUIRED_KEYS = (
    "schema_version",
    "goal",
    "success_claims",
    "mode",
    "current_slice",
    "assumptions",
    "decisions",
    "blockers",
    "evidence",
    "side_effects",
    "next_action",
)


def new_state(goal: str, next_action: str) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "goal": goal,
        "success_claims": [],
        "mode": "routine",
        "current_slice": None,
        "assumptions": [],
        "decisions": [],
        "blockers": [],
        "evidence": [],
        "side_effects": [],
        "next_action": next_action,
    }


def _require_string(item: dict[str, Any], key: str, prefix: str, errors: list[str]) -> None:
    if not isinstance(item.get(key), str) or not item[key].strip():
        errors.append(f"{prefix} requires non-empty string: {key}")


def validate_state(state: Any) -> list[str]:
    if not isinstance(state, dict):
        return ["state must be a JSON object"]

    errors: list[str] = []
    for key in REQUIRED_KEYS:
        if key not in state:
            errors.append(f"state missing key: {key}")

    if errors:
        return errors

    if state["schema_version"] != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    if not isinstance(state["goal"], str):
        errors.append("goal must be a string")
    if not isinstance(state["mode"], str) or state["mode"] not in MODES:
        errors.append(f"mode must be one of: {', '.join(sorted(MODES))}")
    if state["current_slice"] is not None and not isinstance(
        state["current_slice"], dict
    ):
        errors.append("current_slice must be null or an object")
    if not isinstance(state["next_action"], str):
        errors.append("next_action must be a string")

    for key in (
        "success_claims",
        "assumptions",
        "decisions",
        "blockers",
        "evidence",
        "side_effects",
    ):
        if not isinstance(state[key], list):
            errors.append(f"{key} must be a list")

    if errors:
        return errors

    evidence_ids: set[str] = set()
    for index, item in enumerate(state["evidence"], start=1):
        prefix = f"evidence[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for key in ("id", "claim_id", "kind", "checked_at", "environment", "result"):
            _require_string(item, key, prefix, errors)
        evidence_id = item.get("id")
        if isinstance(evidence_id, str):
            if evidence_id in evidence_ids:
                errors.append(f"duplicate evidence id: {evidence_id}")
            evidence_ids.add(evidence_id)
        if item.get("status") not in EVIDENCE_STATUSES:
            errors.append(f"{prefix} has invalid status")
        if not isinstance(item.get("depends_on"), list) or not all(
            isinstance(path, str) and path for path in item.get("depends_on", [])
        ):
            errors.append(f"{prefix}.depends_on must be a list of paths")
        for optional in ("commit", "command"):
            if optional in item and not isinstance(item[optional], str):
                errors.append(f"{prefix}.{optional} must be a string")

    side_effect_ids: set[str] = set()
    idempotency_keys: set[str] = set()
    for index, item in enumerate(state["side_effects"], start=1):
        prefix = f"side_effects[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for key in ("id", "action", "target", "idempotency_key"):
            _require_string(item, key, prefix, errors)
        side_effect_id = item.get("id")
        if isinstance(side_effect_id, str):
            if side_effect_id in side_effect_ids:
                errors.append(f"duplicate side-effect id: {side_effect_id}")
            side_effect_ids.add(side_effect_id)
        idempotency_key = item.get("idempotency_key")
        if isinstance(idempotency_key, str):
            if idempotency_key in idempotency_keys:
                errors.append(
                    f"duplicate side-effect idempotency_key: {idempotency_key}"
                )
            idempotency_keys.add(idempotency_key)
        if item.get("status") not in SIDE_EFFECT_STATUSES:
            errors.append(f"{prefix} has invalid status")
        if not isinstance(item.get("evidence", ""), str):
            errors.append(f"{prefix}.evidence must be a string")

    return errors


def read_state(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_state(path: Path, state: dict[str, Any]) -> None:
    errors = validate_state(state)
    if errors:
        raise ValueError("invalid state:\n" + "\n".join(errors))
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _git_paths(repo: Path, *arguments: str) -> set[str]:
    process = subprocess.run(
        ["git", *arguments],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0:
        detail = process.stderr.strip() or "unknown Git error"
        raise RuntimeError(f"git {' '.join(arguments)} failed: {detail}")
    return {
        line.strip().replace("\\", "/")
        for line in process.stdout.splitlines()
        if line.strip()
    }


def _commit_exists(repo: Path, commit: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=repo,
        capture_output=True,
        check=False,
    ).returncode == 0


def _dependency_changed(dependency: str, changed_paths: set[str]) -> bool:
    dependency = dependency.strip("/").replace("\\", "/")
    return any(
        path == dependency
        or path.startswith(f"{dependency}/")
        or dependency.startswith(f"{path}/")
        for path in changed_paths
    )


def reconcile_state(state: dict[str, Any], repo: Path) -> list[str]:
    stale: list[str] = []
    working_changes = set()
    working_changes |= _git_paths(repo, "diff", "--name-only")
    working_changes |= _git_paths(repo, "diff", "--cached", "--name-only")
    working_changes |= _git_paths(repo, "ls-files", "--others", "--exclude-standard")

    for evidence in state.get("evidence", []):
        if not isinstance(evidence, dict) or evidence.get("status") != "fresh":
            continue
        commit = evidence.get("commit", "")
        dependencies = evidence.get("depends_on", [])
        if not commit or not dependencies:
            continue
        if not _commit_exists(repo, commit):
            evidence["status"] = "stale"
            stale.append(evidence.get("id", "<unknown>"))
            continue
        changed_paths = working_changes | _git_paths(
            repo, "diff", "--name-only", f"{commit}..HEAD"
        )
        if any(_dependency_changed(path, changed_paths) for path in dependencies):
            evidence["status"] = "stale"
            stale.append(evidence.get("id", "<unknown>"))
    return stale


def _load_valid_state(path: Path) -> dict[str, Any]:
    state = read_state(path)
    errors = validate_state(state)
    if errors:
        raise ValueError("invalid state:\n" + "\n".join(errors))
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage Jarvis delivery state")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("path", type=Path)
    init_parser.add_argument("--goal", required=True)
    init_parser.add_argument("--next-action", default="Inspect local truth")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path", type=Path)

    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("path", type=Path)

    reconcile_parser = subparsers.add_parser("reconcile")
    reconcile_parser.add_argument("path", type=Path)
    reconcile_parser.add_argument("--repo", type=Path, default=Path.cwd())
    reconcile_parser.add_argument("--write", action="store_true")

    args = parser.parse_args()
    try:
        if args.command == "init":
            if args.path.exists():
                raise ValueError(f"state already exists: {args.path}")
            write_state(args.path, new_state(args.goal, args.next_action))
            print(f"Initialized {args.path}")
        elif args.command == "validate":
            _load_valid_state(args.path)
            print(f"Valid state: {args.path}")
        elif args.command == "show":
            state = _load_valid_state(args.path)
            print(json.dumps(state, ensure_ascii=False, indent=2))
        elif args.command == "reconcile":
            state = _load_valid_state(args.path)
            stale = reconcile_state(state, args.repo.resolve())
            if args.write and stale:
                write_state(args.path, state)
            print(f"Stale evidence: {len(stale)}")
            for evidence_id in stale:
                print(f"- {evidence_id}")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
