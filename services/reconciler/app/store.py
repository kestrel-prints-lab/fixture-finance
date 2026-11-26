"""In-memory SQLite storage for batch records. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import json
import sqlite3

_conn = sqlite3.connect(":memory:", check_same_thread=False)


def init_db() -> None:
    _conn.execute("CREATE TABLE IF NOT EXISTS t_batch (id TEXT PRIMARY KEY, body TEXT)")


def get_batch(key: str) -> dict | None:
    row = _conn.execute("SELECT body FROM t_batch WHERE id = ?", (key,)).fetchone()
    return json.loads(row[0]) if row else None


def save_batch(key: str, record: dict) -> None:
    _conn.execute("INSERT OR REPLACE INTO t_batch VALUES (?, ?)", (key, json.dumps(record)))


def list_batch_records() -> list[dict]:
    return [json.loads(r[0]) for r in _conn.execute("SELECT body FROM t_batch ORDER BY id")]


def delete_batch(key: str) -> None:
    _conn.execute("DELETE FROM t_batch WHERE id = ?", (key,))
