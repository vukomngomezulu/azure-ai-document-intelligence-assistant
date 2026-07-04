from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import save_file

router = APIRouter()


ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt"
]


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    extension = "." + file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    filepath = save_file(file)

    return {
        "message": "Upload successful",
        "filename": file.filename,
        "path": str(filepath)
    }