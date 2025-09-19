from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from pymongo import MongoClient

app=FastAPI()

class UserIn(BaseModel):
    name:str
    email:str
    password:str=Field(...,min_length=6,max_length=20)
    role:str
    
class UserOut(BaseModel):
    email:str
    password:str
    
    
class UserUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    password:Optional[str]=Field(None,min_length=6,max_length=20)
    role:Optional[str]=None
    
client=MongoClient("mongodb://localhost:27017/") 
db=client['fastapi']   
users_collection=db['users']

@app.post("/register")
async def user_register(user:UserIn):
    if users_collection.find_one({"email":user.email}):
      raise HTTPException(status_code=400,detail="email already registred")
    users_collection.insert_one(user.dict())
    return{
        "message":"user registred successfullys"
    }   
@app.post("/login")
async def user_login(user:UserOut):
    for u in users_collection:
        if u['email']==user.email and u['password']==user.password:
            return {
                f"user logined successfully  {u['name']}"
            }
    raise HTTPException(status_code=401,detail="invalid password or email")
@app.put("/register/{email}")
async def updated_user(email:str,updated_user:UserUpdate):
    for idx,u in enumerate(users_collection):
        if u['email'] == email:  
            if updated_user.name is not None:
                u['name']=updated_user.name
            if updated_user.email is not None:
                u['email']=updated_user.email    
            if updated_user.password is not None:
                u['password']=updated_user.password
            if updated_user.role is not None:
                u['role']=updated_user.role       
            users_collection[idx]=u
            return{
                "message":f"user updated successfully{u['name']}","users":users_collection[idx]
            }  
    raise HTTPException(status_code=404,detail="user not found")  
@app.get("/users")
async def users_details():
    users=list(users_collection.find({},{"_id":0}))
    return{
        "users":users
    }      
@app.delete("/register/{email}")
async def user_delete(email:str):
    for idx,u in enumerate(users_collection):
        if u['email']==email:
            user_delete=users_collection.pop(idx)
            return {
                "message":"users deleted successfully","users":user_delete
            }  
    raise HTTPException(status_code=404,detail="user not found")        

    
    