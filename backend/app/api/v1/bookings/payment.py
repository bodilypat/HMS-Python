#app/api/v1/bookings/payment.py 

from typing import List 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.bookings.payment import PaymentCreate, PaymentResponse, PaymentUpdate
from app.services.bookings import payment_service as PaymentService

router = APIRouter(prefix="payments", tags=["Bookings Payments"])

#--------------------------
# Create Payment
#--------------------------
@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(
    payment_in: PaymentCreate,
    db: Session = Depends(get_db)
) -> PaymentResponse:
    payment = PaymentService.create_payment(db=db, payment_in=payment_in)
    return payment

#--------------------------
# Get Payment by ID
#--------------------------
@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db)
) -> PaymentResponse:
    payment = PaymentService.get_payment(db=db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment
#--------------------------
# Get All Payments
#--------------------------
@router.get("/", response_model=List[PaymentResponse])
def get_payments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[PaymentResponse]:
    payments = PaymentService.get_payments(db=db, skip=skip, limit=limit)
    return payments
#--------------------------
# Update Payment
#--------------------------
@router.put("/{payment_id}", response_model=PaymentResponse)
def update_payment(
    payment_id: int,
    payment_in: PaymentUpdate,
    db: Session = Depends(get_db)
) -> PaymentResponse:
    payment = PaymentService.update_payment(db=db, payment_id=payment_id, payment_in=payment_in)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment
#--------------------------
# Delete Payment
@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db)
) -> None:
    success = PaymentService.delete_payment(db=db, payment_id=payment_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return None





