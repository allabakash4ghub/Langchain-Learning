from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the PDF file
loader =PyPDFLoader(r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\02_pdf_loader\LangChain_and_LangGraph_Comprehensive_Guide.pdf")
#loader =PyPDFLoader(r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\02_pdf_loader\COT_2201.11903v6.pdf")
documents = loader.load()
print("Type of documents:", type(documents))

print("Number of Pages or Documents Loaded:", len(documents))
#print(documents)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

# Split the docuements into chunks
chunks = splitter.split_documents(documents)
print("Number of chunks created:", len(chunks))
print("Type of chunks:", type(chunks))

# insert few chunks

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i+1} ---")
    print(f"Page Contents:",chunk.page_content[:100])  # Print the first 100 characters of each chunk"
    print(f"page Metadata:", chunk.metadata)  # Print the metadata of each chunk