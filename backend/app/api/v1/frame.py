from fastapi import APIRouter, HTTPException, UploadFile, status

router = APIRouter()


@router.post("/save", status_code=status.HTTP_201_CREATED)
async def save_frame(frame: UploadFile, contains_weapon: bool):
    """Save a screenshot from a user specifying some having/not having gun in frame"""
    if not frame:
        raise HTTPException(status_code=400, detail="No frame provided")

    # TODO: save to database
