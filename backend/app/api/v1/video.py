from urllib import response
from fastapi import APIRouter, UploadFile, HTTPException, status
from database.models.stream import CameraStream

from models.video import CameraStreamListResponse, NewStreamRequest, CameraStreamModel

router = APIRouter()


@router.post(
    "/stream", status_code=status.HTTP_201_CREATED, response_model=CameraStreamModel
)
async def add_new_stream(data: NewStreamRequest):
    """Add a new camera rtsp stream"""
    url = data.url
    if not url.startswith("rtsp://"):
        raise HTTPException(
            status_code=400, detail="Invalid RTSP URL, should start with rtsp://"
        )
    # create new stream
    camera_stream = await CameraStream.create(rtsp_url=data.url)

    return camera_stream


@router.get(
    "/stream", status_code=status.HTTP_200_OK, response_model=CameraStreamListResponse
)
async def get_streams():
    """Get a list of all the streams (cameras and videos? or only cameras)"""
    streams = await CameraStream.filter(is_active=True)
    return CameraStreamListResponse(
        streams=CameraStreamModel.model_validate(streams, from_attributes=True)
    )


@router.get("/stream/{stream_id}/")
async def get_stream(stream_id: int):
    """Returns a stream that can be put in <video> tag"""
    pass



@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_video(video: UploadFile):
    """Upload a video to the server and proccess it to check for firearms"""
    pass
