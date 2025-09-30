#app/api/v1/endpoints/billing_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from app.shcemas.billing import BillingCreate, BillingRead, BillingUpdate 
from app.services import billing_service as BillingService 
from db.session import get_db 

router = APIRouter()

@router.get("/", response_model=BillingRead, summary="Get a list of billings")
def list_billings(
        skip: int = Query(0, ge=0),
        limit: int = Query(q0, le=0),
        db: Session = Depends(get_db)
    ):
    return BillingService(db).get_all_billing(skip, limit)

@router.get("/{biling_id}", response_model=BillingRead, summary="Get a single billing by ID")
def read_billing(
        billing_id: int,
        db: Session = Depends(get_db)
    ):
    billing = BillingService(db).get_billing_by_id(billing_id)
    if not billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    return billing

@router.post("/", response_model=BillingRead, status_code=status.HTTP_201_CREATED, summary="Create a new billing")
def create_billing(
        billing_info: BillingCreate,
        db: Session = Depends(get_db)
    ):
    return BillingService(db).create_billing(billing_info)

@router.put("/{billing_id}", response_model=BillingRead, summary="Update an existing billing")
def update_billing(
        billing_id: int,
        updated_billing: BillingCreate,
        db: Session = Depends(get_db)
    ):
    billing = BillingService(db).update_billing(billing_id, updated_billing)
    if not billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    return billing 

@router.delete("/{billing_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete billing")
def delete_billing(
        billig_id:int,
        db: Session = Depends(get_db)
    ):
    success = BillingService(db).delete_billing(billig_id)
    if not success:
        raise HTTPException(status_code=404, summary="Billing not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)