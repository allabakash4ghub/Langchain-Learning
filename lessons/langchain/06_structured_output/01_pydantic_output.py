'''
When we need structured output instead of string , we use pydantic

'''

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
import json

load_dotenv()

# -----------------------------------------
# 1. Define the expected output structure
# -----------------------------------------

class Employee(BaseModel):
    name : str=Field(description="Employee's Full Name")
    age  : int=Field(description="Employee's Age")
    role : str=Field(description="Employee's Role")


# --------------------------------------------------
# 1. Create the LLM
# --------------------------------------------------

# Create a the ChatOpenAI model object 

llm=ChatOpenAI(
model="gpt-4o-mini",
temperature=0.1,
max_completion_tokens=80
)

# -----------------------------------------
# 3. Tell the LLM to return Employee data
# -----------------------------------------
structured_llm=llm.with_structured_output(Employee)

# -----------------------------------------
# 4. Send information to the LLM
# -----------------------------------------

response=structured_llm.invoke(
    """john is 35 years old and works 
    as a Data Scientist"""
)

# -----------------------------------------
# 5. Display the result
# -----------------------------------------

print("\nResponse:")
print(response)

print("\nResponse Type:")
print(type(response))

print("\nEmployee Name:")
print(response.name)

print("\nEmployee Age:")
print(response.age)

print("\nEmployee Role:")
print(response.role)

employee_dict = response.model_dump()

print(f"Dictionary Output:{employee_dict}")

employee_json=response.model_dump_json()

print(f"Json Format:{employee_json}")