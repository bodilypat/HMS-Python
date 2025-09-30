#app/api/v1/endpoints/doctor.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.doctor import DoctorCreate, DoctorRead, DoctorUpdate 
from app.db.session import get_db 
from app.services import doctor_service as DoctorService

router = APIRouter()

@router.get("/", response_model=DotorRead, summary="Get a list of Doctor")
def list_doctors(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return DoctorService(db).get_all_doctors(skip, limit)

@router.get("/{doctor_id}", response_model=DoctorRead, summary="Get a single doctor by id")
def read_doctor(
        doctor_id: int,
        db: Session = Depends(get_db)
    ):
    doctor = DoctorService(db).get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Dotor not found")
    return doctor 

@router.get("/{email}", response_model=DoctorRead, summary="Get doctor by email")
def read_email(
        email: str,
        db: Session = Depends(get_db)
    ):
    email = DoctorService(db).get_doctor_by_email(email)
    if not email:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return email

@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CREATED, summary="Create a new doctor")
def create_doctor(
        doctor_data: DoctorCreate,
        db: Session = Depends(get_db)
    ):
    return DoctorService(db).create_doctor(doctor_data)

@router.put("/{doctor_id}", response_model=DoctorRead, summary="Update an existing doctor")
def update_doctor(
        doctor_id: int,
        updated_doctor: DoctorUpdate,
        db: Session = Depends(get_db)
    ):
    updated = DoctorService(db).update_doctor(doctor_id, updated_doctor)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated 

@router.delete("/{doctor_id}", status_code=status.HTTP_204_CONTENT, summary="Deleted Doctor")
def delete_doctor(
        doctor_id: int,
        db: Session = Depends(get_db)
    ):
    success = DoctorService(db).delete_doctor(doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

