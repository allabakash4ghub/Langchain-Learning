import langchain
from langchain_core.prompts import ChatPromptTemplate

# Create a chat prompt template
prompt=ChatPromptTemplate.from_messages(
    [ ("system",
       "You are a helful tutor explain the concepts in a easy to understand way."
       ),
       ( "human",
        "explain {topic} in {number} simple sentences"           
       )
    ])

# Provide values for the placeholders

final_prompt=prompt.invoke(
{    
"topic":"langchain",
"number":2
}

)

print("\nprompt type")
print(type(final_prompt))

print("\nMessages:")
print(final_prompt.messages)

print("\nPrompt as String:")
print(final_prompt.to_string())