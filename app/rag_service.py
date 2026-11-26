
from pathlib import Path

from app.document_loader import load_pdf
from app.text_splitter import split_document
from app.vector_store import (
    create_vectore_store,
    get_vector_store,
    CHROMA_PATH
)

CHROMA_PATH = Path(CHROMA_PATH)

from app.rag_chain import create_rag_chain


# PDF path
BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "Data" / "EnterpriseAiData.pdf"


if not PDF_PATH.exists():
    raise FileNotFoundError(
        f"PDF file not found: {PDF_PATH}"
    )


# Load existing ChromaDB or create a new one
if CHROMA_PATH.exists() and any(CHROMA_PATH.iterdir()):

    print("Loading existing Chroma database...")

    vector_store = get_vector_store()

    document_count = vector_store._collection.count()

    print("Existing Chroma document count:", document_count)

    if document_count == 0:

        print("Chroma database is empty. Rebuilding from PDF...")

        documents = load_pdf(str(PDF_PATH))

        print("PDF pages loaded:", len(documents))

        chunks = split_document(documents)

        print("Text chunks created:", len(chunks))

        if not chunks:
            raise ValueError(
                "No text chunks were extracted from the PDF."
            )

        vector_store = create_vectore_store(chunks)

else:

    print("Creating a new Chroma database...")

    documents = load_pdf(str(PDF_PATH))

    print("PDF pages loaded:", len(documents))

    chunks = split_document(documents)

    print("Text chunks created:", len(chunks))

    if not chunks:
        raise ValueError(
            "No text chunks were extracted from the PDF."
        )

    vector_store = create_vectore_store(chunks)


# RAG Debug Information
print("\n--- RAG Debug Information ---")

print("PDF exists:", PDF_PATH.exists())
print("PDF path:", PDF_PATH)
print("Chroma path:", CHROMA_PATH)

document_count = vector_store._collection.count()

print("Chroma document count:", document_count)


# Configure retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


# Create RAG chain
rag_chain = create_rag_chain(retriever)


# Generate RAG response
import time


def generate_rag_response(
    question: str,
    chat_history: str = ""
) -> str:

    start_time = time.perf_counter()

    response = rag_chain.invoke({
        "question": question,
        "chat_history": chat_history
    })

    total_time = time.perf_counter() - start_time

    print(
        f"AI response generation time: {total_time:.2f} seconds"
    )

    if isinstance(response, str):
        return response

    if hasattr(response, "content"):
        return response.content

    return str(response)
