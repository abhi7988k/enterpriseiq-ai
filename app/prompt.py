from langchain_core.prompts import ChatPromptTemplate

rag_prompt=ChatPromptTemplate.from_template("""
You are an AI assistant for EnterpriseIQ.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:

"""
)