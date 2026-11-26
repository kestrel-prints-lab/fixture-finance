"""statements: Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from flask import Flask, jsonify

from . import store
from .routes import bp

app = Flask("statements")
app.register_blueprint(bp, url_prefix="/v1/statements")
store.init_db()


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")
