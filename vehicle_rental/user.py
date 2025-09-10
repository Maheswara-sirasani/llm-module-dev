from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class UserCreate(BaseModel):
    name:str=Field(..., min_length=3,max_length=25)
    email:EmailStr
    password:str=Field(..., min_length=8,max_length=30)
    role:str="customer"
    
class UserLogib(BaseModel):
    email:EmailStr
    password:str
    
class UserOut(BaseModel):
    id:Optional[str]
    name:str
    email:EmailStr
    role:str
    
class Token(BaseModel):
    access_token:str
    token_type:str="bearer"
    
class TokenData(BaseModel):
    email:Optional[str]=None            
