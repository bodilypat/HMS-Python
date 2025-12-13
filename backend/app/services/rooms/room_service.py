#app/services/rooms/room_service.py

from app.schemas.rooms import RoomCreate, RoomUpdate, RoomResponse 
from app.crud.rooms.room_crud import  RoomCRUD 
from fastapi import HTTPException, status 

class RoomService:
    def __init__(self):
        self.crud = RoomCRUD()

    async def get_all(self, page: int, page_size: int, status: str = None):
        return await self.crud.get_all(page=page, page_size=page_size, status=status)
    
    async def get_by_id(self, room_id: int):
        room = await self.crud.get_by_id(room_id)
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
        return RoomResponse.from_orm(room)
    
    async def create(self, room_create: RoomCreate):
        room = await self.crud.create(room_create)
        return RoomResponse.from_orm(room)
    
    async def update(self, room_id: int, room_update: RoomUpdate):
        room = await self.crud.get_by_id(room_id)
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
        updated_room = await self.crud.update(room_id, room_update)
        return RoomResponse.from_orm(updated_room)
    
    async def delete(self, room_id: int):
        room = await self.crud.get_by_id(room_id)
        if not room:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
        await self.crud.delete(room_id)

        return {"detail": "Room deleted successfully"}
    
    