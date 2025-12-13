#app/services/billings/billing_service.py

from fastapi import HTTPException
from app.schemas.billings import BillingCreate, billingUpdate, BillingResponse 
from app.crud.billings.billing_crud import BillingCRUD 

class BillingService:
    def __init__(self):
        self.billing_crud = BillingCRUD()

#-----------------------------
# GET ALL BILLINGS
#-----------------------------
    async def get_all(self, page: int, page_size: int, guest_id: int = None):
        billings = await self.billing_crud.get_all(page, page_size, guest_id)
        return [BillingResponse.from_orm(billing) for billing in billings]
    
#-----------------------------
# GET BILLING BY ID
#-----------------------------
    async def get_by_id(self, billing_id: int):
        billing = await self.billing_crud.get_by_id(billing_id)
        if not billing:
            raise HTTPException(status_code=404, detail="Billing not found")
        return BillingResponse.from_orm(billing)
    
#-----------------------------
# CREATE BILLING
#-----------------------------
    async def create(self, billing_create: BillingCreate):
        billing = await self.billing_crud.create(billing_create)
        return BillingResponse.from_orm(billing)

#-----------------------------
# UPDATE BILLING
#-----------------------------
    async def update(self, billing_id: int, billing_update: billingUpdate):
        billing = await self.billing_crud.get_by_id(billing_id)
        if not billing:
            raise HTTPException(status_code=404, detail="Billing not found")
        updated_billing = await self.billing_crud.update(billing_id, billing_update)
        return BillingResponse.from_orm(updated_billing)
    
#-----------------------------
# MARK AS PAID
#-----------------------------
    async def mark_as_paid(self, billing_id: int):
        paid = await self.billing_crud.update_status(billing_id, "paid")
        if not paid:
            raise HTTPException(status_code=404, detail="Billing not found")
        return BillingResponse.from_orm(paid)
    
#-----------------------------
# CANCEL BILLING
#-----------------------------
    async def cancel(self, billing_id: int):
        cancelled = await self.billing_crud.update_status(billing_id, "cancelled")
        if not cancelled:
            raise HTTPException(status_code=404, detail="Billing not found")
        return BillingResponse.from_orm(cancelled)
    
#-----------------------------
# DELETE BILLING
#-----------------------------
    async def delete(self, billing_id: int):
        deleted = await self.billing_crud.delete(billing_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Billing not found")
        return BillingResponse.from_orm(deleted)
    
    