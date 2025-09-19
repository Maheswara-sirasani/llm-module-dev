from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class UserIn(BaseModel):
    name:str
    email:str
    password:str
    
class UserOut(BaseModel):
    email:str
    password:str    
    
users_db=[]

@app.post("/register")
async def user_register(user:UserIn):
    for u in users_db:
       if u["email"]==user.email:
           raise HTTPException(status_code=400,detail="email already registred")
    users_db.append(user.dict())
    return{
        "user registred successfully"
    }
@app.post("/login")   
async def user_login(user:UserOut):
    for u in users_db:
      if u["email"]==user.email and u["password"]==user.password:
          return{f"user logined successfull{u['name']}"}
    raise HTTPException(status_code=401,detail="invalid credentials")      
          
@app.get("/users") 
async def user_details():
    return{
        "users":users_db
    }   
        