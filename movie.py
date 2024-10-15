"""Implement movies stuff."""
import datetime
from typing import Collection, Optional, Generator
from dataclasses import dataclass
import logging
import pricing


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

    def price_code_for_movie(self) -> pricing.PriceStrategy:
        """Get price code for movie."""
        if self.year == datetime.datetime.now().year:
            return pricing.NEW_RELEASE
        if self.is_genre("Children") or self.is_genre("Childrens"):
            return pricing.CHILDRENS
        return pricing.REGULAR

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"


class MovieCatalog:
    """Contains movie data."""

    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "movies"):
            return
        self.movies: dict[str, list[Movie]] = dict()
        self.file = open("movies.csv", "r", encoding="UTF-8")
        def new_movies_generator() -> Generator[Movie, None, None]:
            """Read from file to get more movies."""
            for count, line in enumerate(self.file, 1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                if stripped_line[0] == '#':
                    continue
                values = [val.strip() for val in stripped_line.split(',')]
                if len(values) != 4:
                    logging.error("Line %d: Unrecognized format \"%s\"", count,
                                stripped_line)
                    continue
                arr = self.movies.get(values[1])
                if arr is None:
                    arr = []
                    self.movies[values[1]] = arr
                try:
                    year = int(values[2])
                except ValueError:
                    logging.error("Line %d: Unrecognized format \"%s\"", count,
                                stripped_line)
                    continue
                movie = Movie(values[1], year,
                            [genre.strip() for genre in values[3].split('|')])
                arr.append(movie)
                yield movie
        self.new_movies = new_movies_generator()

    def __del__(self):
        self.file.close()

    def get_movie(self, title: str, year: int = None) -> Optional[Movie]:
        """Get a movie from the catalog."""
        possible_movies = self.movies.get(title)
        if possible_movies is None:
            return next(
                (movie for movie in self.new_movies if movie.title == title),
                None)
        if year is None:
            return possible_movies[0]
        return next((movie for movie in possible_movies if movie.year == year),
                    None) or next(
                        (movie for movie in self.new_movies
                         if movie.title == title and movie.year == year), None)
