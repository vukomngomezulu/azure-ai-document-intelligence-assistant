from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    STORAGE_CONNECTION = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

    DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv(
        "AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"
    )

    DOCUMENT_INTELLIGENCE_KEY = os.getenv(
        "AZURE_DOCUMENT_INTELLIGENCE_KEY"
    )
settings = Settings()