#app/services/rooms/room_type_service.py

from fastapi import HTTPException 
from app.schemas.rooms import RoomTypeCreate, RoomTypeUpdate, RoomTypeResponse 
from app.crud.rooms.room_type_crud import RoomTypeCRUD 


class RoomTypeService:
    def __init__(self):
        self.crud = RoomTypeCRUD()

    async def get_all(self, page: int, page_size: int):
        return await self.crud.get_all(page=page, page_size=page_size)
    
    async def get_by_id(self, room_type_id: int):
        room_type = await self.crud.get_by_id(room_type_id)
        if not room_type:
            raise HTTPException(status_code=404, detail="Room type not found")
        return RoomTypeResponse.from_orm(room_type)
    
    async def create(self, room_type_create: RoomTypeCreate):
        room_type = await self.crud.create(room_type_create)
        return RoomTypeResponse.from_orm(room_type)
    
    async def update(self, room_type_id: int, room_type_update: RoomTypeUpdate):
        room_type = await self.crud.get_by_id(room_type_id)
        if not room_type:
            raise HTTPException(status_code=404, detail="Room type not found")
        updated_room_type = await self.crud.update(room_type_id, room_type_update)
        return RoomTypeResponse.from_orm(updated_room_type)
    
    async def delete(self, room_type_id: int):
        room_type = await self.crud.get_by_id(room_type_id)
        if not room_type:
            raise HTTPException(status_code=404, detail="Room type not found")
        await self.crud.delete(room_type_id)
        return {"detail": "Room type deleted successfully"}
    
    