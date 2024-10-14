"""Implement rental stuff."""
from movie import Movie
from pricing import PriceStrategy


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie: Movie, price_code: PriceStrategy, days_rented: int):
        """Initialize a new movie rental object for
            a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        """Get the price strategy."""
        return self.price_code

    def get_movie(self) -> Movie:
        """Get the moving being rented."""
        return self.movie

    def get_days_rented(self) -> int:
        """Get number of days rented."""
        return self.days_rented

    def get_price(self) -> float:
        """Return the price."""
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self) -> int:
        """Return the rental points."""
        return self.price_code.get_rental_points(self.days_rented)
