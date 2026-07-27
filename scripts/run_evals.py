from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BEHAVIOR_EVALS = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
DEFAULT_CANARIES = ROOT / "evals" / "delivery-canaries.json"
JUDGE_SCHEMA = ROOT / "evals" / "judge-schema.json"
HEARTBEAT_INTERVAL = 30.0


def _progress(message: str) -> None:
    print(message, flush=True)


def _summarize_codex_event(line: str) -> str:
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        return line[:240]
    event_type = event.get("type", "event")
    item = event.get("item")
    if not isinstance(item, dict):
        return event_type
    item_type = item.get("type", "item")
    if item_type == "agent_message":
        text = " ".join(str(item.get("text", "")).split())
        return f"agent message: {text[:200]}"
    if item_type == "command_execution":
        command = " ".join(str(item.get("command", "")).split())
        status = item.get("status", "completed")
        return f"command {status}: {command[:180]}"
    if item_type == "error":
        message = " ".join(str(item.get("message", "")).split())
        return f"error: {message[:200]}"
    return f"{event_type}: {item_type}"


def _run_streaming_process(
    command: list[str],
    *,
    cwd: Path,
    timeout: int,
    env: dict[str, str] | None = None,
    input_text: str | None = None,
    on_stdout: Callable[[str], None] | None = None,
    progress: Callable[[str], None] = _progress,
    heartbeat_label: str,
    heartbeat_interval: float = HEARTBEAT_INTERVAL,
) -> dict[str, Any]:
    process = subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        stdin=subprocess.PIPE if input_text is not None else subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    stdout_lines: list[str] = []
    stderr_lines: list[str] = []

    def drain(
        stream: Any,
        sink: list[str],
        callback: Callable[[str], None] | None = None,
    ) -> None:
        for line in stream:
            sink.append(line)
            if callback and line.strip():
                callback(line.rstrip("\r\n"))
        stream.close()

    stdout_thread = threading.Thread(
        target=drain, args=(process.stdout, stdout_lines, on_stdout), daemon=True
    )
    stderr_thread = threading.Thread(
        target=drain, args=(process.stderr, stderr_lines), daemon=True
    )
    stdout_thread.start()
    stderr_thread.start()
    if process.stdin is not None:
        process.stdin.write(input_text or "")
        process.stdin.close()

    started = time.monotonic()
    next_heartbeat = started + heartbeat_interval
    try:
        while process.poll() is None:
            now = time.monotonic()
            elapsed = now - started
            if elapsed >= timeout:
                raise subprocess.TimeoutExpired(command, timeout)
            if now >= next_heartbeat:
                progress(f"{heartbeat_label}: still running ({int(elapsed)}s)")
                next_heartbeat = now + heartbeat_interval
            try:
                process.wait(
                    timeout=min(1.0, heartbeat_interval, timeout - elapsed)
                )
            except subprocess.TimeoutExpired:
                pass
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
        raise
    finally:
        stdout_thread.join()
        stderr_thread.join()
    return {
        "returncode": process.returncode,
        "stdout": "".join(stdout_lines),
        "stderr": "".join(stderr_lines),
    }


def _bundled_node_root() -> Path:
    return (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "node"
    )


def check_environment() -> dict[str, str]:
    environment = os.environ.copy()
    existing_path = environment.get("PATH")
    path_entries = [str(Path(sys.executable).resolve().parent)]
    if existing_path:
        path_entries.append(existing_path)
    environment["PATH"] = os.pathsep.join(path_entries)
    bundled_modules = _bundled_node_root() / "node_modules"
    if bundled_modules.is_dir():
        existing = environment.get("NODE_PATH")
        search_paths = [bundled_modules]
        pnpm_root = bundled_modules / ".pnpm"
        for pattern in ("playwright@*/node_modules", "playwright-core@*/node_modules"):
            search_paths.extend(sorted(pnpm_root.glob(pattern)))
        if existing:
            search_paths.append(Path(existing))
        environment["NODE_PATH"] = os.pathsep.join(str(path) for path in search_paths)
    environment["JARVIS_NODE"] = node_executable()
    return environment


