from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


# ==================================================
# 1. Create LLM
# ==================================================

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# llm=ChatGroq(
#      model="openai/gpt-oss-120b",
#      temperature=0.1,
#      max_tokens=80
# )

# ==================================================
# 2. Query rewriting prompt
# ==================================================

prompt = ChatPromptTemplate.from_template(
    """
You are a query rewriting assistant for a RAG system.

Rewrite the user's question into a concise,
standalone search query suitable for document retrieval.

Rules:
- Preserve the original meaning.
- Resolve conversational references using the conversation.
- Include important context from previous messages.
- Remove unnecessary words.
- Do not answer the question.
- Return only the rewritten search query.

Conversation:
{conversation}

User question:
{question}
"""
)


# ==================================================
# 3. Create LCEL chain
# ==================================================

chain = prompt | llm


# ==================================================
# 4. Conversation history
# ==================================================

conversation = """
User: What are the main evaluation metrics
used for classification models?

Assistant: Accuracy, Precision, Recall,
F1-Score and ROC-AUC are commonly used.
"""


# ==================================================
# 5. Follow-up question
# ==================================================

question = "Which one should I use for imbalanced data?"


# ==================================================
# 6. Rewrite the query
# ==================================================

response = chain.invoke(
    {
        "conversation": conversation,
        "question": question
    }
)


# ==================================================
# 7. Display results
# ==================================================

print("\nOriginal Query:")
print(question)

print("\nRewritten Query:")
print(response.content)
#print(f"llm.profile: {llm.profile}")