import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def add_chunks(chunks, embeddings):
    ids = []

    documents = []

    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"{chunk['filename']}_{i}")

        documents.append(chunk["chunk"])

        metadatas.append({
            "filename": chunk["filename"],
            "chunk_number": i
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_chunks(query_embedding, n_results=5):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    chunks = []

    if len(results["documents"]) == 0:
        return chunks

    for i in range(len(results["documents"][0])):

        chunks.append({
            "chunk": results["documents"][0][i],
            "filename": results["metadatas"][0][i]["filename"]
        })

    return chunks