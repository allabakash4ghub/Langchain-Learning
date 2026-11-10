from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from openai import vector_stores

load_dotenv()

# --------------------------------------------------
# 1. PDF paths
# --------------------------------------------------

PDF_FILES=[
    r"data\AI Evaluation Report.pdf",
    r"data\Machine Learning & Deep Learning Algorithms and Evaluation Metrics.pdf"
]
CHROMA_PATH = r"chroma_db"

# --------------------------------------------------
# 2. Load PDFs
# --------------------------------------------------

documents = []

for pdf_file in PDF_FILES:
    loader=PyPDFLoader(pdf_file)
    pdf_doc=loader.load()
    documents.extend(pdf_doc)

print(f"Loaded {len(documents)} pages")    


# --------------------------------------------------
# 3. Split documents into chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks=text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# --------------------------------------------------
# 4. Create embeddings
# --------------------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# --------------------------------------------------
# 5. Store in Chroma
# --------------------------------------------------

vector_store=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_PATH
)

print("Documents stored in Chroma")

# --------------------------------------------------
# 6. Inspect metadata
# --------------------------------------------------

print("\nSample chunk metadata:")

# for chunk in chunks[:3]:
#     print(chunk.metadata)


for i, chunk in enumerate(chunks[:5]):

    print("\n-------------------------")
    print(f"Chunk {i}")
    print("-------------------------")

    print("Content:")
    print(chunk.page_content[:50])

    print("Metadata:")
    print(chunk.metadata)