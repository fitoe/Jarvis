from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path

if __package__:
    from scripts.validate import SKILLS, validate_markdown_links
else:
    from validate import SKILLS, validate_markdown_links


REPLACEMENTS = {
    "../../core/": "references/core/",
    "../../capabilities/": "references/capabilities/",
    "../../golden-paths/": "references/golden-paths/",
    "../../recipes/": "references/recipes/",
    "../../examples/": "references/examples/",
    "../../templates/": "references/templates/",
    "../../scripts/state.py": "scripts/state.py",
}

RESOURCE_DIRECTORIES = (
    "core",
    "capabilities",
    "golden-paths",
    "recipes",
    "examples",
    "templates",
)


def _safe_target(output_root: Path, skill_name: str) -> Path:
    resolved_root = output_root.resolve()
    target = (resolved_root / skill_name).resolve()
    if target.parent != resolved_root:
        raise ValueError(f"unsafe package target: {target}")
    return target


def package_skills(root: Path, output_root: Path) -> list[Path]:
    output_root.mkdir(parents=True, exist_ok=True)
    packages: list[Path] = []

    for skill_name in SKILLS:
        source = root / "skills" / skill_name
        target = _safe_target(output_root, skill_name)
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)

        skill_text = (source / "SKILL.md").read_text(encoding="utf-8")
        for old, new in REPLACEMENTS.items():
            skill_text = skill_text.replace(old, new)
        (target / "SKILL.md").write_text(skill_text, encoding="utf-8")

        shutil.copytree(source / "evals", target / "evals")
        (target / "scripts").mkdir()
        shutil.copy2(root / "scripts" / "state.py", target / "scripts" / "state.py")
        for resource in RESOURCE_DIRECTORIES:
            shutil.copytree(
                root / resource,
                target / "references" / resource,
            )
        packages.append(target)

    errors = validate_markdown_links(output_root)
    if errors:
        raise RuntimeError("packaged link validation failed:\n" + "\n".join(errors))
    return packages


def main() -> int:
    parser = argparse.ArgumentParser(description="Build standalone Jarvis skills")
    parser.add_argument(
        "--output",
        type=Path,
        help="output directory; defaults to repository dist/",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="build in a temporary directory and remove it after validation",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    if args.check:
        with tempfile.TemporaryDirectory(prefix="jarvis-packages-") as directory:
            packages = package_skills(root, Path(directory))
            print(f"Jarvis package check passed: {len(packages)} skill package(s)")
        return 0

    output = args.output or root / "dist"
    packages = package_skills(root, output)
    print(f"Packaged {len(packages)} skill package(s) in {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
