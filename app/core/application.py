from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.system.views import router as home_router
from app.api.user.views import router as user_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(api: FastAPI):
    print("Starting the application")

    yield

    print("Closing all resources and shutting down the application")


def get_app():
    api = FastAPI(
        title="HNG X Person Routes",
        description=("Dummy stuff"),
        version="0.0.1",
        lifespan=lifespan,
    )

    api.include_router(user_router)
    api.include_router(home_router)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return api
