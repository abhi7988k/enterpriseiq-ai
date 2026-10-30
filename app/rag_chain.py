from app.prompt import rag_prompt
from app.llm_service import llm
 



def format_doc(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def create_rag_chain(retriever):
    chain = (
        {
            "context":retriever | format_doc,
            "question":lambda x:x
            
        }
        |
        rag_prompt
        |
        llm
    )
    
    return chain