from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class detail(BaseModel):
    name:str
    phone_number:str
    location:str
    
details=[]

@app.post("/details")
async def user_details(detail:detail):
    details.append(detail.dict())
    
    return{"details updated successfully"}
@app.get("/details")
async def get_details():
    return{
        "details":details
    }

    
    