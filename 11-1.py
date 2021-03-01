#11-1
import unittest
from city_functions import show_city
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        res = show_city('chengdu','china')
        self.assertEqual(res,'chengdu,china')
if __name__ == '__main__':
 unittest.main()