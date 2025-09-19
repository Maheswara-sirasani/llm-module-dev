from fastapi import FastAPI
from routers import auth_routes
 
app = FastAPI(title="User Management API")
 
# Include Auth Router
app.include_router(auth_routes.auth_router, prefix="/auth", tags=["Authentication"])
 
@app.get("/")
def root():
    return {"message": "User Management API is running"}
 