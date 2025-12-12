#app/api/v1/billings.py

from fastapi import APIRouter, Depends, Query 
from typing import Optional, List 
from app.schemas.billings import (
    BillingCreate,
    BillingUpdate,
    BillingOut  
)
from app.services.billings.billing_service import  BillingService 

router = APIRouter()

#-----------------------------
# Get All Billings
#-----------------------------
@router.get("/", response_model=List[BillingOut], tags=["Billings"])
async def get_all_billings(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    guest_id: Optional[int] = None,
    booking_id: Optional[int] = None,
    status: Optional[str] = None,
    billing_service: BillingService = Depends()
):
    """ 
    Retrieve all billings with optional filtering by guest_id or booking_id, and pagination support.
    """
    return await billing_service.get_all_billings(
        page=page, 
        page_size=page_size, 
        guest_id=guest_id, 
        booking_id=booking_id,
        status=status
    )

#-----------------------------
#  Get Billing by ID
#-----------------------------
@router.get("/{billing_id}", response_model=BillingOut, tags=["Billings"])
async def get_billing_by_id(
    billing_id: int,
    billing_service: BillingService = Depends()
):
    """ 
    Retrieve a billing by its ID.
    """
    return await billing_service.get_billing_by_id(billing_id=billing_id)

#------------------------------
# Create New Billings
#------------------------------
@router.post("/", response_model=BillingOut, tags=["Billings"])
async def create_billing(
    billing: BillingCreate,
    billing_service: BillingService = Depends()
):
    """ 
    Create a new billing entry.
    """
    return await billing_service.create_billing(billing=billing)

#------------------------------
# Update Billings
#------------------------------
@router.put("/{billing_id}", response_model=BillingOut, tags=["Billings"])
async def update_billing(
    billing_id: int,
    billing: BillingUpdate,
    billing_service: BillingService = Depends()
):
    """ 
    Update an existing billing entry by its ID.
    """
    return await billing_service.update_billing(billing_id=billing_id, billing=billing)

#-------------------------------
# Delete Billing
#-------------------------------
@router.delete("/{billing_id}", response_model=BillingOut, tags=["Billings"])
async def delete_billing(
    billing_id: int,
    billing_service: BillingService = Depends()
):
    """ 
    Delete a billing entry by its ID.
    """
    await billing_service.delete_billing(billing_id=billing_id)
    return {"message": "Billing deleted successfully."}


