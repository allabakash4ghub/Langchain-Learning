from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# create an embedding model instance
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small"
)

# create a chat model instance
llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature =0.0,
    max_completion_tokens=100
)

#create a prompt template for the chat model
prompt = ChatPromptTemplate.from_template(
    template = """You are a helpful assistant. Use only the following context to answer the question.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:"""
)

# -----------------------------------
# Documents
# -----------------------------------

texts = [
    "Employees receive 20 days of annual leave per year.",

    "Medical insurance covers hospitalization expenses for employees.",

    "Customers can request a refund within 30 days of purchase."
]


#create a vector store instance
vector_store = Chroma.from_texts(
    texts = texts,
    embedding = embeddings
)


# -----------------------------------
# Retriever
# -----------------------------------
retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs ={"k": 2})

# -----------------------------------
# Format retrieved documents
# -----------------------------------

def format_docs(docs):
    formatted_docs =[]
    for doc in docs:
        formatted_docs.append(doc.page_content)
    return "\n".join(formatted_docs)  

# -----------------------------------
# RAG Chain
# -----------------------------------

rag_chain = (
      {
       "context" : retriever|format_docs,
       "question" : RunnablePassthrough()
      }
      | prompt 
      | llm
  )

# -----------------------------------
# Ask Question
# -----------------------------------

question = "How long do I have to request a refund?"

response = rag_chain.invoke(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(response.content)