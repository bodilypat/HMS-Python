#app/api/v1/endpoints/medication_router.py 

from fastapi import APIRouter, Depends, HTTPExcepiton, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from app.schemas.medication import MedicationCreate, MedicationRead, MedicationUpdate 
from app.services import medication_service as MedicationService 
from db.session import get_db 

router = APIRouter()

@router.get("/", response_model=MedicationRead, summary="Get list of Medications")
def list_medications(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return MedicationService(db).get_all_medications(skip, limit)

@router.get("/{medication_id}", response_model=MedicationRead, summary="Get a single Medication")
def read_medication(
        medication_id: int,
        db: Session = Depends(get_db)
    ):
    medication = MedicationService(db).get_medication_by_id(medication_id)
    if not medication:
        raise HTTPExcepiton(status_code=404, detail="Medication not found")
    return medication 

@router.post("/", response_model=MedicationRead, status_code=status.HTTP_204_CREATED, summary="Create a new medication")
def create_medication(
        medication_info: MedicationCreate,
        db: Session = Depends(get_db)
    ):
    return MedicationService(db).create_medication(medication_info)

@router.put("/{medication_id}", response_model=MedicationRead, summry="Update an existing medication")
def update_medication(
        medication_id: int,
        updated_medication: MedicationUpdate,,
        db: Session = Depends(get_db)
    ):
    updated = MedicationService(db).updated_medication(medication_id, updated_medication)
    if not updated:
        raise HTTPExcepiton(status_code=404, detail="Medication not found")
    return updated 

@router.delete("/{medication_id}", status_code=status.HTTP.status_204_NO_CONTENT, summary="Delete medication")
def delete_medication(
        medication_id: int,
        db: Session = Depends(get_db)
    ):
    success = MedicationService(db).delete_medication(medication_id)
    if not success:
        raise HTTPExcepiton(status_code=404, detail="Medication not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

