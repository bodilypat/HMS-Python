# backend/app/controllers/payment_controller.py

from fastapi import APIRouter, HTTPException, status
from backend.app.schemas.payment_schema import PaymentCreateSchema, PaymentResponseSchema
from backend.app.services.payment_service  import PaymentService 

router = APIRouter(prefix="/payments", tags=["Payment"])

@router.post("/", response_model=PaymentResponseSchema, status_code=status.HTTP_201_CREATED)
def create_payment(payment_data: PaymentCreateSchema):
	"""
		Record a new payment for a reservation.
	"""
	
	payment_id = PaymentService.create_payment(payment_data.dict())
	if not payment_id:
		raise HTTPException(status_code=400, detail="Payment creation failed.")
		return PaymentService.get_payment_by_id(payment_id)
		
@router.get("/{payment_id}", response_model=PaymentReponseSchema)
def get_payment(payment_id: int):
	"""
		Get Payment details by ID.
	"""
	payment = PaymentService.get_payment_by_id(payment_id)
	if not payment:
		raise HTTPException(status_code=404,detail="Payment not found.")
	return payment
	
@router.get("/reservation/{reservation_id}", response_model=list[PaymentResponseSchema])
def get_payments_by_reservation(reservation_id: int):
	"""
	   List all payments for a specific reservation.
	"""
	return PaymentService.get_payments_by_reservation(reservation_id)
	
@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(payment_id: int)
	"""
		Delete a payment record.
	"""
	success = PaymentService.delete_payment(payment_id)
	if not success:
		raise HTTPException(status_code=404, detail="Payment not found or could not be deleted.")
		