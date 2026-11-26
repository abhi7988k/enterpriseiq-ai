
import os
from pathlib import Path

from langchain_chroma import Chroma
from app.embedding_service import embeddings

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    str(BASE_DIR / "chroma_db")
)

COLLECTION_NAME = "enterpriseiq"

print("VECTOR STORE CHROMA PATH:", CHROMA_PATH)


def create_vectore_store(chunks):
    path = Path(CHROMA_PATH)
    path.mkdir(parents=True, exist_ok=True)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(path),
        collection_name=COLLECTION_NAME
    )

    print("Chroma vector store created successfully.")
    return vector_store


def get_vector_store():
    return Chroma(
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )


def search_documents(question, vector_store):
    return vector_store.similarity_search(
        question,
        k=3
    )
