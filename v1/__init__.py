from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mongoengine

from config import config
from v1.routes import router


def create_app():
    app = FastAPI(
        title=config.SERVICE_NAME.replace("_", " "),
        description=config.SERVICE_DESCRIPTION,
        version=config.VERSION,
        openapi_url="/api/v1/{}/openapi.json".format(config.SUBROUTE),
        docs_url="/api/v1/{}/docs".format(config.SUBROUTE),
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # DATABASE_HOST = config.DATABASE_HOST
    # print("DATABASE_HOST",DATABASE_HOST)

    # mongoengine.connect(db="Device",
    #     host="mongodb://admin:%40ccessDenied321@192.168.1.42:27017/marketplace?authSource=admin")

    # mongoengine.connect(
    #     config.DATABASE_NAME,
    #     host="mongodb://{}:{}@{}:{}/?authSource={}&readPreference=primary&directConnection=true&ssl=false".format(
    #         config.DATABASE_USERNAME,
    #         config.DATABASE_PASSWORD,
    #         config.DATABASE_HOST,
    #         27017,
    #         config.DATABASE_AUTHENTICATION_SOURCE,
    #     ),
    # )

    mongoengine.connect(
        db=config.DATABASE_NAME,  # Replace with your actual DB name
        host="mongodb://localhost:27017",
    )

    app.include_router(router, prefix="/api/v1/device")

    return app


app = create_app()
