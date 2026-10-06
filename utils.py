"""
utils.py - General helper functions.
"""

def clean_text(text: str) -> str:
    """Cleans text by stripping whitespace and converting to lowercase."""
    return text.strip().lower()
