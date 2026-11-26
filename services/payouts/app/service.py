"""Business logic of payouts. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def schedule(body: dict) -> dict:
    key = str(body.get("id", "payout-001"))
    record = {"id": key}
    record["amount"] = to_minor_units(body.get("amount", "1.00"))
    record["bank_transfer"] = clients.bank_transfer({"ref": key, **body})
    record["payout_digest"] = clients.payout_digest({"ref": key, **body})
    store.save_payout(key, record)
    return record


def get_payout(payout_id: str) -> dict:
    record = store.get_payout(payout_id) or {"id": payout_id}
    return record


def list_payouts(batch_id: str) -> dict:
    record = {"id": batch_id}
    record["items"] = store.list_payout_records()
    return record
