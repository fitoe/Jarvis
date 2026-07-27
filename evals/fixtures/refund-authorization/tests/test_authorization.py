from __future__ import annotations

import json
import sqlite3
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from wsgiref.simple_server import make_server

from app import create_app


class RefundAuthorizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.database = str(Path(self.temporary.name) / "refunds.sqlite3")
        self.server = make_server("127.0.0.1", 0, create_app(self.database))
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.url = f"http://127.0.0.1:{self.server.server_port}/refunds"

    def tearDown(self) -> None:
        self.server.shutdown()
        self.thread.join(timeout=2)
        self.server.server_close()
        self.temporary.cleanup()

    def post(self, *, role: str, tenant: str, invoice: str):
        request = Request(
            self.url,
            data=json.dumps({"invoice_id": invoice, "amount": 25}).encode(),
            method="POST",
            headers={
                "Content-Type": "application/json",
                "X-Role": role,
                "X-Tenant": tenant,
            },
        )
        try:
            with urlopen(request) as response:
                return response.status
        except HTTPError as error:
            return error.code

    def refund_count(self) -> int:
        with sqlite3.connect(self.database) as connection:
            return int(connection.execute("SELECT COUNT(*) FROM refunds").fetchone()[0])

    def test_operator_is_denied_without_data_change(self) -> None:
        self.assertEqual(self.post(role="operator", tenant="alpha", invoice="A-1"), 403)
        self.assertEqual(self.refund_count(), 0)

    def test_cross_tenant_admin_is_denied_without_data_change(self) -> None:
        self.assertEqual(self.post(role="finance_admin", tenant="alpha", invoice="B-1"), 403)
        self.assertEqual(self.refund_count(), 0)

    def test_same_tenant_finance_admin_can_refund(self) -> None:
        self.assertEqual(self.post(role="finance_admin", tenant="alpha", invoice="A-1"), 201)
        self.assertEqual(self.refund_count(), 1)


if __name__ == "__main__":
    unittest.main()
