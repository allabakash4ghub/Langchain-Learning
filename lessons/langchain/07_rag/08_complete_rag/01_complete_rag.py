'''Why is this called Retrieval-Augmented Generation?
Retrieval-Augmented Generation (RAG) is a workflow that combines retrieval and generation. 
It allows an application to retrieve relevant information from external data sources before 
generating an answer. This approach enhances the quality and accuracy of the generated responses
by providing the model with additional context from the retrieved documents.

Retrieval : We retrieve information.
User Question
      ↓
Retriever
      ↓
Relevant Documents

Augmented : We augment the model's knowledge with the retrieved information.
We add that retrieved information to the prompt:

Question
+
Retrieved Context

The prompt is augmented with external knowledge.

Generation : We generate an answer.
The model generates an answer based on the augmented prompt.

Retrieval
    +
Augmentation
    +
Generation
    =
RAG

'''

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# create an embedding model instance
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small"
)

# create a chat model instance
chat_model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0.0,
    max_completion_tokens=100
)

# -----------------------------------
# 1. Create documents
# -----------------------------------

texts = [
    "Employees receive 20 days of annual leave per year.",
    
    "Medical insurance covers hospitalization expenses for employees.",
    
    "Customers can request a refund within 30 days of purchase."
]

#create a vector store instance
vector_store = Chroma.from_texts(
    texts = texts,    
    embedding=embeddings
)

# create a retriever instance from the vector store
retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 2}
)

# create a prompt template for the chat model
prompt_template = ChatPromptTemplate.from_template(
    template = """You are a helpful assistant. Use only the following context to answer the question.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:"""
)

# -----------------------------------
# 7. Ask a question
# -----------------------------------

question = "How long do I have to request a refund?"

# -----------------------------------
# 8. Retrieve relevant documents
# -----------------------------------

documents = retriever.invoke(question)

# -----------------------------------
# 9. Convert documents into context
# -----------------------------------

context = "\n".join([doc.page_content for doc in documents])

# -----------------------------------
# 10. Create prompt messages
# -----------------------------------

messages = prompt_template.invoke(
    {"context": context,
     "question": question}
)

# -----------------------------------
# 11. Send prompt to LLM
# -----------------------------------

response = chat_model.invoke(messages)

# -----------------------------------
# 12. Print result
# -----------------------------------

print("\nQuestion:")
print(question)

print("\nRetrieved Context:")
print(context)

print("\nAnswer:")
print(response.content)

print(f"response full: {response}")


''' print output as follows:
Question:
How long do I have to request a refund?

Retrieved Context:
Customers can request a refund within 30 days of purchase.
Employees receive 20 days of annual leave per year.

Answer:
You have 30 days to request a refund.
response full: content='You have 30 days to request a refund.' 
additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 70, 'total_tokens': 80, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_62666fb687', 'id': 'chatcmpl-ENDUQ4G3OJ5S9Du6joIxLYPX0bVLa', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--01a094c1-853f-73e1-bf2b-d01e4ccf9acd-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 70, 'output_tokens': 10, 'total_tokens': 80, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

'''