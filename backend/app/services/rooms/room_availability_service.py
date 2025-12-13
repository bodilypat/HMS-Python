#app/services/rooms/room_availability_service.py

from datetime import date 
from typing import Optional, List 
from fastapi import HTTPException 

from app.schemas.rooms import RoomAvailabilityResponse 
from app.crud.rooms.room_availability_crud import RoomAvailabilityCRUD 

class RoomAvailabilityService:
    def __init__(self):
        self.crud = RoomAvailabilityCRUD()

    async def get_available_rooms(
            self, 
            start_date: date, 
            end_date: date, 
            room_type_id: Optional[int],
            status: Optional[str]
    ) -> List[RoomAvailabilityResponse]:
        
        if start_date > end_date:
            raise HTTPException(status_code=400, detail="Start date cannot be after end date")
        
        rooms = await self.crud.get_available_rooms(
            start_date=start_date,
            end_date=end_date,
            room_type_id=room_type_id,
            status=status
        )
        return [RoomAvailabilityResponse.from_orm(room) for room in rooms]
    
    