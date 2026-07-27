from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import (
    REQUIRED_PATHS,
    SKILLS,
    parse_frontmatter,
    validate_canary_file,
    validate_eval_file,
    validate_repo,
    validate_trigger_evals,
)
from scripts.package_skills import package_skills


ROOT = Path(__file__).resolve().parents[1]


class ValidateRepositoryTests(unittest.TestCase):
    def test_comparative_claims_require_paired_evidence(self) -> None:
        policy = (ROOT / "core" / "evidence-policy.md").read_text(encoding="utf-8")
        for phrase in (
            "same raw task",
            "same repository state",
            "human intervention",
            "rework",
            "elapsed time",
            "visual drift",
            "side effects",
        ):
            self.assertIn(phrase, policy)

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

    def test_delivery_canaries_have_real_fixture_acceptance(self) -> None:
        path = ROOT / "evals" / "delivery-canaries.json"
        self.assertEqual(validate_canary_file(path, ROOT), [])
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(payload["canaries"]), 2)

    def test_packaged_skills_are_standalone(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            packages = package_skills(ROOT, Path(directory))
            self.assertEqual(len(packages), len(SKILLS))
            for package in packages:
                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                self.assertNotIn("../../core/", skill_text)
                self.assertTrue((package / "references" / "core").is_dir())
                self.assertTrue((package / "references" / "capabilities").is_dir())
                self.assertTrue(
                    (
                        package
                        / "references"
                        / "examples"
                        / "lead-operations"
                        / "docs"
                        / "pages"
                        / "lead-list"
                        / "development.md"
                    ).is_file()
                )
                self.assertTrue((package / "scripts" / "state.py").is_file())
                self.assertTrue((package / "evals" / "evals.json").is_file())

    def test_document_first_resources_replace_packet_templates(self) -> None:
        required = set(REQUIRED_PATHS)
        for path in (
            "templates/product-plan.md",
            "templates/page-overview.md",
            "templates/development-guide.md",
        ):
            self.assertIn(path, required)
            self.assertTrue((ROOT / path).is_file(), path)

        for path in (
            "core/slice-contract.md",
            "templates/active-slice.md",
            "templates/slice-packet.json",
            "templates/delegated-task.json",
        ):
            self.assertNotIn(path, required)
            self.assertFalse((ROOT / path).exists(), path)

    def test_jarvis_skill_uses_document_first_context(self) -> None:
        text = (ROOT / "skills" / "jarvis" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "Product Plan",
            "Page Overview",
            "Development Guide",
            "context-closure",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("Slice Packet", text)
        self.assertNotIn("Delegated Task Packet", text)

    def test_document_first_behavior_evals_are_present(self) -> None:
        path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for required_tag in (
            "document-first",
            "context-closure",
            "truth-ownership",
            "shared-boundary",
            "read-only-dry-run",
        ):
            self.assertIn(required_tag, tags)

    def test_page_overview_is_optional_and_discriminated(self) -> None:
        skill_text = (ROOT / "skills" / "jarvis" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Page Overview is optional", skill_text)

        template_text = (ROOT / "templates" / "development-guide.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "Page overview: optional",
            "## Page purpose and journey position",
            "## Entry, exit, and navigation",
        ):
            self.assertIn(phrase, template_text)

        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        cases = [
            case
            for case in payload["evals"]
            if "optional-page-overview" in case["tags"]
        ]
        self.assertGreaterEqual(len(cases), 2)
        combined = " ".join(
            case["expected_output"] + " " + " ".join(case["expectations"])
            for case in cases
        )
        self.assertIn("omit", combined.lower())
        self.assertIn("keep", combined.lower())

    def test_lead_list_golden_example_is_context_closed(self) -> None:
        example_root = ROOT / "examples" / "lead-operations" / "docs"
        product_plan = example_root / "product-plan.md"
        overview = example_root / "pages" / "lead-list" / "overview.md"
        development = example_root / "pages" / "lead-list" / "development.md"

        for path in (product_plan, overview, development):
            self.assertTrue(path.is_file(), path)

        text = development.read_text(encoding="utf-8")
        for phrase in (
            "## Current development goal",
            "owner and status filters",
            "loading, empty, error, and retry",
            "Lead Detail",
            "## Acceptance criteria",
            "## Verification",
            "## When to stop and request more context",
            "needs-context",
        ):
            self.assertIn(phrase, text)

    def test_page_and_project_verification_contract_is_explicit(self) -> None:
        verification = (ROOT / "core" / "verification-policy.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Select test level",
            "## Select verification scope",
            "## Verification cadence",
            "Focused gate",
            "Affected gate",
            "Journey gate",
            "Release gate",
        ):
            self.assertIn(phrase, verification)

        product_build = (ROOT / "capabilities" / "product-build.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "Batch related edits",
            "coherent checkpoint",
            "Avoid repeated compile-test loops",
        ):
            self.assertIn(phrase, product_build)

        product_plan = (ROOT / "templates" / "product-plan.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Critical journey verification", product_plan)
        self.assertIn("## Project verification gates", product_plan)

        development = (ROOT / "templates" / "development-guide.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "| Acceptance claim | Claim type | Risk | Evidence |", development
        )

        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for tag in (
            "focused-gate",
            "affected-gate",
            "journey-gate",
            "release-gate",
            "batched-verification",
            "early-check",
        ):
            self.assertIn(tag, tags)

    def test_human_efficient_collaboration_contract_is_explicit(self) -> None:
        relative = "core/collaboration-policy.md"
        self.assertIn(relative, REQUIRED_PATHS)

        policy_path = ROOT / relative
        self.assertTrue(policy_path.is_file(), policy_path)
        policy = policy_path.read_text(encoding="utf-8")
        for phrase in (
            "## Communicate at material events",
            "## Accept correction without friction",
            "## Hand off outcome first",
        ):
            self.assertIn(phrase, policy)

        skill = (ROOT / "skills" / "jarvis" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Collaboration Policy", skill)
        self.assertIn("../../core/collaboration-policy.md", skill)

        autonomy = (ROOT / "core" / "autonomy-policy.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Respond to steering",
            "**Redirect:**",
            "**Pause:**",
            "**Resume:**",
            "**Cancel:**",
        ):
            self.assertIn(phrase, autonomy)

        decision = (ROOT / "core" / "decision-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Resolve instruction and preference precedence", decision)
        self.assertIn("current explicit user instruction", decision)
        self.assertIn(
            "stable preference stated in the current conversation", decision
        )

        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for tag in ("steering", "pause-resume-cancel", "preference-precedence"):
            self.assertIn(tag, tags)

        operating = (ROOT / "core" / "operating-model.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Work economically",
            "batch independent read-only discovery",
            "Retry only when the next attempt changes a relevant condition",
        ):
            self.assertIn(phrase, operating)

        provider = (ROOT / "core" / "provider-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Do not reload unchanged provider instructions", provider)
        self.assertIn("setup cost", provider)

        for tag in ("execution-economy", "changed-condition", "degraded-progress"):
            self.assertIn(tag, tags)

        quality = (ROOT / "core" / "code-quality-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Activate quality overlays only when relevant", quality)
        for phrase in (
            "Accessibility",
            "Performance",
            "Security and privacy",
            "Operability",
            "Compatibility",
        ):
            self.assertIn(phrase, quality)

        verification = (ROOT / "core" / "verification-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "An active quality overlay selects the smallest check", verification
        )
        self.assertIn("quality-overlay", tags)

    def test_loop_engineering_contract_is_explicit(self) -> None:
        operating = (ROOT / "core" / "operating-model.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Keep one Loop Contract",
            "## Steer by goal-directed heuristics",
            "Stop discovery when",
            "## Run the finite delivery loop",
            "### Discover",
            "### Frame",
            "### Execute",
            "### Observe",
            "### Verify",
            "### Record",
            "### Continue or stop",
            "## Keep nested evidence scopes",
            "## Terminate honestly",
        ):
            self.assertIn(phrase, operating)

        skill = (ROOT / "skills" / "jarvis" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Run Loop Engineering", skill)
        self.assertIn("## Refine toward the goal", skill)
        for move in (
            "Discover",
            "Frame",
            "Execute",
            "Observe",
            "Verify",
            "Record",
            "Continue or stop",
        ):
            self.assertIn(move, skill)

        autonomy = (ROOT / "core" / "autonomy-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Start and reconcile host Goals", autonomy)
        self.assertIn("explicit request", autonomy)

        provider = (ROOT / "core" / "provider-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Use providers as observation boundaries", provider)
        self.assertIn("visible built-in browser", provider)

        delegation = (ROOT / "core" / "delegation-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("## Activate independent checking by risk", delegation)
        self.assertIn("does not reimplement", delegation)
        self.assertIn(
            "## Route delegated work to the least capable sufficient model",
            delegation,
        )
        self.assertIn("Do not invent a model identifier", delegation)

        budget = (ROOT / "core" / "budget-policy.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Budget exhausted is a stop condition", budget)

        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for tag in (
            "loop-discover",
            "loop-frame",
            "loop-observe",
            "evidence-driven-reframe",
            "risk-based-checker",
            "nested-evidence",
            "light-spine",
            "loop-termination",
            "finite-loop",
            "model-routing",
            "heuristic-steering",
            "progressive-refinement",
            "capability-probe",
            "checkpoint",
            "in-flight",
        ):
            self.assertIn(tag, tags)

        old_spec = (
            ROOT
            / "docs"
            / "superpowers"
            / "specs"
            / "2026-07-26-autonomous-goal-browser-workbench-design.md"
        ).read_text(encoding="utf-8")
        old_plan = (
            ROOT
            / "docs"
            / "superpowers"
            / "plans"
            / "2026-07-26-autonomous-goal-browser-workbench.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Status: superseded", old_spec)
        self.assertIn("Status: superseded", old_plan)

    def test_visual_maturity_loop_is_explicit(self) -> None:
        visual = (ROOT / "core" / "visual-source-policy.md").read_text(
            encoding="utf-8"
        )
        for phrase in (
            "## Mature the design source before approval",
            "Correct behavior",
            "Classify the largest blocking mismatch",
            "single targeted edit",
            "implementation-ready",
        ):
            self.assertIn(phrase, visual)

        eval_path = ROOT / "skills" / "jarvis" / "evals" / "evals.json"
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        tags = {tag for case in payload["evals"] for tag in case["tags"]}
        for tag in (
            "visual-maturity",
            "ux-before-polish",
            "reference-driven-direction",
            "targeted-image-edit",
            "truth-ownership",
        ):
            self.assertIn(tag, tags)

        self.assertNotIn("Visual Source Record", visual)
        self.assertNotIn("Slice Packet", visual)


if __name__ == "__main__":
    unittest.main()
