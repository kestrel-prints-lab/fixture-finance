"""HTTP routes of fraud. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from flask import Blueprint, jsonify, request

from . import service

bp = Blueprint("fraud", __name__)


@bp.post("/score")
def score():
    body = request.get_json(silent=True) or {}
    result = service.score(body)
    return jsonify(result)


@bp.get("/score/<score_id>")
def get_score(score_id: str):
    result = service.get_score(score_id)
    return jsonify(result)


@bp.get("/rules")
def list_rules():
    result = service.list_rules()
    return jsonify(result)
