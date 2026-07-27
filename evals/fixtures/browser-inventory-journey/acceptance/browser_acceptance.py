from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def main() -> int:
    node = os.environ.get("JARVIS_NODE") or shutil.which("node")
    if not node:
        print("node executable unavailable", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:
        port = free_port()
        environment = os.environ.copy()
        environment["PORT"] = str(port)
        environment["DATABASE"] = str(Path(directory) / "inventory.sqlite3")
        environment["BASE_URL"] = f"http://127.0.0.1:{port}"
        server = subprocess.Popen(
            [sys.executable, str(ROOT / "acceptance" / "server.py")],
            cwd=ROOT,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            for _ in range(50):
                if server.poll() is not None:
                    stdout, stderr = server.communicate()
                    print(stdout, file=sys.stderr)
                    print(stderr, file=sys.stderr)
                    return 1
                try:
                    with urlopen(environment["BASE_URL"], timeout=0.2) as response:
                        if response.status == 200:
                            break
                except OSError:
                    time.sleep(0.1)
            else:
                print("inventory server did not become ready", file=sys.stderr)
                return 1

            browser = subprocess.run(
                [node, str(ROOT / "acceptance" / "browser_flow.js")],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            sys.stdout.write(browser.stdout)
            sys.stderr.write(browser.stderr)
            return browser.returncode
        finally:
            server.terminate()
            try:
                server.wait(timeout=3)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait(timeout=3)


if __name__ == "__main__":
    raise SystemExit(main())
