
import socket

# Prefer IPv4 for Gemini API connections
_original_getaddrinfo = socket.getaddrinfo

def prefer_ipv4_for_gemini(host, port, family=0, *args, **kwargs):
    if host == "generativelanguage.googleapis.com":
        family = socket.AF_INET

    return _original_getaddrinfo(
        host, port, family, *args, **kwargs
    )

socket.getaddrinfo = prefer_ipv4_for_gemini


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.rag_service import generate_rag_response

app = FastAPI(
    title="Enterprise Ai Service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "https://enterpriseiq-ai.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    prompt: str
    session_id: str


conversation_history = {}


@app.get("/api/ai/health")
def health():
    return {"status": "Ai Service is Running"}


@app.post("/api/ai/chat")
def chat(request: ChatRequest):
    session_id = request.session_id
    history = conversation_history.get(session_id, [])

    chat_history = ""

    for message in history:
        chat_history += (
            f"User: {message['question']}\n"
            f"Assistant: {message['answer']}\n"
        )

    answer = generate_rag_response(
        request.prompt,
        chat_history
    )

    history.append({
        "question": request.prompt,
        "answer": answer
    })

    conversation_history[session_id] = history

    return {
        "answer": answer,
        "session_id": session_id
    }
