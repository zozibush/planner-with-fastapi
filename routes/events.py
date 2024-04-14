from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags = ["Events"]
)

events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_events() -> List[Event]:
    return events
