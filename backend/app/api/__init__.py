from fastapi import APIRouter
from api.v1_router import api_v1_router

root_api_router = APIRouter()
root_api_router.include_router(api_v1_router, prefix="/v1")


@root_api_router.get("/")
async def health():
    return {"status": "ok"}
