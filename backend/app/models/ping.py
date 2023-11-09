from pydantic import BaseModel


class PingRequest(BaseModel):
    url: str
