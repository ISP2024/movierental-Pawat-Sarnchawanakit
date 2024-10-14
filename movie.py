"""Implement movies stuff."""

class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str):
        """Initialize a new movie."""
        self.title = title

    def get_title(self) -> str:
        """Return the title."""
        return self.title

    def __str__(self) -> str:
        return self.title
