"""HTTP routes of payouts. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from fastapi import APIRouter

from . import service

router = APIRouter()


@router.post("/schedule")
def schedule(body: dict | None = None) -> dict:
    body = body or {}
    result = service.schedule(body)
    return result


@router.get("/{payout_id}")
def get_payout(payout_id: str) -> dict:
    result = service.get_payout(payout_id)
    return result


@router.get("/batch/{batch_id}")
def list_payouts(batch_id: str) -> dict:
    result = service.list_payouts(batch_id)
    return result
