from app.services.embedding_service import generate_embedding

embedding = generate_embedding("Hello world")

print(type(embedding))
print(len(embedding))