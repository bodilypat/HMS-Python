#app/api/v1/endpoints/patient_router.py

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.patient import PatientCreate, PatientUpdate, PatientRead 
from app.services import patient_service as PatientService
from app.db.session import get_db 

router = APIRouter()

@router.get("/", respose_model=PatientRead, summary="Get a list of Patients")
def list_patients(
        skip: int = Query(0, ge=0),
        limit: int =Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return PatientService(db).get_all_patients(skip, limit)

@router.get("/{patient_id}", response_model=PatientRead, summary="Get a single patient by ID")
def read_patient(
        patient_id: int,
        db: Session = Depends(get_db)
    ):
    patient = PatientService(db).get_patient_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient 

@router.get("/{patient_email}", response_model=PatientRead, summary="Get Patient by email")
def read_email(
        patient_email: str,
        db: Session = Depends(get_db)
    ):
    email = PatientService(db).get_patient_by_email(patient_email)
    if not email:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Patient

@router.post("/", response_model=PatientRead, status_code=status.HTTP_201_CREATED, summary="Create a new patient")
def create_patient(
        patient_data: PatientCreate,
        db: Session = Depends(get_db)
    ):
    return PatientService(db).create_patient(patient_data)

@router.put("/{patient_id}", response_model=PatientRead, summary="Update an existing patient")
def update_patient(
        patient_id: int,
        updated_patient: PatientUpdate,
        db: Session = Depends(get_db)
    ):
    updated = PatientService(db).update_patient(patient_id, updated_patient)
    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated 

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Patient")
def delete_patient(
        patient_id: int,
        db: Session = Depends(get_db)
    ):
    success = PatientService(db).delete_patient(patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
