from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_document(documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    chunk=text_splitter.split_documents(documents)
    
    return chunk