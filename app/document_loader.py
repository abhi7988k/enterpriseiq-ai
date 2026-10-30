from langchain_community.document_loaders import PyPDFium2Loader


def load_pdf(file_path:str):
    loader=PyPDFium2Loader(file_path)
    documents=loader.load()
    print(len(documents))
    
    return documents

 

    