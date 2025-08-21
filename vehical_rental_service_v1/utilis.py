from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from typing import Optional
 
load_dotenv()
 
SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm", "HS256")
ACCESS_TOKEN_EXPIRE_TIME = int(os.getenv("access_token_expire_time", 60)) 
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = dict(data)  
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
 
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
 