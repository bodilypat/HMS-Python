#backend/app/api/amenities/__init__.py

from .hotel_amenity_router import router as hotel_amenity_router
from .room_amenity_router import router as room_amenity_router 

__all__ = [
	"hotel_amenity_router",
	"room_amenity_router",
	]
