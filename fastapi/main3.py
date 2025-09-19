from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class UserIn(BaseModel):
    name:str
    email:str
    password:str
    
users_db=[]

@app.post("/login")
async def user_login(user:UserIn):
    users_db.append(user.dict())
    return{
        "login details updated"
    } 
@app.get("/users")    
async def get_user():
    return{
        "UserIns":users_db
    }   
    