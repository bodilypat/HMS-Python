#backend/app/controllers/booking/__init__.py

from .booking_controller import router as booking_router 
from .reservation_controller import router as reservation_router 

__all__ = [
	"booking_router",
	"reservation_router",
	]
	