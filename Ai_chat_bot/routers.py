 
from fastapi import APIRouter
from pydantic import BaseModel
import requests
 
router = APIRouter()
 
class ChatRequest(BaseModel):
    message: str
 
@router.get("/")
def root():
    return {"message": "Welcome to the Chatbot API!"}
 
@router.post("/chat")
def chat_with_bot(chat: ChatRequest):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": chat.message, "stream": False}
        )
        if response.status_code == 200:
            data = response.json()
            return {"response": data["response"].strip()}
        else:
            return {"error": "Failed to get response from the model"}
    except Exception as e:
        return {"error": str(e)}
  