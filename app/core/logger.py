"""
File: app/core/logger.py
Responsibility: Centralized, production-grade logging configuration
"""

import logging
import os
from contextvars import ContextVar
from app.core.config import settings

request_id_ctx: ContextVar[str] = ContextVar("request_id", default="-")

os.makedirs(settings.LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(settings.LOG_DIR, "flexible-db.log")


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_ctx.get()
        return True


LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | "
    "%(module)s | %(request_id)s | %(message)s"
)

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE),
    ],
)

logger = logging.getLogger(settings.APP_NAME)
logger.addFilter(RequestIdFilter())
