from fastapi import APIRouter, status
from app.schemas.events import EventIngestRequest, EventIngestResponse

router = APIRouter(prefix="/v1/events", tags=["Events"])

@router.post("/{event_type}", response_model=EventIngestResponse)
def ingest_event(event_type: str, event: EventIngestRequest):
    return EventIngestResponse(
        status="accepted", 
        event_id=event.event_id
    )
