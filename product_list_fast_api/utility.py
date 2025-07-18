import json
from models import Product
from typing import List
from pathlib import Path
 
DATA_FILE = Path("products.json")
 
def load_products() -> List[Product]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Product(**item) for item in data]
 
def save_products(products: List[Product]):
    with open(DATA_FILE, "w") as f:
        json.dump([p.dict() for p in products], f, indent=4)
 