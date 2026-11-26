
from langchain_ollama import ChatOllama

# Initialize local Ollama LLM once and reuse it
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.3,
)


