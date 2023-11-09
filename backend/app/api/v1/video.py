from urllib import response
from fastapi import APIRouter, UploadFile, HTTPException, status

from models.video import GetStreamResponse, NewStreamRequest, Stream

router = APIRouter()


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_video(video: UploadFile):
    """Upload a video to the server and proccess it to check for firearms"""
    pass


@router.post("/stream", status_code=status.HTTP_201_CREATED, response_class=Stream)
async def add_new_stream(data: NewStreamRequest):
    """Add a new camera rtsp stream"""
    url = data.url
    if not url.startswith("rtsp://"):
        raise HTTPException(
            status_code=400, detail="Invalid RTSP URL, should start with rtsp://"
        )

    return {"id": 1, "url": url}


@router.get("/stream", response_class=GetStreamResponse, status_code=status.HTTP_200_OK)
async def get_streams():
    """Get a list of all the streams (cameras and videos? or only cameras)"""
    return {
        "streams": [
            {"id": 1, "url": "https://stream.net/stream-url-1"},
            {"id": 2, "url": "https://stream.net/stream-url-2"},
        ]
    }
