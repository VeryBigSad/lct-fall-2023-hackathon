from fastapi import APIRouter, HTTPException, UploadFile

router = APIRouter()


@router.post("/save")
async def save_frame(frame: UploadFile, contains_weapon: bool):
    # Your logic to save the frame and process it for weapon detection goes here
    # For example, you could save the frame to a file storage and then
    # run your weapon detection algorithm
    if not frame:
        raise HTTPException(status_code=400, detail="No frame provided")

    # Process the frame and determine whether it contains a weapon
    # Here you would integrate your weapon detection logic

    # This is just a placeholder for the real implementation
    weapon_detected = contains_weapon  # Replace with actual detection logic

    return {"frame_name": frame.filename, "weapon_detected": weapon_detected}


# You can add more endpoints related to frames as needed
