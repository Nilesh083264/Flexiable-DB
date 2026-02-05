"""
File: tests/services/test_backup_service.py
Responsibility: Service-level tests for BackupService
"""

from datetime import datetime
from unittest.mock import MagicMock, patch

from app.services.backup_service import BackupService
from app.domain.models.backup_metadata import BackupMetadata


def test_backup_service_triggers_correct_engine():
    """
    Verify BackupService resolves engine via factory and triggers backup
    """
    mock_metadata = BackupMetadata(
        backup_id="test123",
        db_type="mongo",
        timestamp=datetime.utcnow(),
        status="SUCCESS",
        location="backups/mongo/Backup_test",
    )

    mock_engine = MagicMock()
    mock_engine.execute_backup.return_value = mock_metadata

    with patch(
        "app.services.backup_service.DBFactory.get_backup_engine",
        return_value=mock_engine,
    ) as mock_factory:
        service = BackupService()
        result = service.trigger_backup("mongo")

        mock_factory.assert_called_once_with("mongo")
        mock_engine.execute_backup.assert_called_once()
        assert result == mock_metadata


def test_backup_service_propagates_exception():
    """
    Verify BackupService does not swallow exceptions
    """
    mock_engine = MagicMock()
    mock_engine.execute_backup.side_effect = Exception("backup failed")

    with patch(
        "app.services.backup_service.DBFactory.get_backup_engine",
        return_value=mock_engine,
    ):
        service = BackupService()

        try:
            service.trigger_backup("mongo")
            assert False, "Exception should have been raised"
        except Exception as exc:
            assert "backup failed" in str(exc)
