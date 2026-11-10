from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda,RunnableAssign
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, output_parsers


# Load environment variables
load_dotenv()


# --------------------------------------------------
# 1. Clean the user's input
# --------------------------------------------------

def clean_topic(data):
    data["topic"]=data["topic"].strip()
    return data

clean_input=RunnableLambda(clean_topic)

# --------------------------------------------------
# 2. Add additional information
# --------------------------------------------------

add_information=RunnableAssign(
    {
           "topic_length" : RunnableLambda (
            lambda x : len(x["topic"])
        )

    }
)

# --------------------------------------------------
# 3. Create the prompt
# --------------------------------------------------

prompt=ChatPromptTemplate.from_messages(
    [  
        ("system",
         "You are a helful technical tutor."
         "explain the concepts clearly and simply"
        ),
        ("human",
         "Explain the {topic} in {number} simple sentences."
         "The topic name contains {topic_length} characters."

        )
    ]
)

# --------------------------------------------------
# 4. Create the LLM
# --------------------------------------------------

llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=75
)

# --------------------------------------------------
# 5. Create output parser
# --------------------------------------------------

output_parser=StrOutputParser()

# --------------------------------------------------
# 6. Build the complete chain
# --------------------------------------------------

chain= (clean_input
        | add_information
        | prompt
        | llm
        | output_parser)


# --------------------------------------------------
# 7. Execute the chain
# --------------------------------------------------

result = chain.invoke(
    {
        "topic":"  langchain    ",
        "number": 2
    } )

print("\nFinal Response:")
print(result)

print("\nResponse Type:")
print(type(result))

