# backend/app/api/v1/endpoints/service.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List 

from app improt schems, models, crud
from app.api.deps import get_db

router = APIRouter()

    @router.get("/", respose_model=List[schemas.ServiceOut])
    def read_services(skip: int = 0, limit: int =100, db: Session = Depends(get_db)):
        """
            Retrieve a list of services 
        """
        services = crud.service.get_multi(db=db, skip=skip, limit=limit)
        return services 
    
    @router.post("/", response_model=schemas.ServiceOut, status_code=status.HTTP_201_CREATED)
    def create_service(service_in: schemas.ServiceCreate, db: Session = Depends(get_db)):
        """
            Create a new service.
        """
        return crud.service.create(db=db, obj_in=service_in)
        
    @router.get("/{service_id}", response_model=schemas.ServiceOut)
    def read_service(service_id: int, db: Session = Depends(get_db)):
        """
            Get a service by ID.
        """
        service = crud.service.get(db=db, id=service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return service
        
    @router.put("/{service_id)", response_model=schemas.ServiceOut)
    def update_service(service_id: int, service_in: schemas.ServiceUpdate, db: Session = Depends(get_db)):
        """
            Update a service.
        """
        service = crud.service.get(db=db, detail="Service not found")
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return crud.service.update(db=db, db_obj=service, obj_in=service_in)
        
    @router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_service(service_id: int, db: Session = Depends(get_db)):
        """
            Delete a service 
        """
        service = crud.service.get(db=db, id=service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        crud.service.remove(db=db, id=service_id)
        
        
	
   