import os
import json
from typing import List
from models import Expense
 
EXPENSES_FILE = "expenses.json"
 
# Load all expenses from the JSON file
def load_expenses() -> List[Expense]:
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w") as f:
            json.dump([], f)
 
    with open(EXPENSES_FILE, "r") as f:
        return [Expense(**exp) for exp in json.load(f)]
 
# Save expenses to the JSON file
def save_expenses(expenses: List[Expense]):
    with open(EXPENSES_FILE, "w") as f:
        json.dump([exp.dict() for exp in expenses], f, indent=2)
 