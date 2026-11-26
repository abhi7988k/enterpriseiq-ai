
from time import perf_counter

from langchain_core.runnables import RunnableLambda

from app.prompt import rag_prompt
from app.llm_service import llm

def format_doc(docs):
    return "\n\n".join(
        doc.page_content[:2500] for doc in docs
    )

def create_rag_chain(retriever):

    def retrieve_context(inputs):

        start_time = perf_counter()

        docs = retriever.invoke(inputs["question"])

        retrieval_time = perf_counter() - start_time

        print(
            f"\nChroma retrieval time: {retrieval_time:.2f} seconds",
            flush=True
        )

        print(f"Retrieved chunks: {len(docs)}", flush=True)

        # Check what Chroma actually retrieved.
        for i, doc in enumerate(docs, 1):
            print(f"\n--- Retrieved Chunk {i} ---", flush=True)
            print(doc.page_content[:1000], flush=True)
            print("Metadata:", doc.metadata, flush=True)

        context = format_doc(docs)

        print(f"\nTotal context length: {len(context)} characters", flush=True)

        return {
            "context": context,
            "question": inputs["question"],
            "chat_history": inputs.get("chat_history", "")
        }

    def generate_answer(prompt_value):

        start_time = perf_counter()

        response = llm.invoke(prompt_value)

        generation_time = perf_counter() - start_time

        print(
            f"Ollama generation time: {generation_time:.2f} seconds",
            flush=True
        )

        return response

    return (
        RunnableLambda(retrieve_context)
        | rag_prompt
        | RunnableLambda(generate_answer)
    )