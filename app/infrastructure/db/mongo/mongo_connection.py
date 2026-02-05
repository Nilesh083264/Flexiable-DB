"""
File: app/infrastructure/db/mongo/mongo_connection.py
Responsibility: MongoDB connection implementation
"""

from pymongo import MongoClient
from app.core.config import settings
from app.core.logger import logger
from app.core.exceptions import DatabaseConnectionException
from app.domain.interfaces.connection_interface import ConnectionInterface


class MongoConnection(ConnectionInterface):

    def check_connection(self) -> bool:
        try:
            client = MongoClient(
                settings.MONGO_URI,
                serverSelectionTimeoutMS=3000
            )
            client.admin.command("ping")
            logger.info("MongoDB connection successful | DB_TYPE=mongo")
            return True
        except Exception as exc:
            logger.error(f"MongoDB connection failed | {exc}")
            raise DatabaseConnectionException(
                "Unable to connect to MongoDB"
            )
