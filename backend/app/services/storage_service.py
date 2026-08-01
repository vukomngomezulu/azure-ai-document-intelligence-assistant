from pathlib import Path
import shutil

from azure.storage.blob import BlobServiceClient

from app.config.settings import settings


blob_service = BlobServiceClient.from_connection_string(
    settings.STORAGE_CONNECTION
)

container_client = blob_service.get_container_client(
    settings.STORAGE_CONTAINER
)

# Create the container if it doesn't exist
try:
    container_client.create_container()
except Exception:
    pass

TEMP_FOLDER = Path("temp")

TEMP_FOLDER.mkdir(exist_ok=True)


def upload_to_blob(file):
    """
    Upload a file to Azure Blob Storage.
    """

    blob_client = container_client.get_blob_client(file.filename)

    blob_client.upload_blob(
        file.file,
        overwrite=True
    )

    return blob_client.url


def download_blob(filename):
    """
    Download a blob to a temporary local file.
    """

    blob_client = container_client.get_blob_client(filename)

    destination = TEMP_FOLDER / filename

    with open(destination, "wb") as download_file:
        download_file.write(
            blob_client.download_blob().readall()
        )

    return destination


def delete_temp_file(path):
    """
    Remove the temporary local file.
    """

    if path.exists():
        path.unlink()