from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class  item(BaseModel):
    name:str
    price:float
    quantity:int
    
items=[]
@app.post("/items")
async def create_item(item:item):
    items.append(item.dict())
    return{
        "item created successfully"
    }
@app.get("/items")
async def get_item():
    return{"items":items}
        
    