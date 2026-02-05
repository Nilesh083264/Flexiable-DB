"""
File: tests/services/test_health_service.py
Responsibility: Service-level tests for HealthService
"""

from unittest.mock import MagicMock, patch

from app.services.health_service import HealthService


def test_health_service_all_dbs_up():
    """
    Verify all DBs are reported UP when connections succeed
    """
    mongo_checker = MagicMock()
    mongo_checker.check_connection.return_value = None

    postgres_checker = MagicMock()
    postgres_checker.check_connection.return_value = None

    with patch(
        "app.services.health_service.DBFactory.get_all_connection_checkers",
        return_value={
            "mongo": mongo_checker,
            "postgres": postgres_checker,
        },
    ):
        service = HealthService()
        result = service.check_all_dbs()

        assert result == {
            "mongo": "UP",
            "postgres": "UP",
        }


def test_health_service_one_db_down():
    """
    Verify one DB DOWN does not affect other DB health results
    """
    mongo_checker = MagicMock()
    mongo_checker.check_connection.side_effect = Exception("mongo down")

    postgres_checker = MagicMock()
    postgres_checker.check_connection.return_value = None

    with patch(
        "app.services.health_service.DBFactory.get_all_connection_checkers",
        return_value={
            "mongo": mongo_checker,
            "postgres": postgres_checker,
        },
    ):
        service = HealthService()
        result = service.check_all_dbs()

        assert result == {
            "mongo": "DOWN",
            "postgres": "UP",
        }


def test_health_service_all_dbs_down():
    """
    Verify all DBs DOWN scenario
    """
    mongo_checker = MagicMock()
    mongo_checker.check_connection.side_effect = Exception("mongo down")

    postgres_checker = MagicMock()
    postgres_checker.check_connection.side_effect = Exception("postgres down")

    with patch(
        "app.services.health_service.DBFactory.get_all_connection_checkers",
        return_value={
            "mongo": mongo_checker,
            "postgres": postgres_checker,
        },
    ):
        service = HealthService()
        result = service.check_all_dbs()

        assert result == {
            "mongo": "DOWN",
            "postgres": "DOWN",
        }
