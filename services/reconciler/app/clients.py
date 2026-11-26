"""Outbound HTTP calls made by reconciler. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import httpx

STATEMENTS_URL = os.environ["STATEMENTS_URL"]
LEDGER_URL = os.environ["LEDGER_URL"]

_http = httpx.Client(timeout=5.0)


def rebuild_statements(payload: dict) -> dict:
    resp = _http.post(f"{STATEMENTS_URL}/v1/statements/rebuild", json=payload)
    return resp.json()


def ledger_entry(entry_id: str) -> dict:
    resp = _http.get(f"{LEDGER_URL}/v1/entries/{entry_id}")
    return resp.json()
