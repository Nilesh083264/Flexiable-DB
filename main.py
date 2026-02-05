"""
File: main.py
Responsibility:
- Application entry point
- Middleware registration
- Global exception handling
- API bootstrapping
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid

from app.api.routes import router as api_router
from app.core.logger import logger
from app.core.exceptions import AppException

app = FastAPI(title="Flexible Database")


# -------------------------
# Middleware: Request ID
# -------------------------
@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())[:6]
    request.state.request_id = request_id

    logger.info(
        f"Incoming request: {request.method} {request.url.path}",
        extra={"request_id": request_id},
    )

    response = await call_next(request)
    return response


# -------------------------
# Global Exception Handler
# -------------------------
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """
    Handles all application-level exceptions
    """
    logger.error(
        f"{exc.error_code} | {exc.message}",
        extra={"request_id": getattr(request.state, "request_id", None)},
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message,
        },
    )


# -------------------------
# Startup Event (will refactor in DAY 5)
# -------------------------
@app.on_event("startup")
async def startup_event():
    logger.info("Flexible Database service started")


# -------------------------
# API Routes
# -------------------------
app.include_router(api_router, prefix="/api")
