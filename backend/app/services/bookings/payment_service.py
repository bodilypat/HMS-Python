#app/services/bookings/payment_service.py

from fastapi import HTTPException 
from app.schemas.bookings import PaymentCreate, PaymentResponse 
from app.crud.bookings.payment_crud import PaymentCRUD 

class PaymentService:
    def __init__(self):
        self.crud = PaymentCRUD()

    async def get_all(self, page: int, page_size:  int, booking_id: int = None) -> list[PaymentResponse]:
        payments = await self.crud.get_all_payments(page, page_size, booking_id)
        return [PaymentResponse.from_orm(payment) for payment in payments]
    
    async def get_by_id(self, payment_id: int) -> PaymentResponse:
        payment = await self.crud.get_payment_by_id(payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return PaymentResponse.from_orm(payment)
    
    async def create_payment(self, payment_create: PaymentCreate) -> PaymentResponse:
        payment = await self.crud.create_payment(payment_create)
        if payment.amount <= 0:
            raise HTTPException(status_code=400, detail="Payment amount must be greater than zero")
        return PaymentResponse.from_orm(payment)
    
    async def update_payment(self, payment_id: int, payment_update: PaymentCreate) -> PaymentResponse:
        payment = await self.crud.get_payment_by_id(payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        updated_payment = await self.crud.update_payment(payment_id, payment_update)
        if updated_payment.amount <= 0:
            raise HTTPException(status_code=400, detail="Payment amount must be greater than zero")
        return PaymentResponse.from_orm(updated_payment)
    
    async def delete_payment(self, payment_id: int) -> None:
        payment = await self.crud.get_payment_by_id(payment_id)
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        await self.crud.delete_payment(payment_id)
        return None
    
    