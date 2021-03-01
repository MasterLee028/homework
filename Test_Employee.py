import unittest
from Employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_money = Employee('lee','tom',1000)
    def test_give_default_raise(self):
        infor = self.my_money.give_raise()
        self.assertEqual(infor,6000)
    def test_give_custom_raise(self):
        infor1 = self.my_money.give_raise(2000)
        self.assertEqual(infor1,3000)
if __name__ == '__main__':
 unittest.main()
