"""HTTP routes of statements. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from flask import Blueprint, jsonify, request

from . import service

bp = Blueprint("statements", __name__)


@bp.post("/rebuild")
def rebuild():
    body = request.get_json(silent=True) or {}
    result = service.rebuild(body)
    return jsonify(result)


@bp.get("/<statement_id>")
def get_statement(statement_id: str):
    result = service.get_statement(statement_id)
    return jsonify(result)


@bp.get("/account/<account_id>")
def list_statements(account_id: str):
    result = service.list_statements(account_id)
    return jsonify(result)
