#app/api/v1/services.py

from fastapi import APIRouter, Depends, Query 
from typing import Optional, List 

from app.schemas.services import (
    ServiceCreate,
    ServiceUpdate,
    ServiceOut
)
from app.services.service import Service 

router = APIRouter()

#---------------------------------------------------
# Get All Hotel Services (with filters & pagination)
#---------------------------------------------------
@router.get("/", response_model=List[ServiceOut], tags=["Services"])
async def get_all_services(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: Optional[str] = None,
    category: Optional[str] = None,
    active: Optional[bool] = None,
    service: Service = Depends()
):
    return await service.get_all_services(
        page=page, 
        page_size=page_size, 
        name=name, 
        category=category, 
        active=active
    )

#--------------------------------------
# Get Single Service by ID
#--------------------------------------
@router.get("/{service_id}", response_model=ServiceOut, tags=["Services"])
async def get_service_by_id(
    service_id: int,
    service: Service = Depends()
):
    """
    Get a single service by its ID
    """
    return await service.get_service_by_id(service_id=service_id)

#-------------------------------------
# Create New Service
#-------------------------------------
@router.post("/", response_model=ServiceOut, tags=["Services"])
async def create_service(
    service_in: ServiceCreate,
    service: Service = Depends()
):
    """ 
    Create a new service
    """
    return await service.create_service(service_in=service_in)

#-------------------------------------
# Update Service
#-------------------------------------
@router.put("/{service_id}", response_model=ServiceOut, tags=["Services"])
async def update_service(
    service_id: int,
    service_in: ServiceUpdate,
    service: Service = Depends()
):
    """
    Update an existing service by its ID
    """
    return await service.update_service(service_id=service_id, service_in=service_in)

#--------------------------------------
# Delete Service
#--------------------------------------
@router.delete("/{service_id}", response_model=ServiceOut, tags=["Services"])
async def delete_service(
    service_id: int,
    service: Service = Depends()
):
    """ 
    Delete an existing service by its ID
    """
    await service.delete_service(service_id=service_id)
    return {"message": "Service deleted successfully"}


