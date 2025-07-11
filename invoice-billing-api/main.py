from fastapi import FastAPI
from routers import router as invoice_router
 
app = FastAPI(title="Invoice & Billing API")
 
app.include_router(invoice_router, prefix="/invoices", tags=["Invoices"])
 