from fastapi import FastAPI
from database import db
from routers import router as auth_router

app=FastAPI(
    title="vehical rental service",
    version="0.3"
)
@app.on_event("startup")
async def startup():
    await db.users.create_index("email",unique=True)

@app.get("/health")
async def health():
    return{"status":"ok",
           "service":"rental",
           "version":"0.11"
    }
    

app.include_router(auth_router)