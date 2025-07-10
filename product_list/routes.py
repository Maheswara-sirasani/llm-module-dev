from fastapi import APIRouter, HTTPException
from typing import List
from models import Product, BrandQuery
from utility import load_products, save_products
 
router = APIRouter()
 
@router.get("/products", response_model=List[Product])
def get_products(product_name: str = None, brand: str = None):
    products = load_products()
    if product_name:
        products = [p for p in products if p.product_name.lower() == product_name.lower()]
    if brand:
        products = [p for p in products if p.brand.lower() == brand.lower()]
    return products
 
@router.get("/products/total")
def total_stock(product_name: str = None):
    products = load_products()
    if product_name:
        products = [p for p in products if p.product_name.lower() == product_name.lower()]
    total = sum(p.stock for p in products)
    return {"total_stock": total, "category": product_name or "all"}
 
@router.post("/products", response_model=Product)
def add_product(product: Product):
    products = load_products()
    for p in products:
        if p.product_name == product.product_name and p.brand == product.brand:
            raise HTTPException(status_code=400, detail="Product already exists.")
    products.append(product)
    save_products(products)
    return product
 