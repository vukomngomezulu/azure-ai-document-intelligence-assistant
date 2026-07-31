from pathlib import Path

from app.config.settings import settings
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import save_file
from app.services.document_intelligence_service import (
    extract_document,
    get_document_text,
)
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings

router = APIRouter()

ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt",
]


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document, extract its text,
    split it into chunks and generate embeddings.
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    # Save uploaded file
    filepath = save_file(file)

    # Extract text using Azure AI Document Intelligence
    result = extract_document(str(filepath))

    # Get plain text
    document_text = get_document_text(result)

    # Split into chunks
    chunks = chunk_text(document_text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No text could be extracted from the document."
        )

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    from app.services.search_service import upload_documents

    upload_documents(
        filename=file.filename,
        embeddings=embeddings
    )
    return {
    "message": "Document indexed successfully",
    "filename": file.filename,
    "pages": len(result.pages),
    "chunks_created": len(chunks),
    "embeddings_created": len(embeddings),
    "vector_database": settings.SEARCH_INDEX
}