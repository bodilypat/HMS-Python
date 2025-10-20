#app/api/finance/billing_router.py

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.finance.billing import BillingCreate, BillingUpdate, BillingRead 
from services.finance import billing_service as BillingService 
from db.session import get_db

router = APIRouter(prefix="/billings", tags=["Billings"])

@router.get(
        "/",
        response_model=List[BillingRead],
        summary="List all billing records",
        description="Retrieve a paginated list of all billing records in the system."
    )
def read_billings(
        skip: int = Query(0, ge=0, description="Number of items to skip"),
        limit: int = Query(10, le=100, description="Maximum number of items to return."),
        db: Session = Depends(get_db)
    ):
    return BillingService(db).get_all_billings(skip,limit)

@router.get(
        "/{billing_id}",
        response_model=BillingRead,
        summary="Get billing by ID."
        description="Retrieve a specific billing record using its unique ID."
    )
def read_billing(
        billing_id: int,
        db: Session = Depends(get_db)
    ):
    billing = BillingService(db).get_billing_by_id(billing_id)
    if not billing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Billing not found")
    return billing 

@router.post(
        "/",
        response_model=BillingRead,
        status_code=status.HTTP_201_CREATED,
        summary=" Create a new billing record",
        description="Add a new billing entry for a reservation or transaction."
    )
def create_billing(
        billing_info: BillingCreate,
        db: Session = Depends(get_db)
    ):
    return BillingService(db).create_billing(billing_info)

@router.put(
        "/{billing_id}",
        response_model=BillingRead,
        summary="Update an existing billing record",
        description="update billing details like amount, or due date for a specific billing ID"
    )
def update_billing(
        billing_id: int,
        updated_billing:BillingUpdate,
        db: Session = Depends(get_db)
    ):
    updated = BillingService(db).update_billing(billing_id, updated_billing)
    if not updated:
        raise HTTPException(status_code=status.HTTP_NOT_FOUND, detail="Billing not found")
    return updated

@router.delete(
        "/{billing_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a billing record",
        description="Remove a billing entry from the system using its ID."
    )
def delete_billing(
        billing_id: int,
        db: Session = Depends(get_db)
    ):
    success = BillingService(db).delete_billing(billing_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Billing not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


