#app/controller/finance/transaction_router.py 

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemas.orm import Session
from typing import List 

from schemas.finance.transaction import TransactionCreate, TransactionUpdate, TransactionRead 
from db.session import get_db
from services.finance import transaction_service 

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=List[TransactionRead], summary="Get a list of Transactions")
def read_transactions(
        skip: int = query(0, ge=0),
        limit: int = query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return transaction_service.get_all_transactions(db, skip, limit)

@router.get("/{transaction_id}", response_model=TransactionRead, summary="Get a single Transaction by ID")
def read_transaction(
        transaction_id: int,
        db: Session = Depends(get_db)
    ):
    transaction = transaction_service.get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction 

@router.post("/", response_model=TransactionRead, status_code=status.HTTP_201_CREATED, summary="Create a new Transaction")
def create_transaction(
        transaction: TransactionCreate,
        db: Session = Depends(get_db)
    ): 
    return transaction_service.create_transaction(db, transaction)

@router.put("/{transaction_id}", response_model=TransactionRead, summary="Update an existing Transaction")
def update_transaction(
        transaction_id: int ,
        updated_transaction: TransactionUpdate,
        db: Session = Depends(get_db)
    ):
    updated = transaction_service.update_transaction(db, transaction_id, updated_transaction)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated 

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Transaction")
def delete_transaction(
        transaction_id: int,
        db: Session = Depends(get_db)
    ):
    success = transaction_service.delete_transaction(db, transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return Response(status_code=status.HTTP_NO_CONTENT)