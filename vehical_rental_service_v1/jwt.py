import os
from datetime import datetime,timedelta
from jose import jwt,JWTError
from dotenv import load_dotenv

load_dotenv()

secret_key=os.getenv("secret_key","supersecretkey")
algorithm=os.getenv("alogorithm","HS256")
access_token_expire_time=int(os.getenv("access_token_expire_time","60"))

def create_access_token(date:dict,expire_time:int|None=None)->str:
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(time=(expire_time or access_token_expire_time))
    token=jwt.encode(to_encode,secret_key,ALGORITHM=algorithm)
    return token

def decode_access_token(token:str)->dict:
    try:
        payload=jwt.decode(token,secret_key,ALGORITHMS=[algorithm])
        return payload
    except JWTError:
        return{}
