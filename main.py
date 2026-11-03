
import logging
import time
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from controller import router
from logger_service import logger

app = FastAPI()

app.include_router(router)

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()

    try:
        response = await call_next(request)

        duration = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        logger.info(
            f"API Request: {request.method} {request.url.path} "
            f"| Status: {response.status_code} "
            f"| Duration: {duration}ms"
        )

        return response

    except Exception:
        logger.exception(
            f"Unhandled API error: {request.method} {request.url.path}"
        )
        raise


@app.get("/")
@app.get("/home")
def home():
    return FileResponse(TEMPLATES_DIR / "index.html")


@app.get("/enrollment")
def enrollment():
    return FileResponse(TEMPLATES_DIR / "enrollments.html")
