#backend/app/api/amenities/__init__.py

from .feedback_router import router as feedback_router

__all__ = [
	"feedback_router",
	]