from fastapi import FastAPI
from app.routers import events
from app.middleware import request_id_middleware

app = FastAPI(title="Eventflow Ingestion Service")

app.middleware("http")(request_id_middleware)
app.include_router(events.router)
