from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from pymongo import MongoClient
from bson import ObjectId

app=FastAPI()

def user_help(user) -> dict:
    return{
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "password":user["password"]
    }   


class User(BaseModel):
    name:str
    email:str
    password:str
    
client=MongoClient("mongodb://localhost:27017/")  
db=client['practice1'] 
users_db=db['users']

@app.post("/register")
async def user_register(user:User):
    if users_db.find_one({"email":user.email}):
        raise HTTPException(status_code=400,detail="user already registered")
    result=users_db.insert_one(user.dict())
    new_user=users_db.find_one({"_id":result.inserted_id})
    return{
        "message":"user registred successfully","user":user_help(new_user)
    }
@app.get("/users")
async def users():
    users=(user_help(u) for u in users_db.find())
    return{
        "users":users
    }       