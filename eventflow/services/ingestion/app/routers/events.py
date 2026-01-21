from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.repository import save_event
from app.schemas.events import EventIngestRequest

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/v1/events", tags=["Events"])

@router.post("/{event_type}")
def ingest_event(event_type: str, event: EventIngestRequest, db: Session = Depends(get_db)):
    saved, created = save_event(
        db=db,
        event_id=event.event_id,
        event_type=event_type,
        payload=event.payload,
    )
    if not created:
        return {"status": "duplicate", "event_id": event.event_id}
    
    return {"status": "accepted", "event_id": event.event_id}
