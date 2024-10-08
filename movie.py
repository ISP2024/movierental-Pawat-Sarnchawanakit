"""Implement movies stuff."""
from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""


class NewRelease(PriceStrategy):
    """Price strategy for new releases."""

    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return days


class RegularPrice(PriceStrategy):
    """Regular price strategy."""

    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return 1


class ChildrensPrice(PriceStrategy):
    """Price strategy for new children."""

    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        return 1


class Movie:
    """
    A movie available for rent.
    """

    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title: str, price_code: PriceStrategy):
        """Initialize a new movie."""
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        """Get the price strategy."""
        return self.price_code

    def get_title(self) -> str:
        """Return the title."""
        return self.title

    def __str__(self) -> str:
        return self.title

    def get_rental_points(self, days: int) -> int:
        """Return the rental points.

        Arguments:
            days -- The number of days rented.

        Returns:
            The rental points
        """
        return self.price_code.get_rental_points(days)

    def get_price(self, days: int) -> float:
        """Return the price.

        Arguments:
            days -- The number of days rented.

        Returns:
            The price.
        """
        return self.price_code.get_price(days)
