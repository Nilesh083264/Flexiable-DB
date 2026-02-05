"""
File: app/services/health_service.py
Responsibility: Provides aggregated health status for all supported databases
"""

from typing import Dict
from app.infrastructure.factory.db_factory import DBFactory
from app.core.logger import logger


class HealthService:
    """
    Service responsible for checking availability of all supported DB engines.
    """

    def check_all_dbs(self) -> Dict[str, str]:
        """
        Checks connectivity for all supported databases.

        Returns:
            Dict[str, str]: Mapping of db_type to status (UP/DOWN)
        """
        results: Dict[str, str] = {}

        checkers = DBFactory.get_all_connection_checkers()

        for db_type, checker in checkers.items():
            try:
                checker.check_connection()
                results[db_type] = "UP"
                logger.info(f"Health check passed | db_type={db_type}")
            except Exception as exc:
                results[db_type] = "DOWN"
                logger.error(
                    f"Health check failed | db_type={db_type} | reason={exc}"
                )

        return results
