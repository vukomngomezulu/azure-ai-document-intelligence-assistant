from openai import AzureOpenAI

from app.config.settings import settings


client = AzureOpenAI(
    azure_endpoint=settings.OPENAI_ENDPOINT,
    api_key=settings.OPENAI_API_KEY,
    api_version=settings.OPENAI_API_VERSION,
)


def generate_embedding(text: str):
    """
    Generate an embedding for a single text chunk.
    """

    try:
        response = client.embeddings.create(
            model=settings.OPENAI_EMBEDDING_DEPLOYMENT,
            input=text
        )

        return response.data[0].embedding

    except Exception as e:
        raise Exception(f"Failed to generate embedding: {str(e)}")


def generate_embeddings(chunks):
    """
    Generate embeddings for multiple chunks.
    """

    embeddings = []

    for chunk in chunks:

        embeddings.append(
            {
                "text": chunk,
                "embedding": generate_embedding(chunk)
            }
        )

    return embeddings