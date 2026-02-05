"""
File: app/infrastructure/backup/base_backup.py
Responsibility: Template method defining backup workflow and folder structure
"""

import uuid
from datetime import datetime
from pathlib import Path
from app.domain.interfaces.backup_interface import BackupInterface
from app.domain.models.backup_metadata import BackupMetadata
from app.core.logger import logger


class BaseBackup(BackupInterface):

    db_type: str  # must be defined by subclass

    def execute_backup(self) -> BackupMetadata:
        backup_id = str(uuid.uuid4())[:8]
        timestamp = datetime.utcnow()
        backup_folder = self._create_backup_folder(timestamp)

        logger.info(
            f"Backup started | backup_id={backup_id} | "
            f"db_type={self.db_type} | path={backup_folder}"
        )

        self._perform_backup(backup_folder)

        metadata = BackupMetadata(
            backup_id=backup_id,
            db_type=self.db_type,
            timestamp=timestamp,
            status="SUCCESS",
            location=str(backup_folder),
        )

        logger.info(
            f"Backup completed | backup_id={backup_id} | "
            f"db_type={self.db_type}"
        )
        return metadata

    def _create_backup_folder(self, timestamp: datetime) -> Path:
        folder_name = f"Backup_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}"
        path = Path("backups") / self.db_type / folder_name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _perform_backup(self, backup_path: Path) -> None:
        """Implemented by concrete backup engines"""
        raise NotImplementedError
