from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    email: EmailStr
    subscription_type: str
    scans_used: int
    
class Token(BaseModel):
    access_token: str
    token_type: str        