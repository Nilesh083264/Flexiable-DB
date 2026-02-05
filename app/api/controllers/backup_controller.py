"""
File: app/api/controllers/backup_controller.py
Responsibility: Backup-related API endpoints
"""

from fastapi import APIRouter, Query
from typing import Literal
from app.services.backup_service import BackupService
from app.services.list_backup_service import ListBackupService
from app.api.schemas import BackupResponse, ListBackupsResponse

router = APIRouter()
backup_service = BackupService()
list_service = ListBackupService()


@router.post("/start", response_model=BackupResponse)
def start_backup(db_type: Literal["mongo", "postgres"]):
    return backup_service.trigger_backup(db_type)


@router.get("/list", response_model=ListBackupsResponse)
def list_backups(db_type: Literal["mongo", "postgres"] = Query(...)):
    domain_backups = list_service.list_backups(db_type)

    api_backups = [
        BackupResponse(
            backup_id=b.backup_id,
            db_type=b.db_type,
            timestamp=b.timestamp,
            status=b.status,
            location=b.location,
        )
        for b in domain_backups
    ]

    return ListBackupsResponse(backups=api_backups)
