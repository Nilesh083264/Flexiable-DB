"""
File: app/infrastructure/db/postgres/postgres_connection.py
Responsibility: PostgreSQL connection implementation
"""

import psycopg2
from app.core.config import settings
from app.core.logger import logger
from app.core.exceptions import DatabaseConnectionException
from app.domain.interfaces.connection_interface import ConnectionInterface


class PostgresConnection(ConnectionInterface):

    def check_connection(self) -> bool:
        try:
            conn = psycopg2.connect(
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                dbname=settings.POSTGRES_DB,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                connect_timeout=3
            )
            conn.close()
            logger.info("PostgreSQL connection successful | DB_TYPE=postgres")
            return True
        except Exception as exc:
            logger.error(f"PostgreSQL connection failed | {exc}")
            raise DatabaseConnectionException(
                "Unable to connect to PostgreSQL"
            )
