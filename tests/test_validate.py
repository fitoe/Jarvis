from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import SKILLS, parse_frontmatter, validate_eval_file, validate_repo
from scripts.package_skills import package_skills


ROOT = Path(__file__).resolve().parents[1]


class ValidateRepositoryTests(unittest.TestCase):
    def test_current_repository_is_valid(self) -> None:
        self.assertEqual(validate_repo(ROOT), [])

    def test_all_skills_have_three_or_more_evals(self) -> None:
        for skill_name in SKILLS:
            path = ROOT / "skills" / skill_name / "evals" / "evals.json"
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(payload["evals"]), 3, skill_name)

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
                },
                {
                    "id": 1,
                    "prompt": "two",
                    "expected_output": "two",
                    "expectations": ["a", "b"],
                },
                {
                    "id": 3,
                    "prompt": "three",
                    "expected_output": "three",
                    "expectations": ["a", "b"],
                },
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "evals.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            errors = validate_eval_file(path, "sample")
        self.assertTrue(any("unique integer id" in error for error in errors))

    def test_packaged_skills_are_standalone(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            packages = package_skills(ROOT, Path(directory))
            self.assertEqual(len(packages), len(SKILLS))
            for package in packages:
                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                self.assertNotIn("../../core/", skill_text)
                self.assertTrue((package / "references" / "core").is_dir())


if __name__ == "__main__":
    unittest.main()
