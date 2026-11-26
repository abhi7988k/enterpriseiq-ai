import os
import psutil

from collections import OrderedDict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.rag_service import generate_rag_response


app = FastAPI(
    title="EnterpriseIQ AI Service",
    version="2.0.0",
    description="AI service for EnterpriseIQ"
)

# Allow requests from the frontend
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
    prompt: str = Field(..., min_length=1)
    session_id: str = Field(..., min_length=1)


# Store recent conversations for each session
MAX_HISTORY_PER_SESSION = 5
MAX_SESSIONS = 100

conversation_history = OrderedDict()


@app.get("/api/ai/health")
def health():
    return {
        "status": "AI Service is Running",
        "llm": "Ollama",
        "model": os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
    }


@app.get("/api/ai/memory")
def memory_usage():
    process = psutil.Process(os.getpid())
    memory = process.memory_info()

    return {
        "ram_mb": round(memory.rss / (1024 * 1024), 2),
        "vms_mb": round(memory.vms / (1024 * 1024), 2)
    }


@app.post("/api/ai/chat")
def chat(request: ChatRequest):
    session_id = request.session_id

    history = conversation_history.get(session_id, [])

    chat_history = ""

    # Add previous messages to the context
    for message in history:
        chat_history += (
            f"User: {message['question']}\n"
            f"Assistant: {message['answer']}\n"
        )

    try:
        answer = generate_rag_response(
            request.prompt,
            chat_history
        )

        history.append({
            "question": request.prompt,
            "answer": answer
        })

        # Keep only the latest five conversations
        history = history[-MAX_HISTORY_PER_SESSION:]

        conversation_history[session_id] = history
        conversation_history.move_to_end(session_id)

        # Remove older sessions when the limit is reached
        while len(conversation_history) > MAX_SESSIONS:
            conversation_history.popitem(last=False)

        return {
            "answer": answer,
            "session_id": session_id
        }

    except Exception as e:
        print(f"Chat error: {str(e)}", flush=True)

        raise HTTPException(
            status_code=500,
            detail="Failed to generate AI response."
        )