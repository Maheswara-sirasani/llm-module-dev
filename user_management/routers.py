from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timedelta
from database import users_collection, password_resets
from schemas import RegisterRequest, LoginRequest, ChangePasswordRequest, ForgotPasswordRequest, TokenResponse
from auth_utils import hash_password, verify_password, create_access_token
from dependencies import get_current_user
from logger import logger
import uuid
 
auth_router = APIRouter()
 
# ---------------- Register ----------------
@auth_router.post("/register")
def register_user(user: RegisterRequest):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_pw = hash_password(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_pw
    user_dict["created_at"] = datetime.utcnow()
    user_dict["password_changed_at"] = datetime.utcnow()
    users_collection.insert_one(user_dict)
    
    logger.info(f"Registered user: {user.username}")
    return {"message": "User registered successfully"}
 
# ---------------- Login ----------------
@auth_router.post("/login", response_model=TokenResponse)
def login_user(user: LoginRequest):
    db_user = users_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    pwd_age = (datetime.utcnow() - db_user["password_changed_at"]).days
    if pwd_age >= 30:
        raise HTTPException(status_code=403, detail="Password expired, please change your password")
    
    token = create_access_token({"sub": user.username})
    logger.info(f"User logged in: {user.username}")
    return {"access_token": token, "token_type": "bearer"}
 
# ---------------- Change Password ----------------
@auth_router.post("/change-password")
def change_password(req: ChangePasswordRequest, username: str = Depends(get_current_user)):
    db_user = users_collection.find_one({"username": username})
    if not db_user or not verify_password(req.old_password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if verify_password(req.new_password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Cannot reuse old password")
    
    new_hashed = hash_password(req.new_password)
    users_collection.update_one(
        {"username": username},
        {"$set": {"password": new_hashed, "password_changed_at": datetime.utcnow()}}
    )
    logger.info(f"Password changed for {username}")
    return {"message": "Password changed successfully"}
 
# ---------------- Forgot Password ----------------
@auth_router.post("/forgot-password")
def forgot_password(req: ForgotPasswordRequest):
    db_user = users_collection.find_one({"username": req.email})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
 
    reset_count = password_resets.count_documents({
        "email": req.email,
        "created_at": {"$gte": datetime.utcnow() - timedelta(hours=24)}
    })
    if reset_count >= 3:
        raise HTTPException(status_code=429, detail="Max reset attempts reached, try later")
 
    reset_token = str(uuid.uuid4())
    password_resets.insert_one({
        "email": req.email,
        "token": reset_token,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(hours=24)
    })
 
    logger.info(f"Password reset link generated for {req.email}")
    return {"message": "Password reset link sent to your email", "reset_token": reset_token}

 