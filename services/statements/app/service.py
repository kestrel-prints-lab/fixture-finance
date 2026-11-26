"""Business logic of statements. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def rebuild(body: dict) -> dict:
    key = str(body.get("id", "statement-001"))
    record = {"id": key}
    record["schedule_payout"] = clients.schedule_payout({"ref": key, **body})
    store.save_statement(key, record)
    return record


def get_statement(statement_id: str) -> dict:
    record = store.get_statement(statement_id) or {"id": statement_id}
    return record


def list_statements(account_id: str) -> dict:
    record = {"id": account_id}
    record["items"] = store.list_statement_records()
    return record
