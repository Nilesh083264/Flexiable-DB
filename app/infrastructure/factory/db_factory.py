"""
File: app/infrastructure/factory/db_factory.py
Responsibility: Resolve DB engine implementations
"""

from app.core.config import settings
from app.domain.interfaces.connection_interface import ConnectionInterface
from app.infrastructure.db.mongo.mongo_connection import MongoConnection
from app.infrastructure.db.postgres.postgres_connection import PostgresConnection

from app.infrastructure.backup.mongo_backup import MongoBackup
from app.infrastructure.backup.postgres_backup import PostgresBackup

class DBFactory:

    @staticmethod
    def get_connection_checker(db_type: str):
        if db_type == "mongo":
            return MongoConnection()
        if db_type == "postgres":
            return PostgresConnection()
        raise ValueError(f"Unsupported db_type: {db_type}")

    @staticmethod
    def get_backup_engine(db_type: str):
        if db_type == "mongo":
            return MongoBackup()
        if db_type == "postgres":
            return PostgresBackup()
        raise ValueError(f"Unsupported db_type: {db_type}")

    @staticmethod
    def get_all_connection_checkers():
        return {
            "mongo": MongoConnection(),
            "postgres": PostgresConnection(),
        }

    @staticmethod
    def supported_db_types():
        return ["mongo", "postgres"]

