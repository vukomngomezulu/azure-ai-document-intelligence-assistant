from fastapi import FastAPI

app = FastAPI(
    title="Azure AI Document Intelligence Assistant",
    description="A cloud-native Retrieval-Augmented Generation (RAG) platform for intelligent document understanding.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "project": "Azure AI Document Intelligence Assistant",
        "status": "Running",
        "version": "1.0.0"
    }