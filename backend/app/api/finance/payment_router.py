#app/api/finance/payment_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.finance.payment import PaymentCreate, PaymentRead, PaymentUpdate
from services.finance import payment_service as PaymentService
from db.session import get_db 

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.get(
        "/",
        response_model=List[PaymentRead],
        summary="List all payments",
        description="Retrieve a paginated list of all payment records in the system."
    )
def list_payment(
        skip: int = Query(0, ge=0, description="Number of record to skip."),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return PaymentService(db).get_all_payments(skip, limit)

@router.get(
        "/{payment_id}",
        response_model=PaymentRead,
        summary="Get payment by ID.",
        description="Retrieve a specific payment using its unique ID."
    )
def read_payment(
        payment_id: int,
        db: Session = Depends(get_db)
    ):
    payment = PaymentService(db).get_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment 

@router.post(
        "/",
        response_model=PaymentRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new payment",
        description="Create a new payment associated with an invoice or billing"
    )
def create_payment(
        payment_info: PaymentCreate,
        db: Session = Depends(get_db)
    ):
    return PaymentService(db).create_payment(payment_info)

@router.put(
        "/{payment_id}",
        response_model=PaymentRead,
        summary="Update a payment",
        description="Update an existing payment record using ts ID."
    )
def update_payment(
        payment_id: int,
        updated_payment: PaymentUpdate,
        db: Session = Depends(get_db)
    ):
    updated = PaymentService(db).update_payment(payment_id, updated_payment)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return updated 

@router.delete(
        "{payment_id}",
        status_code=status.HTTP_204_NOT_CONTENT,
        summary="Delete a payment",
        description="Remove a specific payment record from the system."
    )
def delete_payment(
        payment_id: int,
        db: Session = Depends(get_db)
    ):
    payment = PaymentService(db).delete_payment(payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return Response(status_code=status.HTTP_204_NOT_CONTENT)




