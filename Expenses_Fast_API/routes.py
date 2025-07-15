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
@router.put("/expenses/{expense_id}", response_model=Expense)
def update_expense(expense_id: int, updated_expense: Expense):
    expenses = load_expenses()
    for index, exp in enumerate(expenses):
        if exp.id == expense_id:
            expenses[index] = updated_expense
            save_expenses(expenses)
            return updated_expense
    raise HTTPException(status_code=404, detail="Expense not found")
@router.get("/expenses/{expense_id}", response_model=Expense)
def get_expense_by_id(expense_id: int):
    expenses = load_expenses()
    for expense in expenses:
        if expense.id == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")
@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()
    for index, expense in enumerate(expenses):
        if expense.id == expense_id:
            deleted_expense = expenses.pop(index)
            save_expenses(expenses)
            return {"message": "Expense deleted", "deleted": deleted_expense}
    raise HTTPException(status_code=404, detail="Expense not found")
 
 
 
