from fastapi import APIRouter, HTTPException
from models import InvoiceCreate, Invoice
from database import db
from utils import calculate_invoice, generate_pdf
import os
 
router = APIRouter()
 
@router.post("/", response_model=Invoice)
def create_invoice(invoice_data: InvoiceCreate):
    invoice_id = len(db) + 1
    invoice = calculate_invoice(invoice_data, invoice_id)
    db.append(invoice)
 
    # Save invoice PDF
    pdf_dir = "invoices"
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"invoice_{invoice.id}.pdf")
    generate_pdf(invoice, pdf_path)
 
    return invoice
 
@router.get("/", response_model=list[Invoice])
def list_invoices():
    return db
 
@router.get("/{invoice_id}", response_model=Invoice)
def get_invoice(invoice_id: int):
    for invoice in db:
        if invoice.id == invoice_id:
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")

 