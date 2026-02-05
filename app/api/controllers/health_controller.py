"""
File: app/api/controllers/health_controller.py
Responsibility: Exposes health and database connectivity status APIs
"""

from fastapi import APIRouter
from app.services.health_service import HealthService
from app.api.schemas import HealthResponse
from typing import Dict

router = APIRouter()
health_service = HealthService()


@router.get("/",response_model=HealthResponse,summary="Application health check")
def health() -> HealthResponse:
    """
    Basic application health check.
    """
    return HealthResponse(status="UP")


@router.get("/db",summary="Database health check for all supported databases")
def db_health() -> Dict[str, str]:
    """
    Checks connectivity status for all supported databases
    (MongoDB, PostgreSQL, etc.).

    Returns:
        {
            "mongo": "UP",
            "postgres": "DOWN"
        }
    """
    return health_service.check_all_dbs()
