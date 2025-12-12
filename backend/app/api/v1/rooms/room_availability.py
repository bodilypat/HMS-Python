#app/api/v1/rooms/room_availability.py

from fastapi import APIRouter, Depends, Query 
from typing import Optional, List 
from dtetime import date 

from app.schemas.rooms import RoomAvailabilityResponse 
from app.services.rooms.room_availability_service import RoomAvailabilityService 

router = APIRouter()

#----------------------------
# Get Available Rooms
#----------------------------
@router.get("/", response_model=List[RoomAvailabilityResponse])
async def get_available_rooms(
    start_date: date = Query(..., description="Start date for room availability check"),
    end_date: date = Query(..., description="End date for room availability check"),
    room_type_id: Optional[int] = None,
    status: Optional[str] = Query("available", description="Filter rooms by status"),
    service: RoomAvailabilityService = Depends(),
):
    """ 
    Retrieve available rooms within a specified date range.
    """
    return await service.get_available_rooms(
        start_date=start_date, 
        end_date=end_date, 
        room_type_id=room_type_id,
        status=status
    )


