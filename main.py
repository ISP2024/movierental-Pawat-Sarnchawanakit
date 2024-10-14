# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
import pricing


def make_movies():
    """Some sample movies."""
    movies = [
        (Movie(title="Air", year=2023, genre=("Drama", "Sports")), pricing.NEW_RELEASE),
        (Movie(title="Oppenheimer", year=2023, genre=("Biography", "Drama", "History")), pricing.REGULAR),
        (Movie(title="Frozen", year=2013, genre=("Animation", "Adventure", "Comedy", "Family", "Fantasy")), pricing.CHILDRENS),
        (Movie(title="Bitconned", year=2022, genre=("Comedy", "Drama")), pricing.NEW_RELEASE),
        (Movie(title="Particle Fever", year=2013, genre=("Documentary", "Science")), pricing.REGULAR)
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
