from app.services.embedding_service import generate_embedding
from app.services.chroma_service import search_chunks


def retrieve_chunks(question):

    embedding = generate_embedding(question)

    return search_chunks(embedding)