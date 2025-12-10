"""User-facing error types and helpers."""

class UserInputError(Exception):
    """Raised for invalid user input in CLI flows."""


def format_error(message: str) -> str:
    return message.strip() or "Something went wrong. Please try again."
