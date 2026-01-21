from sqlalchemy.exc import IntegrityError
from app.db.models import Event


def save_event(db, event_id, event_type, payload):
    event = Event(
        id=event_id, 
        event_type=event_type, 
        payload=payload, 
        status="RECEIVED"
        )
    
    try:
        db.add(event)
        db.commit()
        return event, True
    except IntegrityError:
        db.rollback()
        return None, False
    