import unittest
from rental import Rental
from movie import Movie
import pricing


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = (Movie(title="Dune: Part Two", year=2023, genre=("Science Fiction", "Adventure", "Drama")), pricing.NEW_RELEASE)
        self.regular_movie = (Movie(title="Air", year=2023, genre=("Drama", "Sports")), pricing.REGULAR)
        self.childrens_movie = (Movie(title="Frozen", year=2013, genre=("Animation", "Adventure", "Comedy", "Family", "Fantasy")), pricing.CHILDRENS)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie(title="Air", year=2023, genre=("Drama", "Sports"))
        self.assertEqual("Air", m.title)
        self.assertEqual("Air (2023)", str(m))

    def test_rental_price(self):
        rental = Rental(*self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(*self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(*self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

    def test_rental_points(self):
        rental = Rental(*self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(*self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
