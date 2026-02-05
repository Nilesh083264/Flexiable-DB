"""
File: app/infrastructure/backup/mongo_backup.py
Responsibility: MongoDB backup implementation
"""

import subprocess
from pathlib import Path
from app.infrastructure.backup.base_backup import BaseBackup
from app.core.config import settings
from app.core.exceptions import BackupOperationException


class MongoBackup(BaseBackup):

    db_type = "mongo"

    def _perform_backup(self, backup_path: Path) -> None:
        try:
            subprocess.run(
                [
                    "mongodump",
                    "--uri", settings.MONGO_URI,
                    "--out", str(backup_path)
                ],
                check=True
            )
        except Exception as exc:
            raise BackupOperationException(
                f"MongoDB backup failed: {exc}"
            )
