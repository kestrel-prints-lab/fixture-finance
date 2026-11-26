"""Outbound HTTP calls made by fx-rates. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import httpx

PROVIDER_RATES_BASE = "https://api.example.com"

_http = httpx.Client(timeout=5.0)


def provider_rates() -> dict:
    resp = _http.get(f"{PROVIDER_RATES_BASE}/v1/fx")
    return resp.json()
