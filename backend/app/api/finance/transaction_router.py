#app/api/finance/transaction_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.finance.transaction import TransactionCreate, TransactionRead, TransactionUpdate
from services.finance import transaction_service as TransactionService 
from db.session import transaction_service as TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get(
        "/",
        response_model=List[TransactionRead],
        summary="List all Transactions",
        description="Retrieve a paginated list of all transaction records."
    )
def list_transactions(
        skip: int = Query(0, ge=0, description="Number of records to skip."),
        limit: int = Query(10, le=100, description="Maximum number of records to return."),
        db: Session = Depends(get_db)
    ):
    return TransactionService(db).get_all_transactions(skip, limit)

@router.get(
        "/{transaction_id}",
        response_model=TransactionRead,
        summary="Get a transaction by ID.",
        description="Retrieve the details of a transaction using its unique identifier."
    )
def read_transaction(
        transaction_id: int,
        db: Session = Depends(get_db)
    ):
    transaction = TransactionService(db).get_transaction_by_id(transaction_id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return transaction 

@router.post(
        "/",
        response_model=TransactionCreate,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new transaction",
        discription="Add in new transaction record, typical linked to a payment or booking"
    )
def create_transaction(
        transaction_info: int,
        db: Session = Depends(get_db)
    ):
    return TransactionService(db).create_transaction(transaction_info)

@router.put(
        "/{transaction_id}",
        response_model=TransactionRead,
        summary="Update an existing transaction",
        description="Update the details of a transaction using its ID."
    )
def update_transaction(
        transaction_id: int,
        updated_transaction: TransactionUpdate,
        db: Session = Depends(get_db)
    ):
    updated = TransactionService(db).update_transaction(transaction_id, updated_transaction)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return updated

@router.delete(
        "{transactionn_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a transaction",
        description="Delete a transaction record from the system by its ID."
    )
def delete_transaction(
        transaction_id: int,
        db: Session = Depends(get_db)
    ):
    success = TransactionService(db).delete_transaction(transaction_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT, detail="Transaction not found")
    return Response(status_code=status.HTTP_204_NOT_CONTENT)


