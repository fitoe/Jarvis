from __future__ import annotations

import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from wsgiref.simple_server import make_server

from app import create_app


class InventoryJourneyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        database = str(Path(self.temporary.name) / "inventory.sqlite3")
        self.server = make_server("127.0.0.1", 0, create_app(database))
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()
        self.temporary.cleanup()

    def request(self, method: str, path: str, payload: dict | None = None):
        data = json.dumps(payload).encode() if payload is not None else None
        request = Request(
            self.base_url + path,
            data=data,
            method=method,
            headers={"Content-Type": "application/json"},
        )
        with urlopen(request) as response:
            return response.status, json.loads(response.read())

    def test_receive_use_and_read_persisted_stock(self) -> None:
        self.assertEqual(self.request("POST", "/receive", {"sku": "bolt", "quantity": 8})[0], 201)
        self.assertEqual(self.request("POST", "/use", {"sku": "bolt", "quantity": 3})[0], 200)
        status, body = self.request("GET", "/stock/bolt")
        self.assertEqual(status, 200)
        self.assertEqual(body, {"sku": "bolt", "quantity": 5})

        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()
        self.server = make_server("127.0.0.1", 0, create_app(str(Path(self.temporary.name) / "inventory.sqlite3")))
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_port}"
        self.assertEqual(self.request("GET", "/stock/bolt")[1]["quantity"], 5)

    def test_rejects_using_more_than_available(self) -> None:
        self.request("POST", "/receive", {"sku": "nut", "quantity": 2})
        with self.assertRaises(HTTPError) as error:
            self.request("POST", "/use", {"sku": "nut", "quantity": 3})
        self.assertEqual(error.exception.code, 409)
        self.assertEqual(self.request("GET", "/stock/nut")[1]["quantity"], 2)


if __name__ == "__main__":
    unittest.main()
