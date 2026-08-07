import uuid

from azure.core.credentials import AzureKeyCredential

from azure.search.documents import SearchClient

from azure.search.documents.indexes import SearchIndexClient

from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)

from app.config.settings import settings


# Create Index Client
index_client = SearchIndexClient(
    endpoint=settings.SEARCH_ENDPOINT,
    credential=AzureKeyCredential(settings.SEARCH_KEY)
)


# Create Search Client
search_client = SearchClient(
    endpoint=settings.SEARCH_ENDPOINT,
    index_name=settings.SEARCH_INDEX,
    credential=AzureKeyCredential(settings.SEARCH_KEY)
)


def create_index():
    """
    Create Azure AI Search index if it doesn't exist.
    """

    fields = [

        SimpleField(
            name="id",
            type=SearchFieldDataType.String,
            key=True
        ),

        SimpleField(
    name="chunk_number",
    type=SearchFieldDataType.Int32,
    filterable=True,
    sortable=True
),

        SearchableField(
            name="filename",
            type=SearchFieldDataType.String
        ),

        SearchableField(
            name="chunk",
            type=SearchFieldDataType.String
        ),

        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(
                SearchFieldDataType.Single
            ),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="my-vector-profile"
        ),
    ]

    vector_search = VectorSearch(

        algorithms=[
            HnswAlgorithmConfiguration(
                name="my-hnsw"
            )
        ],

        profiles=[
            VectorSearchProfile(
                name="my-vector-profile",
                algorithm_configuration_name="my-hnsw"
            )
        ]
    )

    index = SearchIndex(
        name=settings.SEARCH_INDEX,
        fields=fields,
        vector_search=vector_search
    )

    try:
        index_client.get_index(settings.SEARCH_INDEX)
        print("Search index already exists.")

    except Exception:

        index_client.create_index(index)
        print("Search index created.")


def upload_documents(filename, embeddings):
    """
    Upload document chunks and embeddings into Azure AI Search.
    """

    documents = []

    for index, item in enumerate(embeddings):

        documents.append(
    {
        "id": f"{filename}-{index}",
        "filename": filename,
        "chunk": chunk,
        "chunk_number": index,
        "embedding": embedding
    }
)
    result = search_client.upload_documents(documents)

    return result