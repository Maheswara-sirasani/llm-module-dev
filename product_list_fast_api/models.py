from pydantic import BaseModel
 
class Product(BaseModel):
    product_name: str
    brand: str
    price: float
    stock: int
 
class BrandQuery(BaseModel):
    brand: str