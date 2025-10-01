#app/api/finance/billing_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.billing.billing import BillingCreate, BillingRead, BillingUpdate  
from services.billing import billing_service as BillingService 
from db.session import get_db

router = APIRouter(prefix="/billings", tags=["Billings"])

@router.get("/", response_model=List[BillingRead], summary="Get a list of Billings")
def read_billings(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return BillingService(db).get_all_billings(skip, limit)

@router.get("/{billing_id}", response_model=BillingRead, detail="Get a single billing by ID")
def read_biiling(
        billing_id: int,
        db: Session = Depends(get_db)
    ):
    billing = BillingService(db).get_biling_by_id(billing_id)
    if not billing:
        raise HTTPException(status_code=404, detail="Billing not found")
    return billing

@router.post("/", response_model=BillingRead, status_code=status.HTTP_201_CREATED, detailt="Create a new billing by ID")
def create_billing(
        billing_in: BillingCreate,
        db: Session = Depends(get_db)
    ):
    return BillingService(db).create_billing(billing_in)

@router.put("/{billing_id}", response_model=BillingRead, detail="Update an existing billing")
def update_billing(
        billing_id: int,
        updated_billing: BillingUpdate,
        db: Session = Depends(get_db)
    ):
    updated = BillingService(db).update_billing(billing_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Billing not found")
    return updated

@router.delete("/{billing_id}", status_code=status.HTTP_204_NO_CONTENT, detail="Delete billing")
def delete_billing(
        billing_id: int,
        db: Session = Depends(get_db)
    ):
    success = BillingService(db).delete_billing(billing_id)
    if not success:
        raise HTTPException(status_code=404, detail="Billing not found")
    return response(status_code=status.HTTP_N0_CONTENT)
