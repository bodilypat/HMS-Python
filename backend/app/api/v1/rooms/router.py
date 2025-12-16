#app/api/v1/rooms/router.py

from fastapi import APIRouter

# Import sub-routers 
from .rooms import router as rooms_router
from .room_types import router as room_types_router
from .amenities import router as amenities_router
from .availability import router as availability_router 

#-------------------------------------------
# Main router for rooms with a common prefix
#-------------------------------------------
router = APIRouter(prefix="/rooms", tags=["Rooms"])

#--------------------------------------------------------------
# Sub-router: Rooms CRUD operations (add, update, delete, list)
#--------------------------------------------------------------
router.include_router(
    rooms_router, 
    prefix="/manage", 
    tags=["Rooms Management"])

#--------------------------------------------------------------
# Sub-router: Room types (Single, double, suite, etc.)
router.include_router(
    room_types_router, 
    prefix="/types", 
    tags=["Room Types"])

#--------------------------------------------------------------
# Sub-router: Room Amenities (WiFi, TV, AC, etc.)
#--------------------------------------------------------------
router.include_router(
    amenities_router, 
    prefix="/amenities", 
    tags=["Room Amenities"])

#--------------------------------------------------------------
# Sub-router: Room Availability & Booking check (check availability, bookings)
#--------------------------------------------------------------
router.include_router(
    availability_router, 
    prefix="/availability", 
    tags=["Room Availability"])

