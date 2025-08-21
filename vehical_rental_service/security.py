from datetime import datetime,timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from config import settings


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain:str,hashed:str) -> str:
    return pwd_context.verify(plain,hashed)

def create_access_token(sub:str,expires_minutes:Optional[int]=None) ->str:
    expire=datetime.utcnow() + timedelta(minutes=expires_minutes or settings.jwt_expire_minutes)
    payload={"sub":sub,"exp":expire}
    
    return jwt.encode(payload,settings.jwt_secret,alogorithm=settings.jwt_algorithm)  

def decode_token(token:str) -> dict:
    return jwt.decode(token,settings.jwt_secret,alogorithms=[settings.jwt_algorithm])






    
    
