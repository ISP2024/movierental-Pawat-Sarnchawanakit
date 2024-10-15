"""Implements tests for pricing."""
from unittest import TestCase
from movie import Movie
import pricing


class PricingTest(TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Set up movies."""
        self.new_movie = Movie(title="Mulan",
                                year=2024,
                                genre=("Animation", "Adventure", "Family"))
        self.regular_movie = Movie(title="CitizenFour",
                                    year=2014,
                                    genre=("Documentary", "Biography",
                                           "Thriller"))
        self.childrens_movie = Movie(title="Frozen",
                                      year=2013,
                                      genre=("Children", "Animation", "Adventure",
                                             "Comedy", "Family", "Fantasy"))

    def test_new_movie(self):
        """Test pricing for new movie."""
        self.assertEqual(self.new_movie.price_code_for_movie(), pricing.NEW_RELEASE)

    def test_regular_movie(self):
        """Test pricing for new movie."""
        self.assertEqual(self.regular_movie.price_code_for_movie(), pricing.REGULAR)

    def test_children_movie(self):
        """Test pricing for new movie."""
        self.assertEqual(self.childrens_movie.price_code_for_movie(), pricing.CHILDRENS)
