from fastapi import APIRouter, HTTPException, status, Depends
from schemas import UserCreate, UserOut, Token
from models import user_collection
from utils import hash_password, verify_password, create_access_token
from auth import get_current_user
 
router = APIRouter()
 
@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = {
        "email": user.email,
        "password_hash": hash_password(user.password),
        "subscription_type": "free",
        "scans_used": 0
    }
    user_collection.insert_one(new_user)
    return {k: new_user[k] for k in ("email", "subscription_type", "scans_used")}
 
@router.post("/login", response_model=Token)
def login(user: UserCreate):
    db_user = user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
 
@router.get("/me", response_model=UserOut)
def read_me(current_user=Depends(get_current_user)):
    return {
        "email": current_user["email"],
        "subscription_type": current_user["subscription_type"],
        "scans_used": current_user["scans_used"]
    }
 
@router.post("/upgrade")
def upgrade_plan(current_user=Depends(get_current_user)):
    user_collection.update_one({"email": current_user["email"]}, {"$set": {"subscription_type": "premium"}})
    return {"message": "Upgraded to premium"}
 