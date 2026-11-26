# fixture-finance

Finance services (Python, FastAPI and Flask). A **test fixture** for an internal, read-only
architecture-inventory tool (Phase A). It contains ordinary business code, no vulnerable code, and is not meant to be run against.

Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Edit the topology, not these files.

| Folder | Framework | Build |
|---|---|---|
| `services/ledger/` | fastapi | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/tax/` | flask | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/fx-rates/` | fastapi | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/fraud/` | flask | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/reconciler/` | fastapi | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/statements/` | flask | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |
| `services/payouts/` | fastapi | build.yml context ${{ matrix.dir }}, matrix include entry pinned by the image name |

Licence: MIT.
