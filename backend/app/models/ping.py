from pydantic import BaseClass


class PingRequest(BaseClass):
    url: str
