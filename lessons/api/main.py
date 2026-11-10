from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Support Triage Helper")


class TicketRequest(BaseModel):
    ticket_text: str = Field(
        ...,
        description="The customer support ticket message",
        example="My package arrived damaged and I need help with a replacement."
    )


@app.post("/triage-ticket")
async def triage_ticket(payload: TicketRequest):
    ticket_text = payload.ticket_text.strip()

    if not ticket_text:
        raise HTTPException(
            status_code=400,
            detail="ticket_text is required"
        )

    # If you need to make an async call (e.g., calling an LLM or database):
    # response = await call_async_llm_service(ticket_text)

    lower_text = ticket_text.lower()

    if "damaged" in lower_text:
        category = "damaged_item"
    elif "refund" in lower_text:
        category = "refund_request"
    else:
        category = "general_support"

    return {
        "category": category,
        "summary": ticket_text[:140]
    }