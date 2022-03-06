class Restaurant:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} is currently open.")


class IceCreamStand(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ["Vanilla", "Chocolate", "Bubble gum", "Coton Candy"]

    def display_flavors(self):
        print(f"Available flavors : {self.flavors}")


marble_slab = IceCreamStand("marble_slab", "ice cream shop")
marble_slab.display_flavors()
