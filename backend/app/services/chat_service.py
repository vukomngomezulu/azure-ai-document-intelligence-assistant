from openai import AzureOpenAI

from app.config.settings import settings


client = AzureOpenAI(
    azure_endpoint=settings.OPENAI_ENDPOINT,
    api_key=settings.OPENAI_API_KEY,
    api_version=settings.OPENAI_API_VERSION,
)


def generate_answer(question: str, chunks, history):
    """
    Generate an answer using GPT-5.5 with conversation history.
    """

    context = "\n\n".join(
        [
            f"Document: {chunk['filename']}\n{chunk['chunk']}"
            for chunk in chunks
        ]
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI document assistant.\n"
                "Answer ONLY using the supplied document context.\n"
                "If the answer is not present, reply:\n"
                "\"I couldn't find that information in the uploaded documents.\""
            )
        }
    ]

    # Previous conversation
    messages.extend(history)

    # Current question
    messages.append(
        {
            "role": "user",
            "content": f"""
Context:

{context}

Question:

{question}
"""
        }
    )

    response = client.chat.completions.create(
        model=settings.OPENAI_CHAT_DEPLOYMENT,
        messages=messages
    )

    return response.choices[0].message.content