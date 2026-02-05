"""
File: app/infrastructure/backup/postgres_backup.py
Responsibility: PostgreSQL backup implementation
"""

import subprocess
import os
from pathlib import Path
from app.infrastructure.backup.base_backup import BaseBackup
from app.core.config import settings
from app.core.exceptions import BackupOperationException


class PostgresBackup(BaseBackup):

    db_type = "postgres"

    def _perform_backup(self, backup_path: Path) -> None:
        output_file = backup_path / "backup.sql"

        # Prepare environment for pg_dump (non-interactive auth)
        env = os.environ.copy()
        env["PGPASSWORD"] = settings.POSTGRES_PASSWORD

        try:
            subprocess.run(
                [
                    "pg_dump",
                    "-h", settings.POSTGRES_HOST,
                    "-U", settings.POSTGRES_USER,
                    "-d", settings.POSTGRES_DB,
                    "-f", str(output_file),
                ],
                env=env,
                check=True,
            )
        except Exception as exc:
            raise BackupOperationException(
                f"PostgreSQL backup failed: {exc}"
            )
