"""HTTP routes of ledger. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from fastapi import APIRouter

from . import service

router = APIRouter()


@router.post("/entries")
def post_entry(body: dict | None = None) -> dict:
    body = body or {}
    result = service.post_entry(body)
    return result


@router.get("/entries/{entry_id}")
def get_entry(entry_id: str) -> dict:
    result = service.get_entry(entry_id)
    return result


@router.get("/entries")
def list_entries() -> dict:
    result = service.list_entries()
    return result


@router.get("/accounts/{account_id}/balance")
def balance(account_id: str) -> dict:
    result = service.balance(account_id)
    return result
