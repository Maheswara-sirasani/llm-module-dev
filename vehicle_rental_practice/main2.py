from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import Optional
from passlib.context import CryptContext

app=FastAPI()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated=["auto"]) 

def hash_password(password:str)->str:
    return pwd_context.hash(password)
def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

class UserIn(BaseModel):
    name:str
    email:str
    password:str
    role:str="user"
    
class UserOut(BaseModel):
    email:str
    password:str

def user_help(user)->dict:
    return{
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "password":user["password"],
        "role":user["role"]
    }
    
client=MongoClient("mongodb://localhost:27017/") 
db=client["hashed_users_db"]  
users_db=db["users"]  

@app.post("/register")
async def user_register(user:UserIn):
    if users_db.find_one({"email":user.email}):
        raise HTTPException(status_code=400,detail="email already registred") 
    hashed_pw=hash_password(user.password)   
    user_data={"name":user.name,
               "email":user.email,
               "password":hashed_pw,
               "role":user.role
    }  
    result=users_db.insert_one(user_data)
    new_user=users_db.find_one({"_id":result.inserted_id}) 
    
    return{
        "message":"user registred success fully",
        "users":user_help(new_user)
    }
    
@app.post("/login") 
async def user_login(user:UserOut):
    users=users_db.find_one({"email":user.email})
    if not users:
        raise HTTPException(status_code=404,detail="invalid email")
    if not verify_password(user.password,users['password']):
          raise HTTPException(status_code=404,detail="invalid password")
    return{
        "message":"user logined sucessfully",
        "name":users["name"],
        "role":users["role"]
    }  