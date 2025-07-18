from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from models import user_collection
import os
from dotenv import load_dotenv
 
load_dotenv()
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
 
def get_user(email: str):
    return user_collection.find_one({"email": email})
 
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(email)
    if not user:
        raise credentials_exception
    return user
 