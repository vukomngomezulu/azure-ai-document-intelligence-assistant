from app.services.retrieval_service import retrieve_chunks

results = retrieve_chunks(
    "What is this memo about?"
)

for item in results:
    print("-" * 50)
    print(item["filename"])
    print(item["chunk"])