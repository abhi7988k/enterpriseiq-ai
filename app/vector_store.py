
import os
from pathlib import Path

from langchain_chroma import Chroma
from app.embedding_service import embeddings

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Persistent Chroma database location
CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    str(BASE_DIR / "chroma_db")
)


def create_vectore_store(chunks):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name="enterpriseiq"
    )

    return vector_store


def get_vector_store():
    vector_store = Chroma(
        persist_directory=CHROMA_PATH,
        collection_name="enterpriseiq",
        embedding_function=embeddings
    )

    return vector_store


def search_documents(question, vector_store):
    return vector_store.similarity_search(question, k=3)
