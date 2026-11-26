"""Outbound HTTP calls made by payouts. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import httpx

DIGEST_URL = os.environ["DIGEST_URL"]
BANK_TRANSFER_BASE = "https://api.example.com"

_http = httpx.Client(timeout=5.0)


def bank_transfer(payload: dict) -> dict:
    resp = _http.post(f"{BANK_TRANSFER_BASE}/v1/transfers", json=payload)
    return resp.json()


def payout_digest(payload: dict) -> dict:
    resp = _http.post(f"{DIGEST_URL}/v1/messages", json=payload)
    return resp.json()
