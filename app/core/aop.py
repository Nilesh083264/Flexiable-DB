"""
File: app/core/aop.py
Responsibility: Aspect-oriented utilities (logging, timing)
"""

import time
from functools import wraps
from app.core.logger import logger


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 3)
        logger.info(f"{func.__name__} executed in {elapsed}s")
        return result
    return wrapper
