from app.services.retrieval_service import retrieve_chunks
from app.services.chat_service import generate_answer

question = "What is this memo about?"

chunks = retrieve_chunks(question)

answer = generate_answer(
    question=question,
    chunks=chunks
)

print("\nQUESTION\n")
print(question)

print("\nANSWER\n")
print(answer)