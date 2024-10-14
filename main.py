# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
import pricing


def make_movies():
    """Some sample movies."""
    movies = [
        (Movie("Air"), pricing.NEW_RELEASE),
        (Movie("Oppenheimer"), pricing.REGULAR),
        (Movie("Frozen"), pricing.CHILDRENS),
        (Movie("Bitconned"), pricing.NEW_RELEASE),
        (Movie("Particle Fever"), pricing.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(*movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
