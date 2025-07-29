from fastapi import FastAPI
from routers import auth_router
 
app = FastAPI(title="User Management API Without JWT")
 
app.include_router(auth_router)
 