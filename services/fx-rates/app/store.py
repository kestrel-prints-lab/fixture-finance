"""In-memory SQLite storage for rate records. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import json
import sqlite3

_conn = sqlite3.connect(":memory:", check_same_thread=False)


def init_db() -> None:
    _conn.execute("CREATE TABLE IF NOT EXISTS t_rate (id TEXT PRIMARY KEY, body TEXT)")


def get_rate(key: str) -> dict | None:
    row = _conn.execute("SELECT body FROM t_rate WHERE id = ?", (key,)).fetchone()
    return json.loads(row[0]) if row else None


def save_rate(key: str, record: dict) -> None:
    _conn.execute("INSERT OR REPLACE INTO t_rate VALUES (?, ?)", (key, json.dumps(record)))


def list_rate_records() -> list[dict]:
    return [json.loads(r[0]) for r in _conn.execute("SELECT body FROM t_rate ORDER BY id")]


def delete_rate(key: str) -> None:
    _conn.execute("DELETE FROM t_rate WHERE id = ?", (key,))
