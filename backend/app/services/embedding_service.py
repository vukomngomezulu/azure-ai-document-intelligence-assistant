import ollama


def generate_embedding(text: str):
    """
    Generate an embedding for a single text.
    """

    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]


def generate_embeddings(chunks):
    """
    Generate embeddings for multiple chunks.
    """

    embeddings = []

    for chunk in chunks:
        embeddings.append(
            generate_embedding(chunk)
        )

    return embeddings