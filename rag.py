"""
rag.py - Retrieval-Augmented Generation (RAG) context retrieval.
"""

import utils


def retrieve_context(question: str) -> str:
    """Retrieves mock context for a given question after cleaning it."""
    cleaned = utils.clean_text(question)
    print(f"[RAG] Retrieving context for query: '{cleaned}'")
    return f"Retrieved knowledge context relevant to '{cleaned}'"
