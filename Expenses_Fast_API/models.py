from pydantic import BaseModel
from datetime import date
 
# Schema for an expense entry
class Expense(BaseModel):
    id: int
    date: date
    category: str
    amount: float
    description: str = ""
 