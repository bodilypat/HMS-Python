#app/api/v1/services/service_request.py

from typing import List 
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.service_request import ServiceRequestCreate, ServiceRequestUpdate, ServiceRequestOut
from app.services.service_request import service_request as ServiceRequest 

router = APIRouter(prefix="/service-requests", tags=["Service Requests"])

#----------------------- Create Service Request -----------------------#
@router.post("/", response_model=ServiceRequestOut)
def create_service_request(
    service_request_in: ServiceRequestCreate,
    db: Session = Depends(get_db)
):
    service_request = ServiceRequest.create_service_request(db, service_request_in)
    return service_request

#----------------------- Get Service Request by ID -----------------------#
@router.get("/{service_request_id}", response_model=ServiceRequestOut)
def get_service_request(
    service_request_id: int,
    db: Session = Depends(get_db)
):
    service_request = ServiceRequest.get_service_request_by_id(db, service_request_id)
    if not service_request:
        raise HTTPException(status_code=404, detail="Service Request not found")
    return service_request
#----------------------- Update Service Request -----------------------#
@router.put("/{service_request_id}", response_model=ServiceRequestOut)  
def update_service_request(  
    service_request_id: int,  
    service_request_in: ServiceRequestUpdate,  
    db: Session = Depends(get_db)  
):  
    service_request = ServiceRequest.update_service_request(db, service_request_id, service_request_in)  
    if not service_request:  
        raise HTTPException(status_code=404, detail="Service Request not found")  
    return service_request
#----------------------- List Service Requests -----------------------#
@router.get("/", response_model=List[ServiceRequestOut])    
def list_service_requests(  
    skip: int = 0,  
    limit: int = 10,  
    db: Session = Depends(get_db)  
):  
    service_requests = ServiceRequest.list_service_requests(db, skip=skip, limit=limit)  
    return service_requests

#----------------------- Delete Service Request -----------------------#
@router.delete("/{service_request_id}", response_model=dict)
def delete_service_request(  
    service_request_id: int,  
    db: Session = Depends(get_db)  
):  
    success = ServiceRequest.delete_service_request(db, service_request_id)  
    if not success:  
        raise HTTPException(status_code=404, detail="Service Request not found")  
    return {"detail": "Service Request deleted successfully"}

#==============Internal helper ===================
def get_service_request_internal(
    service_request_id: int,
    db: Session
) -> ServiceRequestOut:
    service_request = ServiceRequest.get_service_request_by_id(db, service_request_id)
    if not service_request:
        raise HTTPException(status_code=404, detail="Service Request not found")
    return service_request

