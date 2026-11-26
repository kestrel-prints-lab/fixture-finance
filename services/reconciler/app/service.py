"""Business logic of reconciler. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def enqueue(body: dict) -> dict:
    key = str(body.get("id", "batch-001"))
    record = {"id": key}
    record["rebuild_statements"] = clients.rebuild_statements({"ref": key, **body})
    store.save_batch(key, record)
    return record


def status(batch_id: str) -> dict:
    record = store.get_batch(batch_id) or {"id": batch_id}
    record["ledger_entry"] = clients.ledger_entry(str(record.get("entry_id", "entry-001")))
    return record


def run_now(body: dict) -> dict:
    key = str(body.get("id", "batch-001"))
    record = {"id": key}
    record["rebuild_statements"] = clients.rebuild_statements({"ref": key, **body})
    record["items"] = store.list_batch_records()
    return record
