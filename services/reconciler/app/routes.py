"""HTTP routes of reconciler. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from fastapi import APIRouter

from . import service

router = APIRouter()


@router.post("/queue")
def enqueue(body: dict | None = None) -> dict:
    body = body or {}
    result = service.enqueue(body)
    return result


@router.get("/status/{batch_id}")
def status(batch_id: str) -> dict:
    result = service.status(batch_id)
    return result


@router.post("/run")
def run_now(body: dict | None = None) -> dict:
    body = body or {}
    result = service.run_now(body)
    return result
