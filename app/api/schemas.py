"""
File: app/api/schemas.py
Responsibility: API request/response schemas
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Literal,List


class BackupRequest(BaseModel):
    db_type: Literal["mongo", "postgres"]



class HealthResponse(BaseModel):
    status: str


class DBHealthResponse(BaseModel):
    db_connected: bool


class BackupResponse(BaseModel):
    backup_id: str
    db_type: str
    timestamp: datetime
    status: str
    location: str


class ListBackupsResponse(BaseModel):
    backups: List[BackupResponse]

