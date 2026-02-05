"""
File: tests/services/test_list_backup_service.py
Responsibility: Service-level tests for ListBackupService
"""

from pathlib import Path
from datetime import datetime

from app.services.list_backup_service import ListBackupService


def test_list_backups_empty_when_no_directory(tmp_path, monkeypatch):
    """
    If backups/<db_type> does not exist, return empty list
    """
    monkeypatch.chdir(tmp_path)

    service = ListBackupService()
    backups = service.list_backups("mongo")

    assert backups == []


def test_list_backups_returns_valid_backups(tmp_path, monkeypatch):
    """
    Verify valid backup folders are discovered and parsed correctly
    """
    monkeypatch.chdir(tmp_path)

    base = tmp_path / "backups" / "mongo"
    base.mkdir(parents=True)

    folder_name = "Backup_2026-02-04_14-40-54"
    folder = base / folder_name
    folder.mkdir()

    service = ListBackupService()
    backups = service.list_backups("mongo")

    assert len(backups) == 1
    backup = backups[0]

    assert backup.db_type == "mongo"
    assert backup.status == "AVAILABLE"
    assert backup.location == f"backups/mongo/{folder_name}"
    assert backup.timestamp == datetime(2026, 2, 4, 14, 40, 54)


def test_list_backups_ignores_invalid_folder_names(tmp_path, monkeypatch):
    """
    Invalid folder names should be skipped
    """
    monkeypatch.chdir(tmp_path)

    base = tmp_path / "backups" / "mongo"
    base.mkdir(parents=True)

    (base / "invalid_folder").mkdir()
    (base / "Backup_wrong_format").mkdir()

    service = ListBackupService()
    backups = service.list_backups("mongo")

    assert backups == []


def test_list_backups_sorted_newest_first(tmp_path, monkeypatch):
    """
    Backups should be sorted by timestamp descending (newest first)
    """
    monkeypatch.chdir(tmp_path)

    base = tmp_path / "backups" / "mongo"
    base.mkdir(parents=True)

    older = base / "Backup_2026-02-03_10-00-00"
    newer = base / "Backup_2026-02-04_12-00-00"

    older.mkdir()
    newer.mkdir()

    service = ListBackupService()
    backups = service.list_backups("mongo")

    assert len(backups) == 2
    assert backups[0].timestamp > backups[1].timestamp
