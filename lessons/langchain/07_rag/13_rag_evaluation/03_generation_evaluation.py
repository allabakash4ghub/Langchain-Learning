from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field,BaseModel
from dotenv import load_dotenv

# ============================================================
# 1. Evaluation LLM
# ============================================================
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.0,
    seed=42,
    max_tokens=1000
)

# ============================================================
# 2. Evaluation Output Schema
# ============================================================

class EvaluationResults(BaseModel):
    faithfulness : int = Field(
        description="Score from 1 to 5 indicating how well the answer is supported by the context."
    )

    answer_relevance:int=Field(
        description="Score from 1 to 5 indicating how well the answer addresses the question."
    )

    explanation:str=Field(
        description="Brief explanantion about the results"
    )

evaluator=llm.with_structured_output(EvaluationResults)    

# ============================================================
# 3. Question
# ============================================================

question="""
what is F1 score?
"""

# ============================================================
# 4. Retrieved Context
# ============================================================

context = """
F1-Score is the harmonic mean of precision and recall.
It is useful for evaluating classification performance,
particularly on imbalanced datasets.
"""

# ============================================================
# 5. Generated Answer
# ============================================================

# answer = """
# F1-score is the harmonic mean of precision and recall.
# It is useful when evaluating classification models on
# imbalanced datasets.
# """

answer = """
F1-score is the harmonic mean of precision and recall.
It is always the best classification metric and is
better than accuracy for every classification problem.
It also guarantees that the classifier will perform
well on unseen data.
"""

# ============================================================
# 6. Evaluation Prompt
# ============================================================

evaluation_prompt=ChatPromptTemplate.from_template(
    """You are evaluating the quality of a RAG system.

    Evaluate the generated answer using ONLY the supplied
    question and context.

    Do not use outside knowledge.

    -------------------------------
    QUESTION
    -------------------------------
    {question}

    -------------------------------
    CONTEXT
    -------------------------------
    {context}

    -------------------------------
    GENERATED ANSWER
    -------------------------------
    {answer}

    -------------------------------
    EVALUATION CRITERIA
    -------------------------------

    Faithfulness:
    Does every important claim in the answer have support
    in the supplied context?

    Score:
    1 = completely unsupported
    2 = mostly unsupported
    3 = partially supported
    4 = mostly supported
    5 = fully supported

    Answer Relevance:
    Does the answer directly address the user's question?

    Score:
    1 = completely irrelevant
    2 = mostly irrelevant
    3 = partially relevant
    4 = mostly relevant
    5 = directly and completely relevant

    Provide a brief explanation for the scores.
    """
)

print(f"type of evaluation_prompt : {type(evaluation_prompt)}")

# ============================================================
# 7. Run Evaluation
# ============================================================

evaluation=evaluator.invoke(
    evaluation_prompt.format_messages(
        question=question,
        context=context,
        answer=answer
    )
)

# ============================================================
# 8. Display Result
# ============================================================

print("=" * 70)
print("RAG GENERATION EVALUATION")
print("=" * 70)

print("\nQuestion:")
print(question)

print("\nGenerated Answer:")
print(answer)

print(f"type of evaluation : {type(evaluation)}")

print("Final evaluation Result:",evaluation)

print(
    "Faithfulness:",
    evaluation.faithfulness
)

print(
    "Answer Relevance:",
    evaluation.answer_relevance
)

print(
    "Explanation:",
    evaluation.explanation
)