from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader(
    r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\02_pdf_loader\LangChain_and_LangGraph_Comprehensive_Guide.pdf"
)


documents = loader.load()

print("Number of documents loaded:", len(documents))

for document in documents:

    print("\n-----------------------------")

    print("Page:", document.metadata.get("page"))

    print("Source:", document.metadata.get("source"))

    print("Content:")
    print(document.page_content[:200])

    '''  .get() is safer because it returns None if the key doesn't exist 
    instead of immediately raising a KeyError.'''