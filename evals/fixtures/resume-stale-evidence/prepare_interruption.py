from __future__ import annotations

import json
import subprocess
from pathlib import Path


root = Path(__file__).resolve().parent
commit = subprocess.run(
    ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
).stdout.strip()
path = root / "project-state" / "current.json"
state = json.loads(path.read_text(encoding="utf-8"))
state["evidence"][0]["commit"] = commit
path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
(root / "src" / "pricing.py").write_text(
    "RATE = 2\n\n\ndef total(quantity: int) -> int:\n    return quantity * RATE\n",
    encoding="utf-8",
)
