import unittest
from city_function import city_formated

class CityTestCase(unittest.TestCase):
    """ Test for 'city_formated function' """

    def test_city_country(self):
        """ Testing for city, country format """
        formated_city = city_formated("calgary", "canada")
        self.assertEqual(formated_city, "Calgary, Canada.")

    def test_city_country_population(self):
        """ Testing for city, country - population format"""
        formated_city = city_formated("calgary", "canada", "1 336 000")
        self.assertEqual(formated_city, "Calgary, Canada - population 1 336 000.")

if __name__ == '__main__':
    unittest.main()
