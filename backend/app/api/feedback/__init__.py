#backend/app/api/feedback/__init__.py

from .feedback_router import router as feedback_router

__all__ = [
	"feedback_router",
	]
