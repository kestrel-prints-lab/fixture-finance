"""Outbound HTTP calls made by ledger. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import httpx

FX_URL = os.environ["FX_URL"]
RECONCILER_URL = os.environ["RECONCILER_URL"]

_http = httpx.Client(timeout=5.0)


def fx_rate(currency: str) -> dict:
    resp = _http.get(f"{FX_URL}/v1/fx/{currency}")
    return resp.json()


def queue_reconcile(payload: dict) -> dict:
    resp = _http.post(f"{RECONCILER_URL}/v1/reconcile/queue", json=payload)
    return resp.json()


def reconcile_status(batch_id: str) -> dict:
    resp = _http.get(f"{RECONCILER_URL}/v1/reconcile/status/{batch_id}")
    return resp.json()
