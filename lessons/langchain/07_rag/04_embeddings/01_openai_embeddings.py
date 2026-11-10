from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# --------------------------------------------
# Create embedding model
# --------------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# --------------------------------------------
# Convert one sentence into an embedding
# --------------------------------------------

text = "LangChain is a framework for building LLM applications."

vector = embeddings.embed_query(text)

# --------------------------------------------
# Display results
# --------------------------------------------

print(f"Text: {text}")
print(f"Vector length: {len(vector)}") # Vector length: 1536
print(f"Type of vector: {type(vector)}") # Type of vector: <class 'list'>
print(f"Vector: {vector}") # [-0.01495361328125, 0.0098419189453125, 0.047760009765625,....]