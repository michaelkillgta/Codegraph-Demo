"""
chatbot.py - Core coordinator for responding to user queries.
"""

import database
import rag
import utils


def ask_question(question: str) -> str:
    """Coordinates context retrieval, text cleaning, answer creation, and storage."""
    # 1. Clean the incoming question
    cleaned_question = utils.clean_text(question)

    # 2. Retrieve relevant context using RAG
    context = rag.retrieve_context(question)

    # 3. Formulate an answer
    answer = f"Generated answer for '{cleaned_question}' based on: [{context}]"

    # 4. Save the question and answer to the database
    database.save_chat(question, answer)

    return answer
