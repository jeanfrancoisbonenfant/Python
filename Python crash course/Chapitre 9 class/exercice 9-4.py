class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is currently open.")

    def set_number_served(self, count):
        """ Update served total count when used"""
        self.number_served = count

    def increment_number_served(self, increment):
        self.number_served += increment


my_restaurant = Restaurant("pizza 73", "pizzeria")
print(my_restaurant.number_served)

my_restaurant.number_served = 100
print(my_restaurant.number_served)

my_restaurant.set_number_served(666)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(6303)
print(my_restaurant.number_served)
