from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    STORAGE_CONNECTION = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

settings = Settings()