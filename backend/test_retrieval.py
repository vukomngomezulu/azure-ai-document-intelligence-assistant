from app.services.retrieval_service import retrieve_chunks

results = retrieve_chunks(
    "What is this document about?"
)

print(results)