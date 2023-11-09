from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post("/upload")
async def upload_video(video: UploadFile = File(...)):
    # Your logic to save and process the video file goes here
    return {"filename": video.filename}

@router.post("/stream")
async def stream_video(rtspUrl: str):
    # Your logic to handle the RTSP stream link goes here
    if not rtspUrl.startswith("rtsp://"):
        raise HTTPException(status_code=400, detail="Invalid RTSP URL")
    return {"rtspUrl": rtspUrl}

