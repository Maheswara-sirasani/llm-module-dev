from pydantic import BaseModel
from datetime import date


class Product(BaseModel):
    product_name: str
    brand: str
    price: float
    stock: int
    date: date
 
   
    
class BrandQuery(BaseModel):
    brand:str    