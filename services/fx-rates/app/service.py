"""Business logic of fx-rates. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def get_rate(currency: str) -> dict:
    record = store.get_rate(currency) or {"id": currency}
    record["provider_rates"] = clients.provider_rates()
    return record


def refresh(body: dict) -> dict:
    key = str(body.get("id", "rate-001"))
    record = {"id": key}
    record["provider_rates"] = clients.provider_rates()
    store.save_rate(key, record)
    return record


def list_currencies() -> dict:
    key = "all"
    record = {"id": key}
    record["items"] = store.list_rate_records()
    return record
