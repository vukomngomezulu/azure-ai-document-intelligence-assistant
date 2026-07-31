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


def get_document_text(result):
    """
    Extract all text from the Document Intelligence result.
    """

    if hasattr(result, "content") and result.content:
        return result.content

    text = ""

    if hasattr(result, "paragraphs") and result.paragraphs:
        for paragraph in result.paragraphs:
            text += paragraph.content + "\n"

    return text.strip()