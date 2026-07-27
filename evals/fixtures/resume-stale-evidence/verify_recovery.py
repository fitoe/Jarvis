from __future__ import annotations

import json
from pathlib import Path


state = json.loads((Path(__file__).parent / "project-state" / "current.json").read_text(encoding="utf-8"))
evidence = state["evidence"][0]
if evidence.get("status") != "stale":
    raise SystemExit("E1 must be marked stale after its dependency changes")
if "complete" in state.get("next_action", "").lower():
    raise SystemExit("next_action must not preserve the unsupported completion claim")
print("Recovery evidence reconciled")
