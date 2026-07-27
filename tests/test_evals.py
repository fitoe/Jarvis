from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.run_evals import (
    DEFAULT_BEHAVIOR_EVALS,
    _run_streaming_process,
    _snapshot_protected_paths,
    _summarize_codex_event,
    check_environment,
    load_behavior_cases,
    load_canaries,
    probe_capabilities,
    run_codex,
    run_behavior_case,
    run_canary,
    validate_grade,
)


ROOT = Path(__file__).resolve().parents[1]


class ExecutableEvalTests(unittest.TestCase):
    def test_codex_inherits_the_evaluation_runtime_environment(self) -> None:
        process_result = {"returncode": 0, "stdout": "", "stderr": ""}
        with patch(
            "scripts.run_evals._run_streaming_process", return_value=process_result
        ) as runner:
            run_codex(
                "Do the work",
                cwd=ROOT,
                sandbox="read-only",
                model=None,
                timeout=10,
            )
        environment = runner.call_args.kwargs["env"]
        self.assertEqual(
            Path(environment["PATH"].split(os.pathsep)[0]),
            Path(sys.executable).resolve().parent,
        )
        self.assertEqual(environment.get("NODE_PATH"), check_environment().get("NODE_PATH"))

    def test_streaming_process_emits_events_and_heartbeats(self) -> None:
        events: list[str] = []
        progress: list[str] = []
        result = _run_streaming_process(
            [
                sys.executable,
                "-c",
                "import time; print('event', flush=True); time.sleep(0.2)",
            ],
            cwd=ROOT,
            timeout=2,
            on_stdout=events.append,
            progress=progress.append,
            heartbeat_label="test process",
            heartbeat_interval=0.05,
        )
        self.assertEqual(result["returncode"], 0)
        self.assertEqual(events, ["event"])
        self.assertTrue(any("still running" in item for item in progress))

    def test_codex_events_are_summarized_without_command_output(self) -> None:
        line = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "python verify.py",
                    "aggregated_output": "large private output",
                    "status": "completed",
                },
            }
        )
        summary = _summarize_codex_event(line)
        self.assertIn("python verify.py", summary)
        self.assertNotIn("large private output", summary)

    def test_behavior_cases_filter_by_id_and_tag(self) -> None:
        cases = load_behavior_cases(DEFAULT_BEHAVIOR_EVALS, ids={82}, tags={"provider"})
        self.assertEqual([case["id"] for case in cases], [82])

    def test_behavior_case_requires_judged_expectations(self) -> None:
        case = {
            "id": 1,
            "prompt": "Do the work",
            "expected_output": "Safe delivery",
            "expectations": ["Uses evidence"],
        }
        candidate = {"returncode": 0, "response": "I used evidence.", "events": [], "stderr": ""}
        judge = {
            "returncode": 0,
            "response": json.dumps(
                {
                    "case_id": 1,
                    "passed": True,
                    "expectations": [
                        {"expectation": "Uses evidence", "passed": True, "evidence": "used evidence"}
                    ],
                    "summary": "passed",
                }
            ),
            "events": [],
            "stderr": "",
        }
        with patch("scripts.run_evals.run_codex", side_effect=[candidate, judge]):
            result = run_behavior_case(
                case, root=ROOT, model=None, judge_model=None, timeout=10
            )
        self.assertEqual(result["status"], "passed")

    def test_grade_cannot_pass_with_missing_expectations(self) -> None:
        case = {"expectations": ["One", "Two"]}
        grade = {"passed": True, "expectations": []}
        self.assertTrue(validate_grade(case, grade))

    def test_capability_probe_keeps_host_only_capabilities_unverified(self) -> None:
        capabilities = probe_capabilities()["capabilities"]
        self.assertIn(capabilities["codex_exec"]["status"], {"available", "unavailable"})
        self.assertEqual(capabilities["host_browser"]["status"], "unverified")
        self.assertEqual(capabilities["image2"]["status"], "unverified")
        self.assertEqual(capabilities["host_goal"]["status"], "unverified")

    def test_canary_rejects_agent_success_when_acceptance_fails(self) -> None:
        case = load_canaries(ROOT / "evals" / "delivery-canaries.json")[1]
        candidate = {"returncode": 0, "response": "done", "events": [], "stderr": ""}
        with patch("scripts.run_evals.run_codex", return_value=candidate):
            result = run_canary(case, model=None, timeout=30)
        self.assertEqual(result["status"], "failed")

    def test_canary_rejects_modified_acceptance_files(self) -> None:
        case = load_canaries(ROOT / "evals" / "delivery-canaries.json")[1]

        def cheat(_prompt, *, cwd, **_kwargs):
            (cwd / "verify_recovery.py").write_text("print('fake pass')\n", encoding="utf-8")
            return {"returncode": 0, "response": "done", "events": [], "stderr": ""}

        with patch("scripts.run_evals.run_codex", side_effect=cheat):
            result = run_canary(case, model=None, timeout=30)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["protected_changes"], ["verify_recovery.py"])

    def test_generated_python_cache_is_not_acceptance_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            tests = workspace / "tests"
            tests.mkdir()
            (tests / "test_flow.py").write_text("PASS = True\n", encoding="utf-8")
            before = _snapshot_protected_paths(workspace, ["tests"])
            cache = tests / "__pycache__"
            cache.mkdir()
            (cache / "test_flow.cpython-312.pyc").write_bytes(b"generated")
            after = _snapshot_protected_paths(workspace, ["tests"])
        self.assertEqual(before, after)

    def test_canary_accepts_only_observable_recovery_result(self) -> None:
        case = load_canaries(ROOT / "evals" / "delivery-canaries.json")[1]

        def reconcile(_prompt, *, cwd, **_kwargs):
            path = cwd / "project-state" / "current.json"
            state = json.loads(path.read_text(encoding="utf-8"))
            state["evidence"][0]["status"] = "stale"
            state["next_action"] = "Re-run the affected price verification"
            path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            return {"returncode": 0, "response": "reconciled", "events": [], "stderr": ""}

        with patch("scripts.run_evals.run_codex", side_effect=reconcile):
            result = run_canary(case, model=None, timeout=30)
        self.assertEqual(result["status"], "passed")

    def test_canary_rechecks_after_one_evidence_driven_repair(self) -> None:
        case = load_canaries(ROOT / "evals" / "delivery-canaries.json")[1]
        calls = 0

        def repair(_prompt, *, cwd, **_kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                path = cwd / "project-state" / "current.json"
                state = json.loads(path.read_text(encoding="utf-8"))
                state["evidence"][0]["status"] = "stale"
                state["next_action"] = "Re-run affected verification"
                path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            return {"returncode": 0, "response": "attempted", "events": [], "stderr": ""}

        with patch("scripts.run_evals.run_codex", side_effect=repair):
            result = run_canary(case, model=None, timeout=30)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(len(result["repairs"]), 1)

    def test_canary_can_keep_a_numbered_workspace(self) -> None:
        case = load_canaries(ROOT / "evals" / "delivery-canaries.json")[1]
        candidate = {"returncode": 0, "response": "done", "events": [], "stderr": ""}
        with tempfile.TemporaryDirectory() as directory:
            with patch("scripts.run_evals.run_codex", return_value=candidate):
                result = run_canary(
                    case,
                    model=None,
                    timeout=30,
                    keep_workspace=Path(directory),
                )
            self.assertEqual(Path(result["workspace"]).name, "2")


if __name__ == "__main__":
    unittest.main()
