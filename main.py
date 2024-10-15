# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer
import pricing


def make_movies():
    """Some sample movies."""
    movies = [
        Movie(title="Air", year=2024, genre=("Drama", "Sports")),
        MovieCatalog().get_movie("Oppenheimer"),
        Movie(title="Frozen", year=2013, genre=("Children", "Animation", "Adventure", "Comedy", "Family", "Fantasy")),
        MovieCatalog().get_movie("Bitconned"),
        MovieCatalog().get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
