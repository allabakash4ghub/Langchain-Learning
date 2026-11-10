'''  We need to install pypdf for PDF operations
pypdf is responsible for:
Opening the PDF
Reading PDF structure
Extracting text from PDF pages

PyPDFLoader is LangChain's integration/wrapper around PDF parsing functionality.

PyPDFLoader is responsible for:
Integrating PDF loading into LangChain
Creating LangChain Document objects
Attaching metadata such as source/page
Providing the LangChain loader interface

LangChain Loader        Underlying Library
------------------------------------------------
PyPDFLoader             pypdf
Docx loaders            python-docx
Excel loaders           openpyxl
Some web loaders        requests / BeautifulSoup

'''
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(
    r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\02_pdf_loader\LangChain_and_LangGraph_Comprehensive_Guide.pdf"
)

# Load Pdf
documents=loader.load()

# Number of documents/pages
print(f"Number of Documents: {len(documents)}")
print(f"Type of Documents:{type(documents)}")
#print(documents)
for i, document in enumerate(documents):

    print(f"\n--- Document {i + 1} ---")

    print("Page Content:")
    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)

print(f"\nTest the sample data :{documents[0].page_content[:100]}")    


''' 
Very important: metadata is NOT normally embedded
Usually, the page content is what gets converted into the embedding:
Metadata is generally maintained separately as associated information.

'''