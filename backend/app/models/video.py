from pydantic import BaseModel


class CameraStreamModel(BaseModel):
    id: int
    rstp_url: str


class CameraStreamListResponse(BaseModel):
    streams: list[CameraStreamModel]


class NewStreamRequest(BaseModel):
    url: str
