# backend/app/api/v1/endpoints/payment.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from typeing import list

from backend.app.sevices import paymet_service
from backend.app.deps import get_db

router = APIRouter(
	prefix='/payments",
	tags=["Payments"]
	)
	
	router = APIRouter(
		prefix="/payments",
		tags=["Payments"]
	)
	
	@router.post("/", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
    def create_payment(
            payment_in: PaymentCreate,
            db: Session = Depends(get_db)
        ):
        """
            Create a new payment record.
        """
        payment = payment_service.create_payment(db, payment_in)
        if not payment:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create payment."
            )
        return payment 
        
    @router.get("/{payment_id}", response_model=PaymentOut)
    def get_payment_by_id(
            payment_id: int 
            db: Session = Depends(get_db)
        ):
        """
            Retrieve a payment by its ID.
        """
        payment = payment_service.get_payment_by_id(db, payment_id)
        if not payment:
            raise HTTPException (
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patment not found."
            )
            return payment
    @router.get("/", response_model=List[PaymentOut]
        def update_payment(
            payment_id: int,
            payment_update: PaymentUpdate,
            db: Session = Depends(get_db)
        ):
            """
                Delete a payment by ID.
            """
        success = payment_service.delete_payment(db, payment_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detailt=f"Payment with ID {payment_id} not found or could not be deleted."
            )
    