from azure.storage.blob import BlobServiceClient
from app.config.settings import settings

blob_service = BlobServiceClient.from_connection_string(
    settings.STORAGE_CONNECTION
)

container_client = blob_service.get_container_client(
    settings.STORAGE_CONTAINER
)

def upload_file(file):

    blob_client = container_client.get_blob_client(file.filename)

    blob_client.upload_blob(
        file.file,
        overwrite=True
    )

    return blob_client.url