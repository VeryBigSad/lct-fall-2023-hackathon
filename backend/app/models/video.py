from pydantic import BaseClass


class Stream(BaseClass):
    id: int
    url: str


class GetStreamResponse(BaseClass):
    streams: list[Stream]


class NewStreamRequest(BaseClass):
    url: str
