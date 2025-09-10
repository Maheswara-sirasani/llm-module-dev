from datetime import datetime, timedelta,timezone
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
 
def calculate_refund(start_date, amount: float) -> float:
    """
    Calculate refund based on how far in the future the booking start date is.
    - start_date can be:
        - a string in "YYYY-MM-DD" format
        - an ISO datetime string (e.g. "2025-09-10T15:00:00")
        - a datetime object (aware or naive)
    - amount is the total booking amount (float)
    Returns a float rounded to 2 decimals.
    Rules (example):
      >= 24 hours before start  -> full refund
      0 .. <24 hours before     -> 50% refund
      after start               -> 0 refund
    """
    # normalize start to naive UTC datetime
    if isinstance(start_date, str):
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
        except Exception:
            # fallback to iso format
            start = datetime.fromisoformat(start_date)
    elif isinstance(start_date, datetime):
        start = start_date
    else:
        raise ValueError("start_date must be str or datetime")
 
    # if the start has tzinfo, convert to UTC and drop tzinfo
    if getattr(start, "tzinfo", None) is not None:
        start = start.astimezone(timezone.utc).replace(tzinfo=None)
 
    now = datetime.utcnow()  # naive UTC
    diff_seconds = (start - now).total_seconds()
    hours = diff_seconds / 3600.0
 
    if hours >= 24:
        refund = float(amount)
    elif hours >= 0:
        refund = float(amount) * 0.5
    else:
        refund = 0.0
 
    return round(refund, 2)
  