from __future__ import annotations

import os
import sys
from pathlib import Path
from wsgiref.simple_server import make_server


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app import create_app


server = make_server(
    "127.0.0.1",
    int(os.environ["PORT"]),
    create_app(os.environ["DATABASE"]),
)
server.serve_forever()