def node_executable() -> str:
    bundled = _bundled_node_root() / "bin" / ("node.exe" if os.name == "nt" else "node")
    return str(bundled) if bundled.is_file() else (shutil.which("node") or "node")


def probe_capabilities() -> dict[str, Any]:
    environment = check_environment()
    node = node_executable()
    playwright = subprocess.run(
        [
            node,
            "-e",
            "const {chromium}=require('playwright'); process.stdout.write(chromium?'loaded':'missing')",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=environment,
        check=False,
    )
    browser_candidates = [
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    ]
    browser = next((path for path in browser_candidates if path.is_file()), None)
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "capabilities": {
            "codex_exec": {
                "status": "available" if shutil.which("codex") else "unavailable",
                "evidence": shutil.which("codex") or "codex executable not found",
            },
            "playwright": {
                "status": "available" if playwright.returncode == 0 else "unavailable",
                "evidence": playwright.stdout or playwright.stderr.strip(),
            },
            "browser_executable": {
                "status": "available" if browser else "unavailable",
                "evidence": str(browser) if browser else "supported browser executable not found",
            },
            "host_browser": {
                "status": "unverified",
                "evidence": "Desktop built-in browser availability must be inspected in the active host session",
            },
            "image2": {
                "status": "unverified",
                "evidence": "CLI probe cannot safely prove the host Image 2 tool without generation",
            },
            "host_goal": {
                "status": "unverified",
                "evidence": "Goal capability must be inspected in the active host session",
            },
            "subagents": {
                "status": "unverified",
                "evidence": "Subagent models and limits must be inspected in the active host session",
            },
        },
    }


def load_behavior_cases(
    path: Path, ids: set[int] | None = None, tags: set[str] | None = None
) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    cases = payload["evals"]
    if ids:
        cases = [case for case in cases if case["id"] in ids]
    if tags:
        cases = [case for case in cases if tags.intersection(case["tags"])]
    return cases


def load_canaries(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["canaries"]


def _codex_command(
    *,
    cwd: Path,
    sandbox: str,
    output_path: Path,
    model: str | None,
    schema: Path | None = None,
) -> list[str]:
    executable = shutil.which("codex") or "codex"
    command = [
        executable,
        "exec",
        "--ephemeral",
        "--color",
        "never",
        "--sandbox",
        sandbox,
        "--skip-git-repo-check",
        "-C",
        str(cwd),
        "--output-last-message",
        str(output_path),
        "--json",
    ]
    if model:
        command.extend(["--model", model])
    if schema:
        command.extend(["--output-schema", str(schema)])
    command.append("-")
    return command


def run_codex(
    prompt: str,
    *,
    cwd: Path,
    sandbox: str,
    model: str | None,
    timeout: int,
    schema: Path | None = None,
    label: str = "Codex",
) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="jarvis-eval-output-") as directory:
        output_path = Path(directory) / "last-message.txt"
        command = _codex_command(
            cwd=cwd,
            sandbox=sandbox,
            output_path=output_path,
            model=model,
            schema=schema,
        )
        process = _run_streaming_process(
            command,
            cwd=cwd,
            env=check_environment(),
            timeout=timeout,
            input_text=prompt,
            on_stdout=lambda line: _progress(
                f"{label}: {_summarize_codex_event(line)}"
            ),
            heartbeat_label=label,
        )
        response = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
        events = [line for line in process["stdout"].splitlines() if line.strip()]
        return {
            "command": command,
            "returncode": process["returncode"],
            "response": response,
            "events": events,
            "stderr": process["stderr"],
        }


