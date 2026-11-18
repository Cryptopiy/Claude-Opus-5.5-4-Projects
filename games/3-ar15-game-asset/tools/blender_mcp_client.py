#!/usr/bin/env python3
"""Minimal JSON-over-TCP client for the 'MCP for Blender' addon (localhost:9878).

The addon speaks newline-free JSON objects on a raw socket: send one JSON
object, receive one JSON object. We keep a single persistent connection so
the addon's main-thread queue stays warm.
"""
import json
import socket
import sys

HOST = "127.0.0.1"
PORT = 9878


class BlenderMCP:
    def __init__(self, host=HOST, port=PORT, timeout=600.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None

    def connect(self):
        self.sock = socket.create_connection((self.host, self.port), timeout=15.0)
        self.sock.settimeout(self.timeout)
        return self

    def close(self):
        if self.sock:
            try:
                self.sock.close()
            except OSError:
                pass
            self.sock = None

    def send(self, cmd_type, **params):
        if self.sock is None:
            self.connect()
        payload = json.dumps({"type": cmd_type, "params": params}).encode("utf-8")
        self.sock.sendall(payload)
        buf = b""
        while True:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise RuntimeError("connection closed by Blender MCP before a full response")
            buf += chunk
            try:
                return json.loads(buf.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                continue

    def code(self, source):
        """Run a bpy snippet; print() output comes back in result['output']."""
        return self.send("execute_code", code=source)

    def __enter__(self):
        return self.connect()

    def __exit__(self, *exc):
        self.close()


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "ping":
        with BlenderMCP() as b:
            print(json.dumps(b.send("ping"), indent=2))
        return
    if len(sys.argv) > 1 and sys.argv[1] == "scene":
        with BlenderMCP() as b:
            print(json.dumps(b.send("get_scene_info"), indent=2)[:4000])
        return
    if len(sys.argv) > 2 and sys.argv[1] == "run":
        with BlenderMCP() as b:
            r = b.code(open(sys.argv[2], encoding="utf-8").read())
            print(json.dumps(r, indent=2)[:20000])
        return
    print(__doc__)


if __name__ == "__main__":
    main()
