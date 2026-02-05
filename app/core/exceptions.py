"""
File: app/core/exceptions.py
Responsibility: Centralized application exception definitions
"""

from typing import Optional


class AppException(Exception):
    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int,
        details: Optional[str] = None,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details
        super().__init__(message)


class DatabaseConnectionException(AppException):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="DB_CONNECTION_ERROR",
            status_code=503,
        )


class BackupOperationException(AppException):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="BACKUP_ERROR",
            status_code=500,
        )
