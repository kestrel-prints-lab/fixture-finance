"""In-memory SQLite storage for score records. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import json
import sqlite3

_conn = sqlite3.connect(":memory:", check_same_thread=False)


def init_db() -> None:
    _conn.execute("CREATE TABLE IF NOT EXISTS t_score (id TEXT PRIMARY KEY, body TEXT)")


def get_score(key: str) -> dict | None:
    row = _conn.execute("SELECT body FROM t_score WHERE id = ?", (key,)).fetchone()
    return json.loads(row[0]) if row else None


def save_score(key: str, record: dict) -> None:
    _conn.execute("INSERT OR REPLACE INTO t_score VALUES (?, ?)", (key, json.dumps(record)))


def list_score_records() -> list[dict]:
    return [json.loads(r[0]) for r in _conn.execute("SELECT body FROM t_score ORDER BY id")]


def delete_score(key: str) -> None:
    _conn.execute("DELETE FROM t_score WHERE id = ?", (key,))
