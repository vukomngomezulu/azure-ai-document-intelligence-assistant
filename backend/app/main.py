from fastapi import FastAPI

from app.api.routes import upload

app = FastAPI(
    title="Azure AI Document Intelligence Assistant",
    version="1.0.0"
)

app.include_router(
    upload.router,
    prefix="/documents",
    tags=["Documents"]
)


@app.get("/")
def root():
    return {
        "status": "Running"
    }