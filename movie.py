"""Implement movies stuff."""
from typing import Collection
from dataclasses import dataclass

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self) -> str:
        """Get the title."""
        return self.title

    def is_genre(self, genre: str) -> bool:
        """Check if the Movie has that genre."""
        return genre in self.genre

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
