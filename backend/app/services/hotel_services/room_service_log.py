#app/services/hotel_services/room_service_log.py

from fastapi import HTTPException 
from app.schemas.services import RoomServiceCreate, RoomServiceResponse 
from app.crud.services.room_services_crud import RoomServiceCRUD 

class RoomServiceLogService:
    def __init__(self):
        self.room_service_crud = RoomServiceCRUD()

#---------------------------------
# GET ALL ROOM SERVICE LOGS 
#---------------------------------
    async def get_all(self, page: int, page_size: int, room_id: int = None):
        room_services = await self.room_service_crud.get_all(page, page_size, room_id)
        return [RoomServiceResponse.from_orm(service) for service in room_services]
    
#---------------------------------
# GET ROOM SERVICE LOG BY ID
#---------------------------------
    async def get_by_id(self, service_id: int):
        service = await self.room_service_crud.get_by_id(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Room service log not found")
        return RoomServiceResponse.from_orm(service)
    
#---------------------------------
# CREATE ROOM SERVICE LOG
#---------------------------------
    async def create(self, room_service_create: RoomServiceCreate):
        service = await self.room_service_crud.create(room_service_create)
        return RoomServiceResponse.from_orm(service)
    
#---------------------------------
# UPDATE ROOM SERVICE LOG
#---------------------------------
    async def update(self, service_id: int, room_service_update: RoomServiceCreate):
        service = await self.room_service_crud.update(service_id, room_service_update)
        if not service:
            raise HTTPException(status_code=404, detail="Room service log not found")
        return RoomServiceResponse.from_orm(service)
    
#---------------------------------
# DELETE ROOM SERVICE LOG
#---------------------------------
    async def delete(self, service_id: int):
        service = await self.room_service_crud.delete(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Room service log not found")
        return RoomServiceResponse.from_orm(service)
    
    