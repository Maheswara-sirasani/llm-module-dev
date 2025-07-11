from models import InvoiceCreate, Invoice
from typing import List
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
 
def calculate_invoice(invoice: InvoiceCreate, invoice_id: int) -> Invoice:
    subtotal = sum(item.quantity * item.price for item in invoice.items)
    tax = subtotal * invoice.tax_rate
    total = subtotal + tax
    return Invoice(
        id=invoice_id,
        client=invoice.client,
        items=invoice.items,
        subtotal=subtotal,
        tax=tax,
        total=total
    )
 
def generate_pdf(invoice: Invoice, filepath: str):
    c = canvas.Canvas(filepath, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750
    c.drawString(100, y, f"Invoice ID: {invoice.id}")
    c.drawString(100, y - 20, f"Client: {invoice.client}")
    y -= 60
 
    for item in invoice.items:
        c.drawString(100, y, f"{item.name} x {item.quantity} @ {item.price} = {item.quantity * item.price}")
        y -= 20
 
    y -= 20
    c.drawString(100, y, f"Subtotal: {invoice.subtotal}")
    c.drawString(100, y - 20, f"Tax: {invoice.tax}")
    c.drawString(100, y - 40, f"Total: {invoice.total}")
    c.save()

 