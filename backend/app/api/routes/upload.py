from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import save_file
from app.services.document_intelligence_service import extract_document

router = APIRouter()

ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt"
]


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document and extract its contents using
    Azure AI Document Intelligence.
    """

    # Validate file extension
    extension = "." + file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only PDF, DOCX and TXT files are allowed."
        )

    # Save the uploaded file locally
    filepath = save_file(file)

    # Analyze the document
    result = extract_document(str(filepath))

    # Return basic information
    return {
        "message": "Document processed successfully",
        "filename": file.filename,
        "pages": len(result.pages),
        "paragraphs": len(result.paragraphs) if result.paragraphs else 0
    }