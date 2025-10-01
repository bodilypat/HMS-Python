#backend/app/controllers/core/__init__.py

from .user_controller import router as user_controller
from .guest_controller import router as guest_controller
from .staff_controller import router as staff_router

__all__ = [
		"user_router",
		"guest_router",
		"staff_router",
	]