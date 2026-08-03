from fastapi import APIRouter

from app.models.conversation import ConversationRequest

from app.services.retrieval_service import retrieve_chunks
from app.services.chat_service import generate_answer
from app.services.memory_service import (
    add_message,
    get_history,
)

router = APIRouter()


@router.post("/")
def chat(request: ConversationRequest):

    history = get_history(
        request.conversation_id
    )

    chunks = retrieve_chunks(
        request.question
    )

    answer = generate_answer(
        question=request.question,
        chunks=chunks,
        history=history
    )

    add_message(
        request.conversation_id,
        "user",
        request.question
    )

    add_message(
        request.conversation_id,
        "assistant",
        answer
    )

    return {
        "conversation_id": request.conversation_id,
        "answer": answer,
        "sources": list(
            {
                chunk["filename"]
                for chunk in chunks
            }
        )
    }