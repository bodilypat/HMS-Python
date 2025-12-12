#app/api/v1/rooms/router.py

from fastapi import APIRouter

from .rooms import router as rooms_router
from .room_types import router as room_types_router 
from .amenities import router as amenities_router
from .room_availability import router as room_availability_router 

# Main router for rooms module
router = APIRouter(prefix="/rooms", tags=["Rooms"])

router.include_router(rooms_router, prefix="/rooms", tags=["Rooms Management"])
router.include_router(room_types_router, prefix="/room-types", tags=["Room Types"])
router.include_router(amenities_router, prefix="/amenities", tags=["Amenities"])
router.include_router(room_availability_router, prefix="/availability", tags=["Room Availability"])

