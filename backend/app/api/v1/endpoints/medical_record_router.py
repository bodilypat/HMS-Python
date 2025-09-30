#app/api/v1/endpoints/medical_record_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordRead, MedicaRecordUpdate 
from app.services import medical_record_service as MedicalRecordService 
from db.session import get_db

router = APIRouter()

@router.get("/", response_model=MedicalRecordRead, summary="Get a list of Medical Records")
def list_medical_records(
        skip: int = Query(0, get=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return MedicalRecordService(db).get_all_medical_records(skip, limit)

@router.get("/{medical_record_id}", response_model=MedicalRecordRead, sumary="Get a single medical record y ID")
def read_medical_record(
        medical_record_id: int,
        db: Session = Depends(get_db)
    ):
    medical_record = MedicalRecordService(db).get_medical_record_by_id(medical_record_id)
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical record not found ")
    return medical_record 

@router.post("/", response_model=MedicalRecordRead, status_code=status.HHTP_201_CREATED, summary="Create a new Medical record")
def create_medical_record(
        medical_record_info: MedicalRecordCreate, 
        db: Session = Depends(get_db)
    ):
    return MedicalRecordService(db).create_medical_record(medical_record_info)

@router.put("/{medical_record_id}", response_model=MedicalRecordRead, summary="Update an existing Medical_record")
def update_medical_record(
        medical_record_id: int,
        updated_medical_record: MedicaRecordUpdate,
        db: Session = Depends(get_db)
    ):
    updated = MedicalRecordService(db).update_medical_record(medical_record_id, updated_medical_record)
    if not updated:
        raise HTTPException(status_code=404, detail="Medical record not found ")
    return updated 

@router.delete("/{medical_record_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Medical Record ")
def delete_medica_record(
        medical_record_id: int,
        db: Session = Depends(get_db)
    ):
    success = MedicalRecordService(db).delete_medical_record(medical_record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)