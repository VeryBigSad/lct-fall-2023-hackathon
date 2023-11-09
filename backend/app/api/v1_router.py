# app/api/api_v1.py
from fastapi import APIRouter

from .v1 import frame, ping, video

api_v1_router = APIRouter()
api_v1_router.include_router(frame.router, prefix="/frame", tags=["frame"])
api_v1_router.include_router(ping.router, prefix="/ping", tags=["ping"])
api_v1_router.include_router(video.router, prefix="/video", tags=["video"])

# You can add more routers as your application grows
