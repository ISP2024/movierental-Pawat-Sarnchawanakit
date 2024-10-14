"""Implement movies stuff."""
from pricing import PriceStrategy, NewRelease, RegularPrice, ChildrensPrice

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
