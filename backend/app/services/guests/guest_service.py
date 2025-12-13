#app/services/guests/guest_service.py

from fastapi import HTTPException 
from app.schemas.guests import GuestCreate, GuestUpdate, GuestResponse 
from app.crud.guests.guest_crud import GuestCRUD 

class GuestService:
    def __init__(self):
        self.crud = GuestCRUD()

#-----------------------------
# GET ALL GUESTS
#-----------------------------
    async def get_all(self, page: int, page_size: int, search: str = None) -> list[GuestResponse]:
        guests = await self.crud.get_all_guests(page, page_size, search)
        return [GuestResponse.from_orm(guest) for guest in guests]
    
#-----------------------------
# GET GUEST BY ID
#-----------------------------
    async def get_by_id(self, guest_id: int) -> GuestResponse:
        guest = await self.crud.get_guest_by_id(guest_id)
        if not guest:
            raise HTTPException(status_code=404, detail="Guest not found")
        return GuestResponse.from_orm(guest)
    
#------------------------------
# CREATE GUEST
#------------------------------
    async def create(self, guest_create: GuestCreate) -> GuestResponse:
        guest = await self.crud.create_guest(guest_create)
        return GuestResponse.from_orm(guest)
    
#------------------------------
# UPDATE GUEST
#------------------------------
    async def update(self, guest_id: int, guest_update: GuestUpdate) -> GuestResponse:
        guest = await self.crud.update_guest(guest_id, guest_update)
        if not guest:
            raise HTTPException(status_code=404, detail="Guest not found")
        return GuestResponse.from_orm(guest)
    
#------------------------------
# DELETE GUEST
#------------------------------
    async def delete(self, guest_id: int) -> None:
        guest = await self.crud.get_guest_by_id(guest_id)
        if not guest:
            raise HTTPException(status_code=404, detail="Guest not found")
        await self.crud.delete_guest(guest_id)
        return None
    
    





