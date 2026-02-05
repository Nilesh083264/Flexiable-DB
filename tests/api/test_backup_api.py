"""
File: tests/api/test_backup_api.py
Responsibility: API-level tests for Backup endpoints
"""

from datetime import datetime
from unittest.mock import patch

from app.domain.models.backup_metadata import BackupMetadata
from app.core.exceptions import BackupOperationException


# -----------------------
# Trigger Backup API
# -----------------------

def test_trigger_backup_api_success(client):
    """
    Verify POST /api/backup/start returns backup metadata
    """
    mock_metadata = BackupMetadata(
        backup_id="test123",
        db_type="mongo",
        timestamp=datetime(2026, 2, 4, 10, 0, 0),
        status="SUCCESS",
        location="backups/mongo/Backup_test",
    )

    with patch(
        "app.api.controllers.backup_controller.backup_service.trigger_backup",
        return_value=mock_metadata,
    ):
        response = client.post(
            "/api/backup/start",
            params={"db_type": "mongo"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "backup_id": "test123",
            "db_type": "mongo",
            "timestamp": "2026-02-04T10:00:00",
            "status": "SUCCESS",
            "location": "backups/mongo/Backup_test",
        }


def test_trigger_backup_api_failure(client):
    """
    Verify backup API converts application exception into HTTP 500
    """
    with patch(
        "app.api.controllers.backup_controller.backup_service.trigger_backup",
        side_effect=BackupOperationException("backup failed"),
    ):
        response = client.post(
            "/api/backup/start",
            params={"db_type": "mongo"},
        )

        assert response.status_code == 500
        assert response.json()["error_code"] == "BACKUP_ERROR"


# -----------------------
# List Backups API
# -----------------------

def test_list_backups_api_success(client):
    """
    Verify GET /api/backup/list returns list of backups
    """
    mock_backups = [
        BackupMetadata(
            backup_id="Backup_2026-02-04_10-00-00",
            db_type="mongo",
            timestamp=datetime(2026, 2, 4, 10, 0, 0),
            status="AVAILABLE",
            location="backups/mongo/Backup_2026-02-04_10-00-00",
        )
    ]

    with patch(
        "app.api.controllers.backup_controller.list_service.list_backups",
        return_value=mock_backups,
    ):
        response = client.get(
            "/api/backup/list",
            params={"db_type": "mongo"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "backups": [
                {
                    "backup_id": "Backup_2026-02-04_10-00-00",
                    "db_type": "mongo",
                    "timestamp": "2026-02-04T10:00:00",
                    "status": "AVAILABLE",
                    "location": "backups/mongo/Backup_2026-02-04_10-00-00",
                }
            ]
        }


def test_list_backups_api_empty(client):
    """
    Verify empty backups list is handled correctly
    """
    with patch(
        "app.api.controllers.backup_controller.list_service.list_backups",
        return_value=[],
    ):
        response = client.get(
            "/api/backup/list",
            params={"db_type": "mongo"},
        )

        assert response.status_code == 200
        assert response.json() == {"backups": []}
