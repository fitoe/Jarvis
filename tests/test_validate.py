from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import (
    SKILLS,
    parse_frontmatter,
    validate_eval_file,
    validate_repo,
    validate_trigger_evals,
)
from scripts.package_skills import package_skills


ROOT = Path(__file__).resolve().parents[1]


class ValidateRepositoryTests(unittest.TestCase):
    def test_current_repository_is_valid(self) -> None:
        self.assertEqual(validate_repo(ROOT), [])

    def test_jarvis_has_behavior_evals(self) -> None:
        for skill_name in SKILLS:
            path = ROOT / "skills" / skill_name / "evals" / "evals.json"
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(payload["evals"]), 10, skill_name)

    def test_frontmatter_parser_reads_name_and_description(self) -> None:
        values = parse_frontmatter(
            "---\nname: sample\ndescription: A sufficiently useful description.\n---\n"
        )
        self.assertEqual(values["name"], "sample")
        self.assertIn("useful", values["description"])

    def test_eval_validator_rejects_duplicate_ids(self) -> None:
        payload = {
            "skill_name": "sample",
            "evals": [
                {
                    "id": 1,
                    "prompt": "one",
                    "expected_output": "one",
                    "expectations": ["a", "b"],
                    "tags": ["test"],
                },
                {
                    "id": 1,
                    "prompt": "two",
                    "expected_output": "two",
                    "expectations": ["a", "b"],
                    "tags": ["test"],
                },
                {
                    "id": 3,
                    "prompt": "three",
                    "expected_output": "three",
                    "expectations": ["a", "b"],
                    "tags": ["test"],
                },
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "evals.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            errors = validate_eval_file(path, "sample")
        self.assertTrue(any("unique integer id" in error for error in errors))

    def test_trigger_evals_cover_positive_and_negative_cases(self) -> None:
        path = ROOT / "skills" / "jarvis" / "evals" / "trigger-evals.json"
        self.assertEqual(validate_trigger_evals(path), [])
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertIn(True, {item["should_trigger"] for item in payload})
        self.assertIn(False, {item["should_trigger"] for item in payload})

    def test_packaged_skills_are_standalone(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            packages = package_skills(ROOT, Path(directory))
            self.assertEqual(len(packages), len(SKILLS))
            for package in packages:
                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                self.assertNotIn("../../core/", skill_text)
                self.assertTrue((package / "references" / "core").is_dir())
                self.assertTrue((package / "references" / "capabilities").is_dir())
                self.assertTrue((package / "scripts" / "state.py").is_file())


if __name__ == "__main__":
    unittest.main()
