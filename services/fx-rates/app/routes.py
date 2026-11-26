"""HTTP routes of fx-rates. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from fastapi import APIRouter

from . import service

router = APIRouter()


@router.get("/{currency}")
def get_rate(currency: str) -> dict:
    result = service.get_rate(currency)
    return result


@router.post("/refresh")
def refresh(body: dict | None = None) -> dict:
    body = body or {}
    result = service.refresh(body)
    return result


@router.get("/currencies/all")
def list_currencies() -> dict:
    result = service.list_currencies()
    return result
