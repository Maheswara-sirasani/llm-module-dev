from fastapi import Depends,HTTPException,status
from security import OAuth2passwordBearer
from bson import ObjectId
from jose import JWTError
from database import db
from security import decode_token

oauth2_scheme=OAuth2passwordBearer(tokenUrl="/auth/login")


async def get_current_user(token:str=Depends(oauth2_scheme)):
    creds_exc=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not valid credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload=decode_token(token)
        user_id=payload.get("sub")
        if not user_id:
            raise creds_exc
    except JWTError:
        raise creds_exc
    
    user=await db.user.find_one({"id":ObjectId(user_id)})
    if not user:
        raise creds_exc
    
    user["id"]=str(user["_id"])
    user.pop("password",None)
    return user