#app/services/rooms/amenity_service.py

from fastapi import HTTPException
from app.schemas.rooms import AmenityCreate, AmenityUpdate, AmenityResponse 
from app.crud.rooms.amenity_crud import AmenityCRUD 

class AmenityService:
    def __init__(self):
        self.crud = AmenityCRUD()

    async def get_all(self, page: int, page_size: int):
        return await self.crud.get_all(page=page, page_size=page_size)
    
    async def get_amenity_by_id(self, amenity_id: int):
        amenity = await self.crud.get_by_id(amenity_id)
        if not amenity:
            raise HTTPException(status_code=404, detail="Amenity not found")
        return AmenityResponse.from_orm(amenity)
    
    async def create_amenity(self, amenity_create: AmenityCreate):
        amenity = await self.crud.create(amenity_create)
        return AmenityResponse.from_orm(amenity)
    
    async def update(self, amenity_id: int, amenity_update: AmenityUpdate):
        amenity = await self.crud.get_by_id(amenity_id)
        if not amenity:
            raise HTTPException(status_code=404, detail="Amenity not found")
        updated_amenity = await self.crud.update(amenity_id, amenity_update)
        return AmenityResponse.from_orm(updated_amenity)
    
    async def delete_amenity(self, amenity_id: int):
        amenity = await self.crud.get_by_id(amenity_id)
        if not amenity:
            raise HTTPException(status_code=404, detail="Amenity not found")
        await self.crud.delete(amenity_id)
        return {"detail": "Amenity deleted successfully"}
    