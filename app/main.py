from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_service import generate_rag_response

app=FastAPI(
    title="Enterprise Ai Service",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    prompt:str

@app.get("/api/ai/health")
def health():
    return{
        "status":"Ai Service is Running"
    }
    

@app.post("/api/ai/chat")
def chat(request: ChatRequest):
    answer = generate_rag_response(request.prompt)
    
    return{
        "answer" :answer
    }