def _judge_prompt(case: dict[str, Any], candidate: dict[str, Any]) -> str:
    evidence = {
        "case_id": case["id"],
        "prompt": case["prompt"],
        "expected_output": case["expected_output"],
        "expectations": case["expectations"],
        "candidate_response": candidate["response"],
        "candidate_events": candidate["events"],
    }
    return (
        "Judge the candidate only from observable response and event evidence. "
        "Do not award credit for unstated intent. Mark each supplied expectation "
        "passed or failed, quote concise evidence, and set overall passed only when "
        "every expectation passes. Return JSON matching the supplied schema.\n\n"
        + json.dumps(evidence, ensure_ascii=False, indent=2)
    )


def validate_grade(case: dict[str, Any], grade: Any) -> list[str]:
    if not isinstance(grade, dict):
        return ["grade must be an object"]
    items = grade.get("expectations")
    if not isinstance(items, list):
        return ["grade.expectations must be a list"]
    expected = case["expectations"]
    actual = [item.get("expectation") for item in items if isinstance(item, dict)]
    errors: list[str] = []
    if actual != expected:
        errors.append("judge expectations must exactly match the case expectations")
    if grade.get("passed") is not all(
        isinstance(item, dict) and item.get("passed") is True for item in items
    ):
        errors.append("overall judge result must equal all expectation results")
    return errors


def run_behavior_case(
    case: dict[str, Any],
    *,
    root: Path,
    model: str | None,
    judge_model: str | None,
    timeout: int,
) -> dict[str, Any]:
    candidate_prompt = (
        "Apply the installed Jarvis skill to this request in evaluation mode. The "
        "read-only sandbox prevents implementation and external effects; still make "
        "the same workflow, authority, provider, verification, and completion "
        "decisions you would make during execution. Report the concrete next actions "
        "and claims you would or would not accept.\n\nUser request:\n" + case["prompt"]
    )
    candidate = run_codex(
        candidate_prompt,
        cwd=root,
        sandbox="read-only",
        model=model,
        timeout=timeout,
        label=f"behavior {case['id']} candidate",
    )
    result: dict[str, Any] = {"case_id": case["id"], "candidate": candidate}
    if candidate["returncode"] != 0:
        result["status"] = "candidate-error"
        return result

    with tempfile.TemporaryDirectory(prefix="jarvis-eval-judge-") as directory:
        judge = run_codex(
            _judge_prompt(case, candidate),
            cwd=Path(directory),
            sandbox="read-only",
            model=judge_model or model,
            timeout=timeout,
            schema=JUDGE_SCHEMA,
            label=f"behavior {case['id']} judge",
        )
    result["judge"] = judge
    if judge["returncode"] != 0:
        result["status"] = "judge-error"
        return result
    try:
        grade = json.loads(judge["response"])
    except json.JSONDecodeError:
        result["status"] = "judge-invalid-json"
        return result
    result["grade"] = grade
    grade_errors = validate_grade(case, grade)
    if grade_errors:
        result["status"] = "judge-invalid-grade"
        result["grade_errors"] = grade_errors
        return result
    result["status"] = "passed" if grade.get("passed") is True else "failed"
    return result


def _run_check(
    command: list[str], cwd: Path, timeout: int, *, label: str = "check"
) -> dict[str, Any]:
    replacements = {"{python}": sys.executable, "{node}": node_executable()}
    expanded = [replacements.get(part, part) for part in command]
    _progress(f"{label}: started")
    process = _run_streaming_process(
        expanded,
        cwd=cwd,
        env=check_environment(),
        timeout=timeout,
        heartbeat_label=label,
    )
    status = "passed" if process["returncode"] == 0 else "failed"
    _progress(f"{label}: {status}")
    return {
        "command": expanded,
        "returncode": process["returncode"],
        "stdout": process["stdout"],
        "stderr": process["stderr"],
    }


