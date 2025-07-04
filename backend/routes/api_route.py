# backend/routers/api_router.py

from fastapi import APIRouter
from app.controllers import guest_controller

router = APIRouter()
router.include_router(guest_controller.router)
