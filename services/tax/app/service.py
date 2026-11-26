"""Business logic of tax. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def get_rate(region: str) -> dict:
    record = store.get_rate(region) or {"id": region}
    record["fx_rate"] = clients.fx_rate(str(record.get("currency", "currency-001")))
    return record


def list_regions() -> dict:
    key = "all"
    record = {"id": key}
    record["items"] = store.list_rate_records()
    return record


def update_rate(region: str, body: dict) -> dict:
    record = {"id": region}
    record["amount"] = to_minor_units(body.get("amount", "1.00"))
    store.save_rate(region, record)
    return record