def _snapshot_protected_paths(workspace: Path, paths: list[str]) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    resolved_workspace = workspace.resolve()
    for relative in paths:
        target = (resolved_workspace / relative).resolve()
        if target != resolved_workspace and resolved_workspace not in target.parents:
            raise ValueError(f"unsafe protected path: {relative}")
        files = [target] if target.is_file() else sorted(
            path
            for path in target.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.suffix not in {".pyc", ".pyo"}
        )
        if not files:
            snapshot[relative] = "<missing>"
            continue
        for path in files:
            key = path.relative_to(resolved_workspace).as_posix()
            snapshot[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    return snapshot


def _protected_changes(before: dict[str, str], after: dict[str, str]) -> list[str]:
    return sorted(key for key in before.keys() | after.keys() if before.get(key) != after.get(key))


def _initialize_fixture(workspace: Path) -> None:
    commands = (
        ["git", "init", "-b", "main"],
        ["git", "config", "user.email", "jarvis-canary@example.test"],
        ["git", "config", "user.name", "Jarvis Canary"],
        ["git", "add", "."],
        ["git", "commit", "-m", "canary fixture"],
    )
    for command in commands:
        process = subprocess.run(
            command, cwd=workspace, capture_output=True, text=True, check=False
        )
        if process.returncode != 0:
            raise RuntimeError(process.stderr.strip() or f"failed: {' '.join(command)}")


def run_canary(
    case: dict[str, Any],
    *,
    model: str | None,
    timeout: int,
    keep_workspace: Path | None = None,
) -> dict[str, Any]:
    fixture = (ROOT / "evals" / case["fixture"]).resolve()
    if not fixture.is_dir() or ROOT not in fixture.parents:
        raise ValueError(f"unsafe or missing fixture: {fixture}")

    temporary: tempfile.TemporaryDirectory[str] | None = None
    if keep_workspace:
        workspace = keep_workspace.resolve() / str(case["id"])
        if workspace.exists():
            raise ValueError(f"canary workspace already exists: {workspace}")
        workspace.parent.mkdir(parents=True, exist_ok=True)
    else:
        temporary = tempfile.TemporaryDirectory(
            prefix=f"jarvis-canary-{case['id']}-", ignore_cleanup_errors=True
        )
        workspace = Path(temporary.name) / "workspace"
    shutil.copytree(fixture, workspace)

    try:
        _initialize_fixture(workspace)
        prepare = [
            _run_check(
                command,
                workspace,
                timeout,
                label=f"canary {case['id']} prepare {index}",
            )
            for index, command in enumerate(case.get("prepare", []), start=1)
        ]
        if any(check["returncode"] != 0 for check in prepare):
            return {"case_id": case["id"], "status": "prepare-error", "prepare": prepare}

        protected_paths = case.get("protected_paths", [])
        protected_before = _snapshot_protected_paths(workspace, protected_paths)

        candidate = run_codex(
            case["prompt"],
            cwd=workspace,
            sandbox="workspace-write",
            model=model,
            timeout=timeout,
            label=f"canary {case['id']} candidate",
        )
        checks = [
            _run_check(
                item["command"],
                workspace,
                timeout,
                label=f"canary {case['id']} acceptance: {item['name']}",
            )
            for item in case["acceptance"]
        ]
        repairs: list[dict[str, Any]] = []
        protected_changes = _protected_changes(
            protected_before, _snapshot_protected_paths(workspace, protected_paths)
        )
        passed = (
            candidate["returncode"] == 0
            and not protected_changes
            and all(check["returncode"] == 0 for check in checks)
        )
        for attempt in range(case.get("repair_attempts", 0)):
            if passed:
                break
            failed_evidence = [
                {
                    "command": check["command"],
                    "returncode": check["returncode"],
                    "stdout": check["stdout"][-8000:],
                    "stderr": check["stderr"][-8000:],
                }
                for check in checks
                if check["returncode"] != 0
            ]
            repair_prompt = (
                "Independent acceptance rejected the current implementation. Inspect "
                "the actual workspace and failure evidence, classify the cause, make "
                "the smallest coherent repair, and rerun the affected check before "
                "claiming completion. Do not weaken or edit acceptance tests.\n\n"
                f"Repair attempt: {attempt + 1}\n"
                + json.dumps(
                    {
                        "failed_acceptance": failed_evidence,
                        "protected_paths_changed": protected_changes,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            repair = run_codex(
                repair_prompt,
                cwd=workspace,
                sandbox="workspace-write",
                model=model,
                timeout=timeout,
                label=f"canary {case['id']} repair {attempt + 1}",
            )
            repairs.append(repair)
            checks = [
                _run_check(
                    item["command"],
                    workspace,
                    timeout,
                    label=f"canary {case['id']} acceptance: {item['name']}",
                )
                for item in case["acceptance"]
            ]
            protected_changes = _protected_changes(
                protected_before, _snapshot_protected_paths(workspace, protected_paths)
            )
            passed = (
                repair["returncode"] == 0
                and not protected_changes
                and all(check["returncode"] == 0 for check in checks)
            )
        return {
            "case_id": case["id"],
            "status": "passed" if passed else "failed",
            "candidate": candidate,
            "repairs": repairs,
            "acceptance": checks,
            "protected_changes": protected_changes,
            "workspace": str(workspace) if keep_workspace else None,
        }
    finally:
        if temporary:
            temporary.cleanup()


def _write_report(path: Path, kind: str, results: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "kind": kind,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_payload(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _parse_ids(raw: str | None) -> set[int] | None:
    return {int(item) for item in raw.split(",")} if raw else None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Jarvis model behavior evals and delivery canaries"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    behavior = subparsers.add_parser("behavior")
    behavior.add_argument("--ids", help="comma-separated eval IDs")
    behavior.add_argument("--tags", help="comma-separated tags")
    behavior.add_argument("--model")
    behavior.add_argument("--judge-model")
    behavior.add_argument("--timeout", type=int, default=600)
    behavior.add_argument("--output", type=Path, required=True)

    canary = subparsers.add_parser("canary")
    canary.add_argument("--ids", help="comma-separated canary IDs")
    canary.add_argument("--model")
    canary.add_argument("--timeout", type=int, default=1200)
    canary.add_argument("--output", type=Path, required=True)
    canary.add_argument("--keep-workspaces", type=Path)

    probe = subparsers.add_parser("probe")
    probe.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()
    try:
        if args.command == "probe":
            payload = probe_capabilities()
            _write_payload(args.output, payload)
            statuses = payload["capabilities"]
            available = sum(item["status"] == "available" for item in statuses.values())
            print(
                f"Jarvis capability probe: {available}/{len(statuses)} available; "
                f"report={args.output.resolve()}"
            )
            return 0
        if args.command == "behavior":
            tags = set(args.tags.split(",")) if args.tags else None
            cases = load_behavior_cases(DEFAULT_BEHAVIOR_EVALS, _parse_ids(args.ids), tags)
            if not cases:
                raise ValueError("no behavior evals selected")
            results = []
            for case in cases:
                print(f"Running behavior eval {case['id']}...", flush=True)
                results.append(
                    run_behavior_case(
                        case,
                        root=ROOT,
                        model=args.model,
                        judge_model=args.judge_model,
                        timeout=args.timeout,
                    )
                )
                _write_report(args.output, "behavior", results)
            kind = "behavior"
        else:
            selected = _parse_ids(args.ids)
            cases = [
                case
                for case in load_canaries(DEFAULT_CANARIES)
                if not selected or case["id"] in selected
            ]
            if not cases:
                raise ValueError("no delivery canaries selected")
            results = []
            for case in cases:
                print(f"Running delivery canary {case['id']}: {case['name']}...", flush=True)
                results.append(
                    run_canary(
                        case,
                        model=args.model,
                        timeout=args.timeout,
                        keep_workspace=args.keep_workspaces,
                    )
                )
                _write_report(args.output, "canary", results)
            kind = "canary"
        _write_report(args.output, kind, results)
    except (
        OSError,
        ValueError,
        RuntimeError,
        subprocess.TimeoutExpired,
        json.JSONDecodeError,
    ) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    passed = sum(result["status"] == "passed" for result in results)
    print(f"Jarvis {kind} evals: {passed}/{len(results)} passed; report={args.output.resolve()}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
