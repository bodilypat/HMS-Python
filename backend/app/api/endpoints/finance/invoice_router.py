#app/controller/finance/invoices_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.finance.invoice import InvoiceCreate, InvoiceUpdate, InvoiceRead 
from db.session import get_db 
from services.finance import invoice_service 

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.get("/", response_model=List[InvoiceRead], summary="Get a list of Invoices")
def read_invoices(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, 100),
        db: Session = Depends(get_db)
    ):
    return invoice_service.get_all_invoices(db, skip, limit)

@router.get("/{invoice_id}", response_model=InvoiceRead, summary="Get a single invoice by ID")
def read_invoice(
        invoice_id: int,
        db: Session = Depends(get_db)
    ):
    invoice = invoice_service.get_invoice_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice 

@router.post("/", response_model=InvoiceRead, status_code=status.HTTP_201_CREATED, summary="Create a new invoice")
def create_invoice(
        invoice: InvoiceCreate,
        db: Session = Depends(get_db)
    ):
    return invoice_service.create_invoice(db, invoice)

@router.put("/{invoice_id}", response_model=InvoiceRead, summary="Update an existing invoice")
def update_invoice(
        invoice_id: int,
        updated_invoice: InvoiceUpdate,
        db: Session = Depends(get_db)
    ):
    updated = invoice_service.update_invoice(db, invoice_id, updated_invoice)
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return updated 

@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Invoice")
def delete_invoice(
        invoice_id: int,
        db: Session = Depends(get_db)
    ):
    success = invoice_service.delete_invoice(db, invoice_id)
    if not success:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)