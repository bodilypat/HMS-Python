#app/api/finance/invoice_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from schema.finance.invoice import InvoiceCreate, InvoiceUpdate, InvoiceRead
from db.session import get_db 
from service.finance import invoice_service as InvoiceService 

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.get(
        "/",
        response_model=List[InvoiceRead],
        summary="List all invoices",
        description="Retrieve a paginated list of all invoices using its unique ID."
    )
def list_invoices(
        skip: int = Query(0, ge=0, description="Number of records to skip."),
        limit: int = Query(10, le=100, description="Maximum number of records to return."),
        db: Session = Depends(get_db)
    ):
    return InvoiceService(db).get_all_incvoices(skip, limit)

@router.get(
        "/{invoice_id}",
        response_model=InvoiceRead,
        summary="Get invoice by ID.",
        description="Fetch details of specific invoice using its unique ID."
    )
def read_invoice(
        invoice_id: int,
        db: Session = Depends(get_db)
    ):
    invoice = InvoiceService(db).get_invoice_by_id(invoice_id)
    if not invoice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    return invoice 

@router.post(
        "/",
        response_model=InvoiceRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new invoice",
        description="Generate a new invoice for a transaction or billing entry."
    )
def create_invoice(
        invoice_data: InvoiceCreate,
        db: Session = Depends(get_db)
    ):
    return InvoiceService(db).create_invoice(invoice_data)

@router.put(
        "/{invoice_id}",
        response_model=InvoiceRead,
        summary="Update invoice",
        description="Midify the details of an existing invoice using its ID."
    )
def update_invoice(
        invoice_id: int,
        updated_invoice: InvoiceUpdate,
        db: Session = Depends(get_db)
    ):
    updated = InvoiceService(db).update_invoice(invoice_id, updated_invoice)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    return updated

@router.delete(
        "/{invoice_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete invoice",
        description="Remove a specific invoice from the system."
    )
def delete_invoice(
        invoice_id: int,
        db: Session = Depends(get_db)
    ):
    deleted = InvoiceService(db).delete_invoice(invoice_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


