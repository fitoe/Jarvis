from __future__ import annotations

import json
import sqlite3
from urllib.parse import parse_qs


def create_app(database: str):
    """Return a WSGI app for the inventory journey."""
    raise NotImplementedError
