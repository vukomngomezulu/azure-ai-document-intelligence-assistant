
from collections import defaultdict

conversation_store = defaultdict(list)


def get_history(conversation_id: str):
    """
    Return the conversation history.
    """

    return conversation_store[conversation_id]


def add_message(conversation_id: str, role: str, content: str):
    """
    Save a message.
    """

    conversation_store[conversation_id].append(
        {
            "role": role,
            "content": content
        }
    )


def clear_history(conversation_id: str):
    """
    Delete a conversation.
    """

    if conversation_id in conversation_store:
        del conversation_store[conversation_id]