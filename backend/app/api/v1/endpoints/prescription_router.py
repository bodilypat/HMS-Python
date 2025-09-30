#app/api/v1/endpoints/prescription_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, response 
from sqlalchemy.orm import Session 
from app.schemas.prescription import PrescriptionCreate, PrescriptionRead, PrescriptionUpdate 
from app.service import perscription_service as PrescriptionService 
from typing import List
from db.session import get_db

router = APIRouter()

@router.get("/", response_model=PrescriptionRead, summary="Get a list of prescriptions")
def list_prescript(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return PrescriptionService(db).get_all_prescription(skip, limit)

@router.get("/{prescription_id}", response_model=PrescriptionRead, summary="Get a single prescription by ID")
def read_prescription(
        prescription_id: int,
        db: Session = Depends(get_db)
    ):
    prescription = PrescriptionService(db).get_prescript_by_id(prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription 

@router.post("/", response_model=PrescriptionRead, status_code=status.HTTP_201_CREATED, summary="Create a new prescripption")
def create_prescription(
        prescription_info: PrescriptionCreate,
        db: Session = Depends(get_db)
    ):
    return PrescriptionService(db).create_prescription(prescription_info)

@router.put("/{prescription_id}", response_model=PrescriptionRead, summary="Update an existing prescription")
def update_prescription(
        prescription_id: int,
        updated_prescription: PrescriptionUpdate,
        db: Session = Depends(get_db)
    ):
    updated = PrescriptionService(db).update_prescription(prescription_id, updated_prescription)
    if not updated:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return updated 

@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete prescription")
def delete_prescription(
        prescription_id: int,
        db: Session = Depends(get_db)
    ):
    success = PrescriptionService(db).delete_prescript(prescription_id)
    if not success:
        raise HTTPException(status_code=404, detail="Prescription not found ")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    