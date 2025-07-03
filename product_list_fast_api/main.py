from fastapi import FastAPI
from routes import router as products_routes

app=FastAPI(tittle="Product List API ")

app.include_router(products_routes)
