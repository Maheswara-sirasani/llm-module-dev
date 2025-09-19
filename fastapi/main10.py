from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from pymongo import MongoClient
from bson import ObjectId

app=FastAPI()

def user_helper(user) -> dict:
    return{
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "password":user["password"]
    }


class UserIn(BaseModel):
    name:str=Field(...,min_length=3,max_length=25)
    email:str
    password:str=Field(...,min_length=8,max_length=20)
    
client=MongoClient("mongodb://localhost:27017/") 
db=client['practice']  
users_db=db['users'] 

@app.post("/register")
async def user_register(user:UserIn):
    if users_db.find_one({"email":user.email}):
        raise HTTPException(status_code=400,detail="email already registred")
    result=users_db.insert_one(user.dict())
    new_user=users_db.find_one({"_id":result.inserted_id})
    return{
        "message":"user registred successfully ","user":user_helper(new_user)
    }
    
@app.get("/users")
async def user_details():
    users=[user_helper(u) for u in users_db.find()]
    return{"users":users}    