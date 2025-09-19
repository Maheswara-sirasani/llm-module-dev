from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 
app = FastAPI()
 
class UserIn(BaseModel):
    name: str
    email: str
    password: str
 
class UserOut(BaseModel):
    email: str
    password: str
 
database = []
 
 
@app.post("/register")
async def user_register(user: UserIn):
    # Check if email already exists
    for u in database:
        if u['email'] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
   
    # Append user and return success
    database.append(user.dict())
    return {"message": "User registered successfully", "user": user.dict()}
 
 
@app.post("/login")
async def user_login(user: UserOut):
    for u in database:
        if u['email'] == user.email and u['password'] == user.password:
            return {"message": f"User login successfully {u['name']}"}
   
    raise HTTPException(status_code=401, detail="Invalid credentials")
 
 
@app.get("/users")
async def user_details():
    return {"users": database}
 
 
@app.put("/register/{email}")
async def user_updated(email: str, user_updated: UserIn):
    for idx, u in enumerate(database):
        if u['email'] == email:
            database[idx] = user_updated.dict()
            return {"message": "User updated successfully", "user": database[idx]}
   
    raise HTTPException(status_code=404, detail="User not found")
 
 