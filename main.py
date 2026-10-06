"""
main.py - Entry point of the my-ai-app application.
"""

import chatbot


def main() -> None:
    """Executes the application flow by asking a question through the chatbot."""
    user_query = "What is Artificial Intelligence?"
    print(f"[Main] Starting process with query: '{user_query}'\n")

    response = chatbot.ask_question(user_query)

    print(f"\n[Main] Response received:\n{response}")


if __name__ == "__main__":
    main()
