from openai import AzureOpenAI
from app.config.settings import settings

client = AzureOpenAI(
    azure_endpoint=settings.OPENAI_ENDPOINT,
    api_key=settings.OPENAI_API_KEY,
    api_version=settings.OPENAI_API_VERSION,
)

print("Endpoint:", settings.OPENAI_ENDPOINT)
print("Deployment:", settings.OPENAI_EMBEDDING_DEPLOYMENT)

try:
    response = client.embeddings.create(
        model=settings.OPENAI_EMBEDDING_DEPLOYMENT,
        input="Hello world"
    )

    print("SUCCESS")
    print(len(response.data[0].embedding))

except Exception as e:
    print(e)