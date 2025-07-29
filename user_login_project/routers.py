from fastapi import APIRouter, HTTPException
from schemas import RegisterRequest, LoginRequest, ChangePasswordRequest, ForgotPasswordRequest, TokenResponse
from database import users_db, sessions_db, password_reset_requests
from logger import logger
from datetime import datetime, timedelta
import uuid
 
auth_router = APIRouter()
 
# 1. Register
@auth_router.post("/register")
def register_user(user: RegisterRequest):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
 
    users_db[user.username] = {
        "username": user.username,
        "password": user.password,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "dob": str(user.dob),
        "doj": str(user.doj),
        "address": user.address,
        "comment": user.comment,
        "active": user.active,
        "password_last_changed": datetime.now()
    }
    logger.info(f"User {user.username} registered successfully")
    return {"message": "User registered successfully"}
 
# 2. Login
@auth_router.post("/login", response_model=TokenResponse)
def login_user(login: LoginRequest):
    user = users_db.get(login.username)
    if not user or user["password"] != login.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = str(uuid.uuid4())  # Dummy token
    sessions_db[token] = login.username
    logger.info(f"User {login.username} logged in")
    return TokenResponse(access_token=token)
 
# 3. Change Password
@auth_router.post("/change-password")
def change_password(data: ChangePasswordRequest, token: str):
    username = sessions_db.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="Not logged in")
    
    user = users_db[username]
    if user["password"] != data.old_password:
        raise HTTPException(status_code=400, detail="Old password is incorrect")
    
    user["password"] = data.new_password
    user["password_last_changed"] = datetime.now()
    logger.info(f"User {username} changed password")
    return {"message": "Password changed successfully"}
 
# 4. Forgot Password
@auth_router.post("/forgot-password")
def forgot_password(req: ForgotPasswordRequest):
    reset_id = str(uuid.uuid4())
    password_reset_requests[req.email] = {
        "reset_id": reset_id,
        "expires": datetime.now() + timedelta(hours=24)
    }
    logger.info(f"Password reset link generated for {req.email}")
    return {"message": "Password reset link generated (mocked)"}
 
# 5. Logout
@auth_router.post("/logout")
def logout(token: str):
    if token in sessions_db:
        username = sessions_db.pop(token)
        logger.info(f"User {username} logged out")
        return {"message": "Logged out successfully"}
    raise HTTPException(status_code=401, detail="Invalid token")
# 6. get all users
@auth_router.get("/users")
def get_all_users():
    return list(users_db.keys())
# 7. get user by username
@auth_router.get("/users/{username}")       
def get_user_by_username(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
# 8. delete user by username
@auth_router.delete("/users/{username}")    
def delete_user_by_username(username: str):
    if username in users_db:
        del users_db[username]
        logger.info(f"User {username} deleted")
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
# 9. update user by username
@auth_router.put("/users/{username}")
def update_user_by_username(username: str, user: RegisterRequest):  
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[username].update({
        "first_name": user.first_name,
        "last_name": user.last_name,
        "dob": str(user.dob),
        "doj": str(user.doj),
        "address": user.address,
        "comment": user.comment,
        "active": user.active,
        "password": user.password
    })
    logger.info(f"User {username} updated successfully")
    return {"message": "User updated successfully"}


 