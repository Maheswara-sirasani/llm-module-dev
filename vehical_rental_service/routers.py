from fastapi import APIRouter, HTTPException, status, Depends
from pymongo.errors import DuplicateKeyError
from database import db
from user import UserCreate, UserLogin, UserOut, Token
from security import hash_password, verify_password, create_access_token
from auth import get_current_user
 
router = APIRouter(prefix="/auth", tags=["auth"])
 
def to_user_out(doc) -> UserOut:
    return UserOut(
        id=str(doc["_id"]),
        name=doc["name"],
        email=doc["email"],
        role=doc.get("role", "customer"),
    )
 
@router.post("/register", response_model=UserOut, status_code=201)
async def register(payload: UserCreate):
    doc = {
        "name": payload.name,
        "email": payload.email.lower(),
        "password": hash_password(payload.password),
        "role": payload.role or "customer",
    }
    try:
        res = await db.users.insert_one(doc)
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Email already registered")
 
    created = await db.users.find_one({"_id": res.inserted_id})
    return to_user_out(created)
 
@router.post("/login", response_model=Token)
async def login(payload: UserLogin):
    user = await db.users.find_one({"email": payload.email.lower()})
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
 
    token = create_access_token(sub=str(user["_id"]))
    return Token(access_token=token)
 
@router.get("/me", response_model=UserOut)
async def me(current_user=Depends(get_current_user)):
    return {
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"],
        "role": current_user.get("role", "customer"),
    }
 