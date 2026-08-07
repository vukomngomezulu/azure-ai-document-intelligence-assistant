from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.retrieval_service import retrieve_chunks
from app.services.chat_service import generate_answer

router = APIRouter()


@router.post("/")
def chat(request: ChatRequest):

    chunks = retrieve_chunks(request.question)

    answer = generate_answer(
        question=request.question,
        chunks=chunks
    )

    sources = list(
        {
            chunk["filename"]
            for chunk in chunks
        }
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }