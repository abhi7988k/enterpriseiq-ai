from document_loader import load_pdf
from text_splitter import split_document
from vector_store import create_vectore_store
from rag_chain import create_rag_chain


def test():
    # 1. Load PDF
    documents = load_pdf("Data/enterpriseiq_rag_test_document.pdf")
    print("Documents:", len(documents))

    # 2. Split into chunks
    chunks = split_document(documents)
    print("Chunks:", len(chunks))

    # 3. Create vector store
    vector_store = create_vectore_store(chunks)
    print("Vector store created successfully")

    # 4. Create retriever
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    # 5. Create RAG chain
    rag_chain = create_rag_chain(retriever)

    # 6. Ask question
    question = "What authentication mechanism does EnterpriseIQ use?"

    response = rag_chain.invoke(question)

    # 7. Print answer
    print("\nANSWER:")
    print(response.content)


test()