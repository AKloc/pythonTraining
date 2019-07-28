import unittest
from city_functions import city_country

class CityFunctionsTests(unittest.TestCase):
    def test_city_country(self):
        result = city_country("buffalo", "ny")
        self.assertEquals("Buffalo, Ny: Population 30000", result)

    def test_city_country_population(self):
        result = city_country("akron", "oh", 5000)
        self.assertEquals("Akron, Oh: Population 5000", result)

    # This runs before any of the other test methods, as you'd expect.
    def setUp(self):


# Don't forget this part.
unittest.main()