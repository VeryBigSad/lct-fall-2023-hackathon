from pydantic import BaseModel


class Stream(BaseModel):
    id: int
    url: str


class GetStreamResponse(BaseModel):
    streams: list[Stream]


class NewStreamRequest(BaseModel):
    url: str
