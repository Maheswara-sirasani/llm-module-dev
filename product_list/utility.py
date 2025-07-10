import os
import json
from typing import List
from models import Product
 
PRODUCT_LIST_FILE = "Products.json"
 
def load_products() -> List[Product]:
    if not os.path.exists(PRODUCT_LIST_FILE):
        with open(PRODUCT_LIST_FILE, "w") as f:
            json.dump([], f)
        return []
 
    try:
        with open(PRODUCT_LIST_FILE, "r") as f:
            data = json.load(f)
            return [Product(**item) for item in data]
    except (json.JSONDecodeError, TypeError):
        # If file is corrupted, reset it
        with open(PRODUCT_LIST_FILE, "w") as f:
            json.dump([], f)
        return []
 
def save_products(products: List[Product]):
    with open(PRODUCT_LIST_FILE, "w") as f:
        json.dump([product.dict() for product in products], f, indent=4)
 