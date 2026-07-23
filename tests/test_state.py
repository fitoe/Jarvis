from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.state import new_state, reconcile_state, validate_state, write_state


class DeliveryStateTests(unittest.TestCase):
    def test_new_state_is_valid(self) -> None:
        state = new_state("Ship the first useful slice", "Inspect local truth")
        self.assertEqual(validate_state(state), [])

    def test_duplicate_side_effect_keys_are_rejected(self) -> None:
        state = new_state("Publish", "Check remote")
        state["side_effects"] = [
            {
                "id": "S1",
                "action": "create_repository",
                "target": "owner/repo",
                "idempotency_key": "github:owner/repo",
                "status": "confirmed",
                "evidence": "https://github.com/owner/repo",
            },
            {
                "id": "S2",
                "action": "create_repository",
                "target": "owner/repo",
                "idempotency_key": "github:owner/repo",
                "status": "planned",
                "evidence": "",
            },
        ]
        errors = validate_state(state)
        self.assertTrue(any("duplicate side-effect idempotency_key" in item for item in errors))

    def test_reconcile_marks_evidence_stale_when_dependency_changed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            subprocess.run(
                ["git", "init", "-b", "main"],
                cwd=repo,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.email", "jarvis@example.test"],
                cwd=repo,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Jarvis Test"],
                cwd=repo,
                check=True,
            )
            dependency = repo / "src" / "orders.py"
            dependency.parent.mkdir()
            dependency.write_text("TOTAL = 1\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(
                ["git", "commit", "-m", "initial"],
                cwd=repo,
                check=True,
                capture_output=True,
            )
            commit = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=repo,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            state = new_state("Orders work", "Continue")
            state["evidence"] = [
                {
                    "id": "E1",
                    "claim_id": "C1",
                    "kind": "test",
                    "status": "fresh",
                    "commit": commit,
                    "checked_at": "2026-07-24T00:00:00Z",
                    "environment": "test",
                    "command": "python -m unittest",
                    "depends_on": ["src/orders.py"],
                    "result": "passed",
                }
            ]
            dependency.write_text("TOTAL = 2\n", encoding="utf-8")

            stale = reconcile_state(state, repo)
            self.assertEqual(stale, ["E1"])
            self.assertEqual(state["evidence"][0]["status"], "stale")

    def test_write_state_is_valid_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "current.json"
            write_state(path, new_state("Goal", "Next"))
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["goal"], "Goal")

    def test_reconcile_rejects_non_git_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                reconcile_state(new_state("Goal", "Next"), Path(directory))


if __name__ == "__main__":
    unittest.main()
