"""In-memory SQLite storage for entry records. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import json
import sqlite3

_conn = sqlite3.connect(":memory:", check_same_thread=False)


def init_db() -> None:
    _conn.execute("CREATE TABLE IF NOT EXISTS t_entry (id TEXT PRIMARY KEY, body TEXT)")


def get_entry(key: str) -> dict | None:
    row = _conn.execute("SELECT body FROM t_entry WHERE id = ?", (key,)).fetchone()
    return json.loads(row[0]) if row else None


def save_entry(key: str, record: dict) -> None:
    _conn.execute("INSERT OR REPLACE INTO t_entry VALUES (?, ?)", (key, json.dumps(record)))


def list_entry_records() -> list[dict]:
    return [json.loads(r[0]) for r in _conn.execute("SELECT body FROM t_entry ORDER BY id")]


def delete_entry(key: str) -> None:
    _conn.execute("DELETE FROM t_entry WHERE id = ?", (key,))
