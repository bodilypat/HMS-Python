#app/api/v1/endpoints/appointment_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.services import appointment_service as AppointmentService 
from typing import List
from db.session import get_db 

router = APIRouter()

@router.get("/", response_model=AppointmentRead, summary="Get a list of Appointments")
def list_appointments(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return AppointmentService(db).get_all_appointment(skip, limit)

@router.get("/{appointment_id}", Response_model=AppointmentRead, summary="Get a single appointemnt")
def read_appointment(
        appointment_id: int,
        db: Session = Depends(get_db)
    ):
    appointment = AppointmentService(db).get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED, summary="Create new appointment")
def create_appointment(
        appointment_info: AppointmentCreate,
        db: Session = Depends(get_db)
    ):
    return AppointmentService(db).create_appointment(appointment_info)

@router.put("/{appointment_id}", response_model=AppointmentRead, summary="Update an existing appointment")
def update_appointment(
        appointment_id: int, 
        updated_appointment: AppointmentUpdate,
        db: Session = Depends(get_db)
    ):
    updated = AppointmentService(db).update_appointment(appointment_id, updated_appointment)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment of found")
    return updated 

@router.delete("/{appointment_id}", status_code=status.HTTP_NO_CONTENT, summary="Delete appointment")
def delete_appointment(
        appointment_id: int,
        db: Session = Depends(get_db)
    ):
    success = AppointmentService(db).delete_appointment(appointment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)