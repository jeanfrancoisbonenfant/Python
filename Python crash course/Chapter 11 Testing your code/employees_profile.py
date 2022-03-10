class Employee:
    """ Attempt to create an employee"""
    def __init__(self,first_name, last_name, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """ Method raise employee salary by default or custom amount."""
        self.salary += amount
