from pydantic import BaseModel, Field
from typing import Dict, Any
from uuid import UUID
from datetime import datetime


class EventIngestRequest(BaseModel):
    event_id: UUID
    timestamp: datetime
    payload: Dict[str, Any]

class EventIngestResponse(BaseModel):
    status: str
    event_id: UUID
