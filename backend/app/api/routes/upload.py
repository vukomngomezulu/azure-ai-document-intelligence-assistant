from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import save_file
from app.services.local_document_service import extract_text
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.chroma_service import add_chunks

router = APIRouter()

ALLOWED_EXTENSIONS = [".txt"]


@router.post("/")
async def upload_document(file: UploadFile = File(...)):

    extension = "." + file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    # Save locally
    file_path = save_file(file)

    # Extract text locally
    text = extract_text(file_path)
    # Chunk text
    chunks = chunk_text(text)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="No text found in document."
        )

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Prepare chunks for ChromaDB
    chunk_data = []

    for i, chunk in enumerate(chunks):
        chunk_data.append({
            "chunk": chunk,
            "filename": file.filename,
            "chunk_number": i
        })

    # Store in ChromaDB
    add_chunks(chunk_data, embeddings)

    return {
        "message": "Document indexed successfully",
        "chunks": len(chunk_data)
    }