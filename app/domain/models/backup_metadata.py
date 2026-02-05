"""
File: app/domain/models/backup_metadata.py
Responsibility: Represents metadata of a backup operation
"""

from datetime import datetime
from pydantic import BaseModel


class BackupMetadata(BaseModel):
    backup_id: str
    db_type: str
    timestamp: datetime
    status: str
    location: str
