"""Business logic of ledger. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def post_entry(body: dict) -> dict:
    key = str(body.get("id", "entry-001"))
    record = {"id": key}
    record["amount"] = to_minor_units(body.get("amount", "1.00"))
    record["fx_rate"] = clients.fx_rate(str(body.get("currency", "currency-001")))
    record["queue_reconcile"] = clients.queue_reconcile({"ref": key, **body})
    record["reconcile_status"] = clients.reconcile_status(str(body.get("batch_id", "batch-001")))
    store.save_entry(key, record)
    return record


def get_entry(entry_id: str) -> dict:
    record = store.get_entry(entry_id) or {"id": entry_id}
    return record


def list_entries() -> dict:
    key = "all"
    record = {"id": key}
    record["items"] = store.list_entry_records()
    return record


def balance(account_id: str) -> dict:
    record = {"id": account_id}
    record["items"] = store.list_entry_records()
    return record
