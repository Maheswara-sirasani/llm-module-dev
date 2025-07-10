from fastapi import FastAPI
from routes import router as products_routes
 
app = FastAPI(title="Product List API")
app.include_router(products_routes)
 