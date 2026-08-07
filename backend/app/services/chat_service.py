import ollama


def generate_answer(question, chunks, history=None):
    """
    Generate an answer using the retrieved document chunks and
    optional conversation history.
    """

    if history is None:
        history = []

    context = "\n\n".join(
        chunk["chunk"] for chunk in chunks
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that answers questions ONLY "
                "using the provided context. "
                "If the answer is not in the context, reply with "
                "'I could not find that information in the uploaded documents.'"
            )
        }
    ]

    # Add previous conversation
    messages.extend(history)

    # Add current question
    messages.append(
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}

Answer:
"""
        }
    )

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    return response["message"]["content"]