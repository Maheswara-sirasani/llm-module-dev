
FastAPI
 
## Introduction
 
FastAPI is a high-performance Python web framework for building APIs. 
It uses Pydantic for data validation and is built on Starlette for async support.
 
Key Features:
 
 Asynchronous and blazing fast
 
 Type-checked with Pydantic
 
 Auto-generated OpenAPI docs
 
 Intuitive dependency injection
 
 Built-in support for OAuth2/JWT
 
 
##  Installation & Setup
 
pip install fastapi uvicorn
 
 
## Your First FastAPI App
```python 
main.py
 
from fastapi import FastAPI
 
router = FastAPI()
 
@router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
 
Run it:
 
uvicorn main:app --reload
```
 
Visit: http://localhost:8000
 
 
## Path Parameters & Query Params
```python 
@router.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```    
 
item_id is a path param
 
q is a query param
 
 
## Request Body & Data Validation
```python 
from pydantic import BaseModel
 
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
 
@router.post("/items/")
def create_item(item: Item):
    return item
```    

 FastAPI will validate input automatically.
 

## Response Models
```python 
from typing import Optional
 
class ItemResponse(BaseModel):
    name: str
    price: float
    tax: Optional[float] = None
 
@router.get("/item/", response_model=ItemResponse)
def read_item():
    return {"name": "Phone", "price": 999.99, "tax": 50}
```    
 
 
## Asynchronous Programming
 
```python
import
``` asyncio
 
@router.get("/async-example")
async def async_hello():
    await asyncio.sleep(1)
    return {"message": "Hello after 1 second"}
```    
 
 
## Dependency Injection
```python 
from fastapi import Depends
 
def get_token():
    return "secure-token"
 
@arouter.get("/protected")
def protected(token: str = Depends(get_token)):
    return {"token": token}
```    
 
 
## Handling Forms & Files
```python 
from fastapi import Form, File, UploadFile
 
@router.post("/submit/")
def submit_form(name: str = Form(...), file: UploadFile = File(...)):
    return {"name": name, "filename": file.filename}
```    

 
## CRUD with Databases (SQLAlchemy)
 
Install:
 
pip install sqlalchemy
```python 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
```    
 
Use SessionLocal and FastAPI Depends to manage sessions.

 
##  Authentication (JWT, OAuth2)
 
Install:
 
pip install python-jose[cryptography] passlib[bcrypt]
 
Supports:
 
OAuth2 password flow
 
JWT access tokens
 
Reusable get_current_user dependency
 
 
## Background Tasks
```python 
from fastapi import BackgroundTasks
 
def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")
 
@rouer.post("/log/")
def log_event(background_tasks: BackgroundTasks, msg: str):
    background_tasks.add_task(write_log, msg)
    return {"message": "Logging started"}
```    

 
## Middlewares & Events
```python 
@router.middleware("http")
async def log_requests(request, call_next):
    print("New request:", request.url)
    response = await call_next(request)
    return response
 
@outer.on_event("startup")
def on_start():
    print("App starting...")
 
@router.on_event("shutdown")
def on_shutdown():
    print("App shutting down...")
``` 
 
## Documentation (Swagger & Redoc)
 
Auto-generated at:
 
http://localhost:8000/docs (Swagger UI)
 
http://localhost:8000/redoc (ReDoc)
 
 
You can customize metadata:
 
router = FastAPI(title="My API", description="Docs!", version="1.0.0")
 
 
## Testing APIs
 
pip install httpx pytest
```python 
test_main.py
 
from fastapi.testclient import TestClient
from main import app
 
client = TestClient(app)
 
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
``` 
 
Deployment (Uvicorn, Docker, etc.)
 
Run in production:
 
uvicorn main:app --host 0.0.0.0 --port 80
 
Dockerfile
 
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
 
 
## Best Practices
 
Use response_model for consistent output
 
Add type hints everywhere
 
Organize with routers and modules
 
Keep configuration in .env
 
Handle exceptions with custom handlers