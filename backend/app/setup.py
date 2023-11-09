import asyncio

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.settings import config_parameters
from database import init_database
from api import root_api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="MISIS Magnolia API",
        debug=not config_parameters.IS_PROD,
        # docs_url=None,
        # redoc_url=None,
        # openapi_url=None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    return app


try:
    import uvloop

    uvloop.install()
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

server = create_app()
server.include_router(root_api_router, prefix="/api")
init_database(server)
