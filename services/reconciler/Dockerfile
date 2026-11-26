# reconciler. Generated from testenv/topology/topology.yaml by testenv/topology/generate.js. Do not edit by hand.
# Built with the service folder as the context.
FROM python:3.12-slim
WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app

USER 10001
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
