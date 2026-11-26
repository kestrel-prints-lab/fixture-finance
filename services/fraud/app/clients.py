"""Outbound HTTP calls made by fraud. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import requests

IDENTITY_URL = os.environ["IDENTITY_URL"]
RISK_SIGNALS_BASE = "https://api.example.com"


def user_risk(user_id: str) -> dict:
    resp = requests.get(f"{IDENTITY_URL}/v1/users/{user_id}/risk", timeout=5)
    return resp.json()


def risk_signals(payload: dict) -> dict:
    resp = requests.post(f"{RISK_SIGNALS_BASE}/v1/risk-signals", json=payload, timeout=5)
    return resp.json()
