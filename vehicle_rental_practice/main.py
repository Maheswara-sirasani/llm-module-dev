from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from passlib.context import CryptContext

app=FastAPI()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def user_help(user)->dict:
    return{
        
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "password":user["password"]
        
     
    }
def vehicles_help(vehicles)->dict:
    return{
        "id":str(vehicles["_id"]),
        "vehicle_type":vehicles["vehicle_type"],
        "vehicle_brand":vehicles["vehicle_brand"],
        "number_plate":vehicles["number_plate"],
        "per_hour_price":vehicles["per_hour_price"]
    }    

class UserIn(BaseModel):
    name:str
    email:str
    password:str
    role:str="user"
    
class UserOut(BaseModel):
    email:str
    password:str
    
class Vehicles(BaseModel):
    vehicle_type:str
    vehicle_brand:str
    number_plate:str
    per_hour_price:float
    
   
    

client=MongoClient("mongodb://localhost:27017/")  
db=client['vehicles_practice_db']
vehicle_db=db['vehicles'] 
users_db=db['users'] 

def hash_password(password:str)->str:
    return pwd_context.hash(password)
def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

@app.post("/register")
async def user_register(user:UserIn):
    if users_db.find_one({"email":user.email}):
        raise HTTPException(status_code=400,detail="email already registered")
    hashed_pw=hash_password(user.password)
    user_data={"name":user.name,
               "email":user.email,
               "password":hashed_pw,
               "role":user.role}
    result=users_db.insert_one(user_data)
    new_result=users_db.find_one({"_id":result.inserted_id})
    return{
        "message":"user registered successfully","users":user_help(new_result)
    }
    
@app.post("/login")
async def user_login(user:UserOut):
    
    db_user=users_db.find_one({'email':user.email})
    if not db_user:
        raise HTTPException(status_code=401,detail="inavalid credentials") 
    if not verify_password(user.password,db_user['password']): 
        raise HTTPException(status_code=401,detail="invalid password")
    return{
       "message": "user logined sucessfully",
       "role":db_user["role"] 
    }  

@app.post("/register/vehicles")
async def vehicle_register(vehicles:Vehicles): 
    if vehicle_db.find_one({"number_plate":vehicles.number_plate}):
        raise HTTPException(status_code=404,detail="vehicle already registred") 
    vehicles=vehicle_db.insert_one(vehicles.dict())
    new_vehicles=vehicle_db.find_one({"_id":vehicles.inserted_id})
    return{
        "message":"vehicles registred successfully","vehicles":vehicles_help(new_vehicles)
    } 
    
@app.get("/users")
async def user_details():
    users=[user_help(u) for u in users_db.find()]
    return{
        "users":users
    }   
     
@app.get("/vehicles") 
async def vehicle_detail():
    vehicles=(vehicles_help(u) for u in vehicle_db.find())  
    return{
        "vehicles":vehicles
    } 
            

