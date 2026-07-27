from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "0.2"
MODES = {"routine", "shared", "high-risk"}
EVIDENCE_STATUSES = {"fresh", "stale", "unverified"}
SIDE_EFFECT_STATUSES = {"planned", "confirmed", "failed", "reversed"}
IN_FLIGHT_STATUSES = {"planned", "running", "uncertain", "completed", "failed"}
IN_FLIGHT_KINDS = {"provider", "agent", "command", "external-effect"}
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
        "in_flight": [],
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

    in_flight = state.get("in_flight", [])
    if not isinstance(in_flight, list):
        errors.append("in_flight must be a list")
        return errors
    in_flight_ids: set[str] = set()
    for index, item in enumerate(in_flight, start=1):
        prefix = f"in_flight[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for key in ("id", "target", "resume_action"):
            _require_string(item, key, prefix, errors)
        item_id = item.get("id")
        if isinstance(item_id, str):
            if item_id in in_flight_ids:
                errors.append(f"duplicate in-flight id: {item_id}")
            in_flight_ids.add(item_id)
        if item.get("kind") not in IN_FLIGHT_KINDS:
            errors.append(f"{prefix} has invalid kind")
        if item.get("status") not in IN_FLIGHT_STATUSES:
            errors.append(f"{prefix} has invalid status")
        for optional in ("external_id", "started_at"):
            if optional in item and not isinstance(item[optional], str):
                errors.append(f"{prefix}.{optional} must be a string")

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


def reconcile_in_flight(state: dict[str, Any]) -> list[str]:
    uncertain: list[str] = []
    for item in state.get("in_flight", []):
        if isinstance(item, dict) and item.get("status") == "running":
            item["status"] = "uncertain"
            uncertain.append(item.get("id", "<unknown>"))
    return uncertain


def _load_valid_state(path: Path) -> dict[str, Any]:
    state = read_state(path)
    errors = validate_state(state)
    if errors:
        raise ValueError("invalid state:\n" + "\n".join(errors))
    return state


def checkpoint_state(
    path: Path,
    *,
    goal: str | None,
    next_action: str,
    in_flight: dict[str, str] | None = None,
) -> dict[str, Any]:
    if path.exists():
        state = _load_valid_state(path)
    else:
        if not goal:
            raise ValueError("--goal is required when creating recovery state")
        state = new_state(goal, next_action)
    state["next_action"] = next_action
    if in_flight:
        items = state.setdefault("in_flight", [])
        items[:] = [item for item in items if item.get("id") != in_flight["id"]]
        items.append(in_flight)
    write_state(path, state)
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

    checkpoint_parser = subparsers.add_parser("checkpoint")
    checkpoint_parser.add_argument("path", type=Path)
    checkpoint_parser.add_argument("--goal")
    checkpoint_parser.add_argument("--next-action", required=True)
    checkpoint_parser.add_argument("--in-flight-id")
    checkpoint_parser.add_argument("--kind", choices=sorted(IN_FLIGHT_KINDS))
    checkpoint_parser.add_argument("--target")
    checkpoint_parser.add_argument("--resume-action")
    checkpoint_parser.add_argument("--external-id")

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
            uncertain = reconcile_in_flight(state)
            stale = reconcile_state(state, args.repo.resolve())
            if args.write and (stale or uncertain):
                write_state(args.path, state)
            print(f"Stale evidence: {len(stale)}")
            for evidence_id in stale:
                print(f"- {evidence_id}")
            print(f"Uncertain in-flight work: {len(uncertain)}")
            for item_id in uncertain:
                print(f"- {item_id}")
        elif args.command == "checkpoint":
            supplied = (args.in_flight_id, args.kind, args.target, args.resume_action)
            if (any(supplied) and not all(supplied)) or (
                args.external_id and not all(supplied)
            ):
                raise ValueError(
                    "--in-flight-id, --kind, --target, and --resume-action must be supplied together"
                )
            in_flight = None
            if all(supplied):
                in_flight = {
                    "id": args.in_flight_id,
                    "kind": args.kind,
                    "target": args.target,
                    "status": "running",
                    "resume_action": args.resume_action,
                    "started_at": datetime.now(timezone.utc).isoformat(),
                }
                if args.external_id:
                    in_flight["external_id"] = args.external_id
            checkpoint_state(
                args.path,
                goal=args.goal,
                next_action=args.next_action,
                in_flight=in_flight,
            )
            print(f"Checkpointed {args.path}")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
