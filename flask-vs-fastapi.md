
# Flask vs FastAPI — A Complete Learning Guide with MongoDB CRUD and Async Concepts

## Overview

In this guide, you will learn the core differences between **Flask** and **FastAPI** through structured learning content. This article combines conceptual explanations, code examples, and practical insights focused on Python web API development using **MongoDB Cloud**.

This guide follows a progressive flow:
- Understanding the basics of Flask and FastAPI
- Deep dive into architecture (WSGI vs ASGI)
- Sync vs Async explained with real examples
- CRUD API examples using MongoDB
- Data validation using Pydantic (FastAPI)
- Performance insights and when to choose each framework
- Interview preparation with Knowledge Check section

By the end, you will have a hands-on understanding of when and how to use Flask or FastAPI effectively.

---

## Section 1: Flask Basics — WSGI and Synchronous APIs

### What is Flask?
Flask is a **micro web framework** based on **WSGI (Web Server Gateway Interface)**. It provides simplicity and flexibility to create RESTful APIs without enforcing any directory structures or specific patterns.

**WSGI** runs in synchronous blocking mode, meaning each HTTP request is handled one at a time.

### Example Flask Endpoint

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return {'message': 'Hello from Flask (Sync)'}
```

**Key Points:**
- Suitable for simple APIs
- Easy to set up and extend with Flask extensions
- Not built for high concurrency

---

## Section 2: FastAPI Basics — ASGI and Asynchronous APIs

### What is FastAPI?
FastAPI is a **modern web framework** based on **ASGI (Asynchronous Server Gateway Interface)** with native support for async/await syntax and automatic OpenAPI documentation.

**ASGI** enables asynchronous non-blocking I/O, suitable for high-performance APIs.

### Example FastAPI Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return {"message": "Hello from FastAPI (Async)"}
```

**Key Points:**
- Built-in async support
- Auto-generates OpenAPI docs
- High-performance for concurrent workloads

---

## Section 3: Sync vs Async Explained

### Synchronous (Flask):
- Blocking request handling
- Simpler but inefficient under heavy concurrent requests

### Asynchronous (FastAPI):
- Non-blocking request handling using **async/await**
- Efficient with high concurrency (e.g., database calls, external APIs)

**Async Advantage Example:**
```python
@app.get("/async-task")
async def async_task():
    await some_async_operation()
    return {"status": "done"}
```

---

## Section 4: MongoDB Cloud Setup with Atlas

- Visit [https://cloud.mongodb.com](https://cloud.mongodb.com)
- Create a free cluster, database `bookstore`, collection `books`
- Whitelist your IP and get connection URI
- Store the connection string securely in `.env` file

```dotenv
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/bookstore?retryWrites=true&w=majority
```

---

## Section 5: Flask CRUD API with MongoDB (Sync)

### Highlights:
- Synchronous CRUD using Flask-PyMongo
- Suitable for basic CRUD services

```python
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "your_mongo_uri_here"
mongo = PyMongo(app)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    mongo.db.books.insert_one(data)
    return jsonify({"msg": "Book added"}), 201
```

Run Flask API:
```bash
python flask_app.py
```

---

## Section 6: FastAPI CRUD API with MongoDB (Async + Pydantic)

### Highlights:
- Asynchronous CRUD with FastAPI and Motor
- Input validation using Pydantic models
- Auto-generated Swagger documentation

```python
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

app = FastAPI()
client = AsyncIOMotorClient("your_mongo_uri_here")
db = client.bookstore

class Book(BaseModel):
    title: str
    author: str

@app.post("/books")
async def create_book(book: Book):
    await db.books.insert_one(book.dict())
    return {"message": "Book added"}
```

Run FastAPI API:
```bash
uvicorn fastapi_app:app --reload
```

---

## Section 7: Data Validation with Pydantic (FastAPI)

Pydantic enforces strict data validation using Python type hints.

```python
class Book(BaseModel):
    title: str
    author: str
```

**Benefits of Pydantic:**
- Eliminates manual data parsing
- Improves reliability and reduces code errors

---

## Section 8: Automatic API Documentation

FastAPI provides OpenAPI docs automatically:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

In Flask, similar documentation requires Flask-Swagger or Flask-RESTful extensions.

---

## Section 9: Performance Benchmarks (Summary)

| Category | Flask (Sync) | FastAPI (Async) |
|-----------|----------------|-----------------|
| Requests/sec | Lower | Higher |
| Concurrent Requests | Blocking | Non-blocking |
| Data Validation | Manual | Pydantic |
| API Documentation | Manual setup | Automatic |
| Scalability | Limited | High |

---

## Section 10: Choosing Between Flask and FastAPI

| Choose Flask When | Choose FastAPI When |
|---------------------|----------------------|
| Simplicity required | High concurrency required |
| Small APIs or PoC | Production-grade APIs |
| No async dependency | Async architecture is needed |

---

## Section 11: Knowledge Check — Interview Questions

1. Explain WSGI vs ASGI with examples.
2. How does async/await work in FastAPI?
3. How does Pydantic simplify validation?
4. Why is FastAPI better for high concurrency workloads?
5. How can you connect Flask to MongoDB Cloud?
6. Describe how FastAPI handles OpenAPI generation.
7. What is blocking vs non-blocking in API frameworks?
8. What is the purpose of `.env` files in Python projects?
9. Explain a basic CRUD operation using Flask.
10. Explain a basic CRUD operation using FastAPI and Motor.
11. Why is type hinting essential in FastAPI?
12. How does Uvicorn serve FastAPI applications?
13. Why are Flask APIs considered synchronous?
14. Explain advantages of FastAPI in modern microservices.
15. What are the drawbacks of Flask in high-load applications?
16. Which framework offers better developer productivity and why?
17. Describe the role of Motor in FastAPI.
18. When should you avoid FastAPI despite its features?
19. How do you generate API schema in Flask vs FastAPI?
20. How does FastAPI handle background tasks compared to Flask?

---

This guide equips you with both theoretical knowledge and hands-on code experience to confidently use Flask or FastAPI with modern cloud databases like MongoDB Atlas.