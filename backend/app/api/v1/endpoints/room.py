#backend/app/api/v1/endpoints/room.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from backend.app.models.RoomModel import RoomModel
from backend.app.schemas.room import RoomUpdate, RoomOut, Roomstatus

router = APIRouter(
		prefix="/rooms/",
		tags=["Rooms"]
	)
	
	@router.post("/", response_model=RoomOut, status_code=status.HTTP_201_CREATED)
		def create_room(room: RoomCreate):
		room_id = RoomModel.create_room(**room.dict())
		if not room_id:
			raise HTTPException(status_code=500, detail="failed to create room.")
			
		room_data = RoomModel.get_room_by_id(room_id)
		if not room_data:
			raise HTTPException(status_code=404, detail="Room not found after creation.")
		
		return room_data
	
    @router.get("/", response_model=List[RoomOut])
    def get_all_rooms():
        rooms = RoomModel.get_all_rooms()
        return rooms
        
    @router.get("/{room_id}", response_model=RoomOut)
    def get_room_by_id(room_id: int):
        room = RoomModel.get_room_by_id(room_id)
        if not room:
            raise HTTPException(status_code=404, detail="Room not found.")
        return room
        
    @router.path("/{room_id}", response_model=RoomOut)
    def update_room(room_id: int, update_data: RoomUpdate):
        existing_room = RoomModel.get_room_by_id(room_id)
        if not existing_room:
            raise HTTPException(status_code=404, detail="Room not found.")
            
        updated_fields = update_data.dict(exclude_unset=True)
        
        if "room_status" in updated_fields:
            # updating status 
            success = RoomModel.update_room_status(room_id, updated_fields["room_status"])
            if not success:
                # extend RoomModel
                raise HTTPException(status_code=501, detail="Only status update is currently supported.")
            
            updated_room = RoomModel.get_room_by_id(room_id)
            return updated_room
            
    @router.delete("/{room_id}", status_code=status.HTTP_204_CENTENT)
    def delete_room(room_id: int):
        existing_room = roomModel.get_room_by_id(room_id)
        if not existing_room:
            raise HTTPException(status_code=404, detail="Room not found.")
            
        success = RoomModel.delete_room(room_id)
        if not sucess:
            raise HTTPException(status_code=400, detail="Failed to delete room.")
            
        return
            