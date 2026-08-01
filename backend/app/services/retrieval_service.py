from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

from app.config.settings import settings
from app.services.embedding_service import generate_embedding


search_client = SearchClient(
    endpoint=settings.SEARCH_ENDPOINT,
    index_name=settings.SEARCH_INDEX,
    credential=AzureKeyCredential(settings.SEARCH_KEY)
)


def retrieve_chunks(question: str, top_k: int = 3):
    """
    Retrieve the most relevant document chunks using vector search.
    """

    # Generate embedding for the user's question
    question_embedding = generate_embedding(question)

    # Build vector query
    vector_query = VectorizedQuery(
        vector=question_embedding,
        k_nearest_neighbors=top_k,
        fields="embedding"
    )

    # Search Azure AI Search
    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=["filename", "chunk"]
    )

    chunks = []

    for result in results:
        chunks.append(
            {
                "filename": result["filename"],
                "chunk": result["chunk"]
            }
        )

    return chunks