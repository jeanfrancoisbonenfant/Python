import unittest
from employees_profile import Employee

class TestEmployees_profile(unittest.TestCase):
    """ Test for class Employee. """

    def setUp(self):
        self.my_employee = Employee("Jean-Francois", "Bonenfant", 200000)

    def test_give_default(self):
        """ Test give_raise default value. """
        self.my_employee.give_raise()
        self.assertEqual(205000, self.my_employee.salary)

    def test_give_custome(self):
        """ Test give_raise custome value. """
        self.my_employee.give_raise(100000)
        self.assertEqual(300000, self.my_employee.salary)


if __name__ == "__main__":
    unittest.main()

