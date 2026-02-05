"""
File: tests/unit/test_backup_engines.py
Responsibility: Unit tests for MongoDB and PostgreSQL backup engines
"""

from pathlib import Path
from unittest.mock import patch
import pytest

from app.infrastructure.backup.mongo_backup import MongoBackup
from app.infrastructure.backup.postgres_backup import PostgresBackup
from app.core.exceptions import BackupOperationException


# -----------------------
# Mongo Backup Tests
# -----------------------

@patch("subprocess.run")
def test_mongo_backup_executes_mongodump(mock_run, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    backup = MongoBackup()
    backup_path = tmp_path / "backups" / "mongo" / "Backup_test"
    backup_path.mkdir(parents=True)

    backup._perform_backup(backup_path)

    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]

    assert "mongodump" in args
    assert "--out" in args
    assert str(backup_path) in args


@patch("subprocess.run", side_effect=Exception("mongodump failed"))
def test_mongo_backup_failure_raises_exception(mock_run, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    backup = MongoBackup()
    backup_path = tmp_path / "backups" / "mongo" / "Backup_test"
    backup_path.mkdir(parents=True)

    with pytest.raises(BackupOperationException):
        backup._perform_backup(backup_path)


# -----------------------
# Postgres Backup Tests
# -----------------------

@patch("subprocess.run")
@patch("os.environ", {})
def test_postgres_backup_executes_pg_dump(mock_run, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    backup = PostgresBackup()
    backup_path = tmp_path / "backups" / "postgres" / "Backup_test"
    backup_path.mkdir(parents=True)

    backup._perform_backup(backup_path)

    mock_run.assert_called_once()
    args = mock_run.call_args[0][0]

    assert "pg_dump" in args
    assert "-f" in args
    assert str(backup_path / "backup.sql") in args


@patch("subprocess.run", side_effect=Exception("pg_dump failed"))
def test_postgres_backup_failure_raises_exception(mock_run, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    backup = PostgresBackup()
    backup_path = tmp_path / "backups" / "postgres" / "Backup_test"
    backup_path.mkdir(parents=True)

    with pytest.raises(BackupOperationException):
        backup._perform_backup(backup_path)
