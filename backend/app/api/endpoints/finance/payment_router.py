#app/controller/finance/payment_router.py 

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from schemas.billing.payment import PaymentCreate, PaymentRead, PaymentUpdate 
from services.payment import payment_service as PaymentService 
from db.session  import get_db 

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.get("/", response_model=List[PaymentRead], summary="Get a list of Payments")
def get_payments(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return PaymentService(db).get_all_payments(skip, limit)

@router.get("/{payment_id}", response_model=PaymentRead, summary="Get a single of Payments")
def read_payment(
        payment_id: int,
        db: Session = Depends(get_db)
    ):
    payment = PaymentService(db).get_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment 

@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED, summary="Create a new Payment")
def create_payment(
        payment_in: PaymentCreate,
        db: Session = Depends(get_db)
    ):
    return PaymentService(db).create_payment(payment_in)

@router.put("/{payment_id}", response_model=PaymentRead, summary="Update an existing payment")
def update_payment(
        payment_id: int,
        updated_payment: PaymentUpdate,
        db: Session = Depends(get_db)
    ):
    updated = PaymentService(db).update_payment(payment_id, updated_payment)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated 

@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Payment")
def delete_payment(
        payment_id: int,
        db: Session = Depends(get_db)
    ):
    success = PaymentService(db).delete(payment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Payment not found")
    return Response(status_code=status.HTTP_NO_CONTENT)
