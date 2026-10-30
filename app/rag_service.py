
from pathlib import Path

from app.document_loader import load_pdf
from app.text_splitter import split_document
from app.vector_store import create_vectore_store, get_vector_store
from app.rag_chain import create_rag_chain


# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "Data" / "EnterpriseAiData.pdf"
CHROMA_PATH = BASE_DIR / "chroma_db"


# Load the existing vector store or create a new one
if CHROMA_PATH.exists() and any(CHROMA_PATH.iterdir()):
    print("Loading existing Chroma database...")
    vector_store = get_vector_store()

else:
    print("Creating a new Chroma database...")

    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"PDF file not found: {PDF_PATH}"
        )

    documents = load_pdf(str(PDF_PATH))
    print("PDF pages loaded:", len(documents))

    chunks = split_document(documents)
    print("Text chunks created:", len(chunks))

    vector_store = create_vectore_store(chunks)


# Debugging information
print("\n--- RAG Debug Information ---")
print("PDF exists:", PDF_PATH.exists())
print("PDF path:", PDF_PATH)
print("Chroma document count:", vector_store._collection.count())


# Test document retrieval
test_question = "main components of an enterprise AI system"

test_docs = vector_store.similarity_search(
    test_question,
    k=3
)

print("\n--- Retrieved Document Chunks ---")

if test_docs:
    for i, doc in enumerate(test_docs, start=1):
        print(f"\nChunk {i}:")
        print(doc.page_content[:800])
else:
    print("No relevant document chunks were retrieved.")


# Configure retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# Create RAG chain
rag_chain = create_rag_chain(retriever)


# Generate response
def generate_rag_response(question: str) -> str:
    response = rag_chain.invoke(question)

    if isinstance(response, str):
        return response

    if hasattr(response, "content"):
        return response.content

    return str(response)
