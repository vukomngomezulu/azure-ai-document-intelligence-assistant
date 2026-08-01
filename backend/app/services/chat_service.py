from openai import AzureOpenAI

from app.config.settings import settings


client = AzureOpenAI(
    azure_endpoint=settings.OPENAI_ENDPOINT,
    api_key=settings.OPENAI_API_KEY,
    api_version=settings.OPENAI_API_VERSION,
)


def generate_answer(question: str, chunks):
    """
    Generate an answer using GPT-5.5 and the retrieved document chunks.
    """

    context = "\n\n".join(
        [
            f"Document: {chunk['filename']}\n{chunk['chunk']}"
            for chunk in chunks
        ]
    )

    system_prompt = """
You are an AI document assistant.

Answer ONLY using the information provided in the context.

If the answer cannot be found in the context, reply:

"I couldn't find that information in the uploaded documents."

Do not make up information.
"""

    user_prompt = f"""
Context:

{context}

Question:

{question}
"""

    response = client.chat.completions.create(
        model=settings.OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
       
    )

    return response.choices[0].message.content