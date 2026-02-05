"""
File: tests/api/test_health_api.py
Responsibility: API-level tests for Health endpoints
"""

from unittest.mock import patch


def test_health_api_all_dbs_up(client):
    """
    Verify health API returns UP for all DBs
    """
    with patch(
        "app.api.controllers.health_controller.health_service.check_all_dbs",
        return_value={
            "mongo": "UP",
            "postgres": "UP",
        },
    ):
        response = client.get("/api/health/db")

        assert response.status_code == 200
        assert response.json() == {
            "mongo": "UP",
            "postgres": "UP",
        }


def test_health_api_partial_db_down(client):
    """
    Verify health API handles partial DB failure
    """
    with patch(
        "app.api.controllers.health_controller.health_service.check_all_dbs",
        return_value={
            "mongo": "DOWN",
            "postgres": "UP",
        },
    ):
        response = client.get("/api/health/db")

        assert response.status_code == 200
        assert response.json() == {
            "mongo": "DOWN",
            "postgres": "UP",
        }


def test_health_api_all_dbs_down(client):
    """
    Verify health API handles all DBs DOWN
    """
    with patch(
        "app.api.controllers.health_controller.health_service.check_all_dbs",
        return_value={
            "mongo": "DOWN",
            "postgres": "DOWN",
        },
    ):
        response = client.get("/api/health/db")

        assert response.status_code == 200
        assert response.json() == {
            "mongo": "DOWN",
            "postgres": "DOWN",
        }
