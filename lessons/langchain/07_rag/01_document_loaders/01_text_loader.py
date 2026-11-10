''' 
A Document Loader converts external data into LangChain Document objects.

Document:
The information loaded from your source.

Document
├── page_content
└── metadata

E.g.

Document(
    page_content="LangChain is a framework...",
    metadata={"source": "example.txt"}
)

'''
from langchain_community.document_loaders import TextLoader

# create a Loader
loader=TextLoader(
  "E:/GenAI/Langchain-Learning/lessons/langchain/07_rag/01_document_loaders/sample.txt"
 )

# '''  OR
# loader = TextLoader(
#     r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\01_document_loaders\sample.txt"
# )
# '''
# Load the document

documents=loader.load()

print("Number of documents:")
print(len(documents))

print(f"Complete Documents:{documents}")
print(f"Type of Documents: {type(documents)} ")

print("\nDocument:")
print(documents[0])

print("\nFirst Document Type:")
print(type(documents[0]))

print("\nPage Content:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)

