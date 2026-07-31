import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    # Azure Storage
    STORAGE_CONNECTION = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

    # Azure AI Document Intelligence
    DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv(
        "AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"
    )

    DOCUMENT_INTELLIGENCE_KEY = os.getenv(
        "AZURE_DOCUMENT_INTELLIGENCE_KEY"
    )

    # Azure OpenAI
    OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    OPENAI_API_VERSION = os.getenv(
        "AZURE_OPENAI_API_VERSION"
    )

    OPENAI_CHAT_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_CHAT_DEPLOYMENT"
    )

    OPENAI_EMBEDDING_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    )

    # Azure AI Search
    SEARCH_ENDPOINT = os.getenv(
        "AZURE_SEARCH_ENDPOINT"
    )

    SEARCH_KEY = os.getenv(
        "AZURE_SEARCH_KEY"
    )

    SEARCH_INDEX = os.getenv(
        "AZURE_SEARCH_INDEX"
    )


settings = Settings()