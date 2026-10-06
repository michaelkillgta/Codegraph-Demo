"""
database.py - Simple in-memory storage for chat logs.
"""

# In-memory list to store chat messages
chat_history = []


def save_chat(question: str, answer: str) -> None:
    """Saves a user question and system answer to the chat history."""
    chat_history.append({"question": question, "answer": answer})
    print(f"[Database] Saved chat record: {question} -> {answer}")


def get_chat_history() -> list:
    """Returns the list of all recorded chats."""
    return chat_history
