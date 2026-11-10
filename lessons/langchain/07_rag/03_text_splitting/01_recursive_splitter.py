
'''
| Method               | Input             | Output           |
| -------------------- | ----------------- | ---------------- |
| `split_text()`       | String            | `list[str]`      |
| `create_documents()` | List of strings   | `list[Document]` |
| `split_documents()`  | List of Documents | `list[Document]` |

'''

from langchain_text_splitters import RecursiveCharacterTextSplitter

input_text = """
LangChain is a framework for developing applications
powered by language models.

LangChain provides components for prompts, models,
output parsers, document loaders, retrievers, and agents.

Retrieval-Augmented Generation, commonly called RAG,
allows an application to retrieve relevant information
from external data before generating an answer.
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap= 25
)

chunks = splitter.split_text(text=input_text)
print("Number of Chunks Created:", len(chunks))
print(f"Chunks: {chunks}")
print(f"Type of Chunks: {type(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")

    print(chunk)

 ###### Other method of splitting text into chunks is by using the `split_documents()` method.
 # This method takes a list of Document objects as input and returns a list of Document objects as output. Each Document object contains a chunk of text along with its metadata.   

print("\n\n--- Splitting Text into Documents ---")
chunks2 = splitter.create_documents(texts=[input_text])
print("Number of Documents Created:", len(chunks2))
print(f"Type of Documents: {type(chunks2)}")
print(f"Documents: {chunks2}")