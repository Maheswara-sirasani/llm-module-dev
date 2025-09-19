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
    
database=[]

@app.post("/register")
async def user_register(user:UserIn):
    for u in database:
        if u['email']==user.email:
            raise HTTPException(status_code=400,detail="email already exists")
        database.append(user.dict())
        return {"message":"user registred successfully"} 
@app.post("/login")
async def user_login(user:UserOut):
    for u in database:
        if u['email']==user.email and u['password']==user.password:
            return { "message":f"user login succcessfully {u['name']}"}
        raise HTTPException(status_code=401,detail="invalid crdentials")
@app.get("/users")
async def user_details():
    return{ "users":database}   
@app.put("/register/{email}")
async def user_updated(email:str,user_updated:UserIn):
    for idx,u in enumerate(database):
        if u['email']==email:
            database[idx]=user_updated.dict()
            return {"message":"user updated successfully","users":database[idx]}
        raise HTTPException(status_code=404,detail="user not found")
              