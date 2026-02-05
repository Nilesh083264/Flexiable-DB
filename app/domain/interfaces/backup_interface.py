"""
File: app/domain/interfaces/backup_interface.py
Responsibility: Contract for database backup operations
"""

from abc import ABC, abstractmethod
from app.domain.models.backup_metadata import BackupMetadata


class BackupInterface(ABC):

    @abstractmethod
    def execute_backup(self) -> BackupMetadata:
        """Execute database backup and return metadata"""
        pass
