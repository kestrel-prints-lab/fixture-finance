"""Outbound HTTP calls made by tax. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

import os

import requests

FX_URL = os.environ["FX_URL"]


def fx_rate(currency: str) -> dict:
    resp = requests.get(f"{FX_URL}/v1/fx/{currency}", timeout=5)
    return resp.json()
