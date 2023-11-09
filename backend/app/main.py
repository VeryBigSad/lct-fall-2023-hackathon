import uvicorn

from core.settings import config_parameters


def main():
    if config_parameters.IS_PROD:
        uvicorn.run(
            "setup:server",
            host=config_parameters.API_HOST,
            port=config_parameters.API_PORT,
            loop="uvloop",
            reload=False,
            use_colors=True,
        )
    else:
        uvicorn.run(
            "setup:server",
            host=config_parameters.API_HOST,
            port=config_parameters.API_PORT,
            loop="asyncio",
            reload=True,
            use_colors=True,
        )


if __name__ == "__main__":
    main()
