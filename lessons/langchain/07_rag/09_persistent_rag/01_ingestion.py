from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Configuration
# -----------------------------------
SOURCE_FILE_PATH = r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\09_persistent_rag\data\company_policy.txt"
CROMA_PATH = r"E:\GenAI\Langchain-Learning\lessons\langchain\07_rag\09_persistent_rag\data\chroma_db"

# -----------------------------------
# 1. Load document
# -----------------------------------

loader = TextLoader(SOURCE_FILE_PATH)
documents = loader.load()
print(f"Loaded documents: {len(documents)}")

# -----------------------------------
# 2. Split document into chunks
# -----------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)

chunks = splitter.split_documents(documents)
print(f"Number of chunks created: {len(chunks)}")
print(f"sample chunk: {chunks[0]}")

# -----------------------------------
# 3. Create embedding model
# -----------------------------------
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# -----------------------------------
# 4. Create persistent Chroma database
# -----------------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CROMA_PATH
)

print("\nIngestion completed successfully!")

print(f"Vector database saved in: {CROMA_PATH}")