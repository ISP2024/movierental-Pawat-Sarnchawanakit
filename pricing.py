"""Implements pricing strategies."""
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


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDRENS = ChildrensPrice()
