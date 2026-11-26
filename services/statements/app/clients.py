"""Outbound HTTP calls made by statements. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import requests

PAYOUTS_URL = os.environ["PAYOUTS_URL"]


def schedule_payout(payload: dict) -> dict:
    resp = requests.post(f"{PAYOUTS_URL}/v1/payouts/schedule", json=payload, timeout=5)
    return resp.json()
