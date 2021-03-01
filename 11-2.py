#11-2
import unittest
from city_functions import show_city
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        res = show_city('chengdu','china')
        self.assertEqual(res,'chengdu,china')
    def test_city_country_population(self):
        infor1 = show_city('shanghai','china','10000')
        self.assertEqual(infor1,'shanghai,china-population 10000')
if __name__ == '__main__':
 unittest.main()