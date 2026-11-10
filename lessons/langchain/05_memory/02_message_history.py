from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


load_dotenv()

# --------------------------------------------------
# 1. Create the LLM
# --------------------------------------------------

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens= 100
)

# --------------------------------------------------
# 2. Create the prompt
# --------------------------------------------------

prompt =ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helful assistance."),
        MessagesPlaceholder(
            variable_name="history"             
         ),
         (
             "human",
             "{input}"
         )
    ]
)

# --------------------------------------------------
# 3. Create the basic chain
# --------------------------------------------------

chain=prompt | llm 

# --------------------------------------------------
# 4. Store chat histories
# --------------------------------------------------

store={}

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()

    return store[session_id]     

# --------------------------------------------------
# 5. Add message history to the chain
# --------------------------------------------------

conversation=RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# --------------------------------------------------
# 6. First question
# --------------------------------------------------

response=conversation.invoke(
    {
        "input":"My name is Bunny."
    },
    config={
        "configurable": {
            "session_id": "user_1"
        }
    }
)

print("\nAI:")
print(response.content)

# --------------------------------------------------
# 7. Second question
# --------------------------------------------------

response=conversation.invoke(
    {
        "input": "What is my name?"
    },
    config={
        "configurable": {
            "session_id": "user_1"
        }
    }
)

print("\nAI:")
print(response.content)