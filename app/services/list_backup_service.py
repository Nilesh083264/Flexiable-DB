"""
File: app/services/list_backup_service.py
Responsibility: Read-only service to list existing backups from filesystem
"""

from pathlib import Path
from datetime import datetime
from typing import List
from app.domain.models.backup_metadata import BackupMetadata


class ListBackupService:

    def list_backups(self, db_type: str) -> List[BackupMetadata]:
        base_path = Path("backups") / db_type

        if not base_path.exists():
            return []

        backups: List[BackupMetadata] = []

        for backup_dir in sorted(base_path.iterdir(), reverse=True):
            if not backup_dir.is_dir():
                continue

            try:
                timestamp_str = backup_dir.name.replace("Backup_", "")
                timestamp = datetime.strptime(
                    timestamp_str, "%Y-%m-%d_%H-%M-%S"
                )
            except ValueError:
                continue

            backups.append(
                BackupMetadata(
                    backup_id=backup_dir.name,
                    db_type=db_type,
                    timestamp=timestamp,
                    status="AVAILABLE",
                    location=str(backup_dir),
                )
            )

        return backups
