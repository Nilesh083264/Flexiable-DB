"""
File: app/api/routes.py
Responsibility: Central API router registry
"""

from fastapi import APIRouter
from app.api.controllers.health_controller import router as health_router
from app.api.controllers.backup_controller import router as backup_router


router = APIRouter()
router.include_router(health_router, prefix="/health", tags=["Health"])
router.include_router(backup_router,prefix="/backup",tags=["Backup"])
