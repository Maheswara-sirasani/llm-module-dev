from pydantic import BaseModel
from typing import List
 
class Item(BaseModel):
    name: str
    quantity: int
    price: float
 
class InvoiceCreate(BaseModel):
    client: str
    items: List[Item]
    tax_rate: float = 0.18  
 
class Invoice(BaseModel):
    id: int
    client: str
    items: List[Item]
    subtotal: float
    tax: float
    total: float
 