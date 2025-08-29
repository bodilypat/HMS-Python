#backend/app/controllers/finance/billing_controller.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typig import List 

from backend.app.services import billing_service
from backend.app.deps import get_db
from backend.app.schemas.billing import BillingCreated, BillingUpdate, BillingOut 

router = APIRouter(
		prefix="/billing",
		tags=["Billing"]
	)
	
@router.post("/", response_model=BillingOut, status_code=status.HTTP_201_CREATED)
def create_bill(
		billing_in: BillingCreate,
		db: Session = Depends(get_db)
	):
	"""
		Create a new billing record.
	"""
	create_bill = billing_service.create_bill(db, biling_in)
	if not create_bill:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST.
			detail="Failed to create billing record."
		)
	return create_bill
	
@router.get("/{billing_id}", response_model=BillingOut)
def get_billing_by_id(
        billing_id: int,
        db: Session = Depends(get_db)
    )
    """
        Retrieve a billing record by its ID.
    """
    billing = billing_service.get_billing_by_id(db, billing_id)
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Billing record not found."
        )
    return billing
    
@router.get("/", response_model=List[BillingOut])
def get_all_billings(
        db: Session = Depends(get_db)
    ):
    """
        List all billing records.
    """
    return billing_service.get_all_billings(db)
    
@router.put("/{billing_id}", response_model=BillingOut)
def update_billing(
        billing_id: int,
        billing_update: BillingUpdate,
        db: Session = Depends(get_db)
    ):
    """
        Update an existing billing record. 
    """
    updated_billing = billing_service.update_bill(db, bill_id, billing_update)
    if not updated_billing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing record with ID {billing_id} not found or could not be updated."
        )
    return updated_billing
 
@router.delete("/{billing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_billing(
        billing_id: int,
        db: Sessionj = Depends(get_db)
    ):
    """
        Delete a billing record by its ID.
    """
    del_billing = billing_service.delete_billing(db, billing_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Billing record with ID {billing_id] not found or could not be deleted."
        )
        
        