class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is currently open.")


my_restaurant = Restaurant("Pizza 73", "pizzeria")
print(my_restaurant.name)
print(my_restaurant.type)
