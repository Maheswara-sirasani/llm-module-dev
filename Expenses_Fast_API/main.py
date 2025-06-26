from fastapi import FastAPI
from routes import router as expense_routes
 
app = FastAPI()
 
# Include all routes from the routes module
app.include_router(expense_routes)