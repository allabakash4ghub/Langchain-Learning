'''   
                    ChatOpenAI
                        │
             ┌──────────┴──────────┐
             │                     │
        Normal Output        Structured Output
             │                     │
             ▼                     ▼
       StrOutputParser        Pydantic
             │                     │
             ▼                     ▼
           str                  Employee

You can combine LangChain components based on the type of output you need.

Need plain text?

prompt | llm | StrOutputParser()

Need structured data?

prompt | llm.with_structured_output(Employee)        

'''
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatMessagePromptTemplate,ChatPromptTemplate
from pydantic import BaseModel,Field

load_dotenv()

# -----------------------------------------
# 1. Define the expected output structure
# -----------------------------------------

class Employee (BaseModel):
    name:str = Field(description="Employee's full name")
    age:int  = Field(description="Employee's age")
    role:str = Field(description="Employee's Job Role ") 

# -----------------------------------------
# 2. Create the prompt
# -----------------------------------------

prompt=ChatPromptTemplate.from_messages(
    [ 
        ("system",
         "You are an information extraction assistant."
         "Extract the employee information from the use's text."
        ),
        (
            "human",
            "{employee_information}"
        )


    ]
)

# -----------------------------------------
# 3. Create the LLM
# -----------------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1,
    max_completion_tokens=80
)

# -----------------------------------------
# 4. Configure structured output
# -----------------------------------------

structured_llm=llm.with_structured_output(Employee)
# -----------------------------------------
# 5. Create the LCEL chain
# -----------------------------------------
chain=prompt|structured_llm
# -----------------------------------------
# 6. Invoke the chain
# -----------------------------------------
response=chain.invoke({
    "employee_information":
    """
       John is 35 years old and works as a
       Data Scientist.
    """
}

)

print("\nResponse:")
print(response)

print("\nResponse Type:")
print(type(response))

employee_dict = response.model_dump()

print(f"Dictionary Output:{employee_dict}")

employee_json=response.model_dump_json()

print(f"Json Format:{employee_json}")