from fastapi import APIRouter

from pydantic import BaseModel

from app.services.chat_service import chat_with_database

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    reply = chat_with_database(request.message)

    return {
        "reply": reply
    }
