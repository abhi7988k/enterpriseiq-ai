
from time import perf_counter

from langchain_core.runnables import RunnableLambda

from app.prompt import rag_prompt
from app.llm_service import llm


def format_doc(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(retriever):

    # Step 1: Retrieve relevant documents from Chroma
    def retrieve_context(inputs):

        start_time = perf_counter()

        docs = retriever.invoke(inputs["question"])

        retrieval_time = perf_counter() - start_time

        print(
            f"Chroma retrieval time: {retrieval_time:.2f} seconds",
            flush=True
        )

        print(f"Retrieved document chunks: {len(docs)}", flush=True)

        return {
            "context": format_doc(docs),
            "question": inputs["question"],
            "chat_history": inputs.get("chat_history", "")
        }

    # Step 2: Generate answer using Gemini
    def generate_answer(prompt_value):

        start_time = perf_counter()

        response = llm.invoke(prompt_value)

        generation_time = perf_counter() - start_time

        print(
            f"Gemini generation time: {generation_time:.2f} seconds",
            flush=True
        )

        return response

    # Step 3: Build RAG pipeline
    chain = (
        RunnableLambda(retrieve_context)
        | rag_prompt
        | RunnableLambda(generate_answer)
    )

    return chain
