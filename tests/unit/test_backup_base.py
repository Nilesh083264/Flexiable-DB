"""
File: tests/unit/test_backup_base.py
Responsibility: Unit tests for BaseBackup template workflow
"""

from pathlib import Path
from datetime import datetime
from unittest.mock import MagicMock
import pytest

from app.infrastructure.backup.base_backup import BaseBackup
from app.domain.models.backup_metadata import BackupMetadata


class DummyBackup(BaseBackup):
    """
    Test double for BaseBackup to avoid real DB backup logic
    """
    db_type = "dummy"

    def _perform_backup(self, backup_path: Path) -> None:
        # Simulate successful backup without side effects
        (backup_path / "dummy.txt").touch()


def test_backup_folder_created(tmp_path, monkeypatch):
    """
    Verify backup folder is created with correct structure
    """
    monkeypatch.chdir(tmp_path)

    backup = DummyBackup()
    metadata = backup.execute_backup()

    backup_path = Path(metadata.location)

    assert backup_path.exists()
    assert backup_path.is_dir()
    assert "Backup_" in backup_path.name
    assert backup_path.parent.name == "dummy"


def test_backup_metadata_contents(tmp_path, monkeypatch):
    """
    Verify metadata fields are populated correctly
    """
    monkeypatch.chdir(tmp_path)

    backup = DummyBackup()
    metadata = backup.execute_backup()

    assert isinstance(metadata, BackupMetadata)
    assert metadata.db_type == "dummy"
    assert metadata.status == "SUCCESS"
    assert isinstance(metadata.timestamp, datetime)
    assert metadata.location.startswith("backups/dummy")


def test_perform_backup_is_called(tmp_path, monkeypatch):
    """
    Verify Template Method calls _perform_backup()
    """
    monkeypatch.chdir(tmp_path)

    backup = DummyBackup()
    backup._perform_backup = MagicMock()

    backup.execute_backup()

    backup._perform_backup.assert_called_once()


def test_backup_creates_expected_file(tmp_path, monkeypatch):
    """
    Verify backup operation creates expected output
    """
    monkeypatch.chdir(tmp_path)

    backup = DummyBackup()
    metadata = backup.execute_backup()

    backup_path = Path(metadata.location)
    dummy_file = backup_path / "dummy.txt"

    assert dummy_file.exists()
