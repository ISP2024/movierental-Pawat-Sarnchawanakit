import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
import pricing


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
        
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
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

    @unittest.skip("No convenient way to test")
    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        pass

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_get_total_charge(self):
        c = Customer("Movie Mogul")
        self.assertEqual(0.0, c.get_total_charge())
        c.add_rental(Rental(self.new_movie, 4))  # days
        self.assertEqual(12.0, c.get_total_charge())

    def test_get_total_rental_points(self):
        c = Customer("Movie Mogul")
        self.assertEqual(0, c.get_total_rental_points())
        c.add_rental(Rental(self.new_movie, 4))  # days
        c.add_rental(Rental(self.regular_movie, 3))  # days
        self.assertEqual(5, c.get_total_rental_points())
