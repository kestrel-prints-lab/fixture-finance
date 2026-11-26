"""HTTP routes of tax. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from flask import Blueprint, jsonify, request

from . import service

bp = Blueprint("tax", __name__)


@bp.get("/rates/<region>")
def get_rate(region: str):
    result = service.get_rate(region)
    return jsonify(result)


@bp.get("/regions")
def list_regions():
    result = service.list_regions()
    return jsonify(result)


@bp.post("/rates/<region>")
def update_rate(region: str):
    body = request.get_json(silent=True) or {}
    result = service.update_rate(region, body)
    return jsonify(result)
