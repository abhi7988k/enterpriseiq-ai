
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.rag_service import generate_rag_response

app = FastAPI(
    title="Enterprise Ai Service",
    version="1.0.0"
)

# Allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
         "https://enterpriseiq-ai.vercel.app"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/api/ai/health")
def health():
    return {
        "status": "Ai Service is Running"
    }

@app.post("/api/ai/chat")
def chat(request: ChatRequest):
    answer = generate_rag_response(request.prompt)

    return {
        "answer": answer
    }
