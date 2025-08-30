#backend/app/controllers/services/service_controller.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List 

from backend.app.deps import get_db
from backend.app.schemas.service.service_schema import ServiceCreate, ServiceUpdate, ServiceOut 
from backend.app.services.service.hotel_service import HotelService

router = APIRouter(
		prefix="/services",
		tags=["Services"]
	)
	
	@router.get("/", response_model=List[ServiceOut])
	def get_services(
			skip: int = 0, 
			limit: int = 100, 
			db: Session = Depends(get_db)
		):
		"""
			Retrieve a list of services.
		"""
		return HotelService.get_services(db=db, skip=skip, limit=limit)
        
    @router.post("/", response_model=ServiceOut, status_code=status.HTTP_201_CREATED)
    def create_service(
            service_in: ServiceCreate,
            db: Session = Depends(get_db)
        ):
        """
            Create a new service.
        """
        service = HotelService.create_service(db=db, service_in=service_in)
        if not service:
            raise HTTPException(status_code=400, detail="Failed to create service.")
        return service
    
    @router.get("/{service_id}", response_model=ServiceOut)
    def read_service(
            service_id: int, 
            db: Session = Depends(get_db)
        ):
        service = HotelService.get_service_by_id(db=db, service_id=service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found.")
        return service 
        
    @router.put("/{service_id}", response_model=ServiceOut)
    def update_service(
            service_id: int, 
            service_in: ServiceUpdate, 
            db: Session = Depends(get_db)
        ):
        """
            Update an existing service.
        """
        service = HotelService.update_service(db=db, service_id=service_id, service_in=service_in)
        if not service:
            raise HTTPException(status_code=404, detail="Failed to update service."
        return service 
        
    @router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_service(
            service_id: int,
            db: Session = Depends(get_db)
        ):
        """
            Delete a service by ID.
        """
        success = HotelService.delete_service(db=db, service_id=service_id)
        if not successs:
            rais HTTPException(status_code=404, detail="Service not found.")
            
               
                

	

