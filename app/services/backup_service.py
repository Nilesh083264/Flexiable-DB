"""
File: app/services/backup_service.py
Responsibility: Orchestrates database utility operations
Responsibility: Orchestrates backup workflow
"""

from app.infrastructure.factory.db_factory import DBFactory
from app.core.aop import log_execution
from app.domain.models.backup_metadata import BackupMetadata


class BackupService:

    @log_execution
    def check_db_connection(self) -> bool:
        checker = DBFactory.get_connection_checker()
        return checker.check_connection()


    @log_execution
    def trigger_backup(self, db_type: str):
        engine = DBFactory.get_backup_engine(db_type)
        return engine.execute_backup()







