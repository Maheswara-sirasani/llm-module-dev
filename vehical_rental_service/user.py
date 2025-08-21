from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class UserCreate(BaseModel):
    name:str=Field(..., min_length=3, max_length=20)
    emil:EmailStr
    password:str=Field(..., min_length=8,  max_length=25)
    role:Optional[str]=""  #customer or admin


class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
class UserOut(BaseModel):
    id:str
    email:EmailStr
    password:str
    role:str
    
class Token(BaseModel):
    access_token:str
    token_type:str="bearer"
        
        
    
