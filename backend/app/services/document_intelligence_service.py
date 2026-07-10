from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

from app.config.settings import settings


client = DocumentIntelligenceClient(
    endpoint=settings.DOCUMENT_INTELLIGENCE_ENDPOINT,
    credential=AzureKeyCredential(
        settings.DOCUMENT_INTELLIGENCE_KEY
    )
)


def extract_document(path: str):
    """
    Extract text and layout information from a document.
    """

    with open(path, "rb") as document:

        poller = client.begin_analyze_document(
            "prebuilt-layout",
            body=document
        )

        result = poller.result()

    return result