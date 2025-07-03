import os
import json
from typing import List
from models import Product

Product_list_file = "Products.json"

def load_products() -> List[Product]:
     if not os.path.exists(Product_list_file):
            with open(Product_list_file, "w") as f:
             json.dump([], f)
 
     with open(Product_list_file, "r") as f:
       return [Product(**exp) for exp in json.load(f)]
 
# Save products to the JSON file
def save_products(products: List[Product]):
    with open(Product_list_file, "w") as f:
        json.dump([exp.dict() for exp in products], f, indent=2)
 
    
    
