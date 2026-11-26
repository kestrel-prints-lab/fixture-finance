"""reconciler: Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand."""

from fastapi import FastAPI

from . import store
from .routes import router

app = FastAPI(title="reconciler")
app.include_router(router, prefix="/v1/reconcile")
store.init_db()


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}
