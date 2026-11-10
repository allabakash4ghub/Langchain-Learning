from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()


loader = TextLoader(
    "data/company_policy.txt"
)

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)


chunks = splitter.split_documents(documents)


print("Number of chunks:", len(chunks))


for i, chunk in enumerate(chunks):

    print(f"\n========== Chunk {i + 1} ==========")

    print("Content:")
    print(chunk.page_content)

    print("\nMetadata:")
    print(chunk.metadata)