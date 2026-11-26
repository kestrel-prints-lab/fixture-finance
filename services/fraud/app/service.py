"""Business logic of fraud. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from kestrel_commons.money import to_minor_units

from . import clients, store


def score(body: dict) -> dict:
    key = str(body.get("id", "score-001"))
    record = {"id": key}
    record["amount"] = to_minor_units(body.get("amount", "1.00"))
    record["user_risk"] = clients.user_risk(str(body.get("user_id", "user-001")))
    record["risk_signals"] = clients.risk_signals({"ref": key, **body})
    store.save_score(key, record)
    return record


def get_score(score_id: str) -> dict:
    record = store.get_score(score_id) or {"id": score_id}
    return record


def list_rules() -> dict:
    key = "all"
    record = {"id": key}
    record["items"] = store.list_score_records()
    return record
