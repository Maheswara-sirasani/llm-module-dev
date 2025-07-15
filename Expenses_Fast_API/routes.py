from fastapi import APIRouter, HTTPException
from typing import List
from models import Expense
from utils import load_expenses, save_expenses
 
router = APIRouter()
 
@router.get("/expenses", response_model=List[Expense])
def get_expenses():
    return load_expenses()
 
@router.post("/expenses", response_model=Expense)
def add_expense(expense: Expense):
    expenses = load_expenses()
    if any(e.id==expense.id for e in expenses):
        raise HTTPException(status_code=400,detail="id already exit")
    expenses.append(expense)
    save_expenses(expenses)
    return expense
@router.get("monthly-total/{year}/{month}")
def get_monthly_total(year:int,month:int):
    expenses=load_expenses()
    total=sum(e.amount for e in expenses if e.date.year==year and e.date.month==month)
    return{"year":year,"month":month,"total":total}
@router.get("/expenses/total")
def get_total_expenses():
    expenses = load_expenses()
    total = sum(exp.amount for exp in expenses)
    return {"total": total}
 
