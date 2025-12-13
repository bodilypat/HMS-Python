#app/services/hotel_services/additional_service.py

from fastapi import HTTPException 
from app.schemas.servces import ServiceCreate, ServiceUpdate, ServiceResponse 
from app.crud.services.services_crud import ServiceCRUD 

class AdditionalService:
    def __init__(self):
        self.service_crud = ServiceCRUD()

#-------------------------------
# GET ALL SERVICES
#-------------------------------
    async def get_all(self, page: int, page_size: int, active: bool = True):
        services = await self.service_crud.get_all(page, page_size, active)
        return [ServiceResponse.from_orm(service) for service in services]
    
#------------------------------
# GET SERVICE BY ID
#------------------------------
    async def get_by_id(self, service_id: int):
        service = await self.service_crud.get_by_id(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return ServiceResponse.from_orm(service)
    
#------------------------------
# CREATE SERVICE
#------------------------------
    async def create(self, service_create: ServiceCreate):
        service = await self.service_crud.create(service_create)
        return ServiceResponse.from_orm(service)
    
#------------------------------
# UPDATE SERVICE
#------------------------------
    async def update(self, service_id: int, service_update: ServiceUpdate):
        service = await self.service_crud.get_by_id(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        service = await self.service_crud.update(service, service_update)
        return ServiceResponse.from_orm(service)
    
#------------------------------
# DEACTIVATE SERVICE
#------------------------------
    async def deactivate(self, service_id: int):
        service = await self.service_crud.get_by_id(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        service = await self.service_crud.deactivate(service)
        return ServiceResponse.from_orm(service)
    
#------------------------------
# DELETE SERVICE
#------------------------------
    async def delete(self, service_id: int):
        service = await self.service_crud.get_by_id(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        await self.service_crud.delete(service)
        return {"detail": "Service deleted successfully"}
    
    