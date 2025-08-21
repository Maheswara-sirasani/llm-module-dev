from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from bson import ObjectId
from database import db
from hash import hash_password, verify_password
from utilis import create_access_token, decode_access_token
from user import UserCreate, UserOut, Token
 
router = APIRouter(prefix="/auth", tags=["auth"])
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
 
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
 
    hashed = hash_password(user.password)
    doc = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed,
        "role": user.role
    }
    res = await db.users.insert_one(doc)
    created = await db.users.find_one({"_id": res.inserted_id})
    return UserOut(
        id=str(created["_id"]),
        name=created["name"],
        email=created["email"],
        role=created["role"]
    )
 
@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_doc = await db.users.find_one({"email": form_data.username})
    if not user_doc:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
 
    if not verify_password(form_data.password, user_doc["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
 
    token_data = {
        "sub": str(user_doc["_id"]),
        "email": user_doc["email"],
        "role": user_doc.get("role", "customer")
    }
 
    access_token = create_access_token(token_data)
    return Token(access_token=access_token, token_type="bearer")
 
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
 
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
 
    user_doc = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
 
    user_doc["id"] = str(user_doc["_id"])
    return user_doc
 
async def require_admin(current_user=Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user
 