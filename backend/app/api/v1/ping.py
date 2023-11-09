from typing import Optional
from fastapi import APIRouter, HTTPException, BackgroundTasks, status

from models.ping import PingRequest

router = APIRouter()


@router.post("/ping", status_code=status.HTTP_201_CREATED)
async def ping_detection(data: PingRequest):
    """Save a url and ping it every time we get a new detection"""
    pass


# Add more endpoints as needed
