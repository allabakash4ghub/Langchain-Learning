from langchain_core.prompts import PromptTemplate

# create a prompt template

prompt = PromptTemplate(template="Explain the {topic} in {number} simple sentences",
                       input_variables=["topic","number"])

# Provide values for the variables
final_prompt=prompt.invoke(
    {
        "topic":"langchain",
        "number":2
    }
)
print(final_prompt)
print(type(final_prompt))
print(final_prompt.to_string())
print(type(final_prompt.to_string()))