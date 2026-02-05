"""
File: tests/factories/test_db_factory.py
Responsibility: Unit tests for DBFactory resolution logic
"""

import pytest

from app.infrastructure.factory.db_factory import DBFactory
from app.infrastructure.backup.mongo_backup import MongoBackup
from app.infrastructure.backup.postgres_backup import PostgresBackup
from app.infrastructure.db.mongo.mongo_connection import MongoConnection
from app.infrastructure.db.postgres.postgres_connection import PostgresConnection


# -----------------------
# Backup Engine Factory
# -----------------------

def test_get_mongo_backup_engine():
    engine = DBFactory.get_backup_engine("mongo")
    assert isinstance(engine, MongoBackup)


def test_get_postgres_backup_engine():
    engine = DBFactory.get_backup_engine("postgres")
    assert isinstance(engine, PostgresBackup)


def test_get_backup_engine_invalid_db():
    with pytest.raises(ValueError):
        DBFactory.get_backup_engine("invalid_db")


# -----------------------
# Connection Checker Factory
# -----------------------

def test_get_mongo_connection_checker():
    checker = DBFactory.get_connection_checker("mongo")
    assert isinstance(checker, MongoConnection)


def test_get_postgres_connection_checker():
    checker = DBFactory.get_connection_checker("postgres")
    assert isinstance(checker, PostgresConnection)


def test_get_connection_checker_invalid_db():
    with pytest.raises(ValueError):
        DBFactory.get_connection_checker("invalid_db")


# -----------------------
# Supported DB Types
# -----------------------

def test_supported_db_types():
    supported = DBFactory.supported_db_types()
    assert "mongo" in supported
    assert "postgres" in supported
    assert len(supported) >= 2
