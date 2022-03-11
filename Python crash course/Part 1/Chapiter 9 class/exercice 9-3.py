class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.single = True
        self.date_count = 0

    def describe_user(self):
        print(
            f"{self.first_name} {self.last_name} has {self.date_count} dates.")

    def greet_user(self):
        print("Welcome {self.first_name} {self.last_name}!")

        """
        To be continue..
        trying to use disctionary of users
        to create new instance of User class
        """


users = {
    "jeff": {
        "first name": "jeff",
        "last name": "bonenfant",
        "single status": False,
        "date count": 0,
        },
    "brigitte": {
        "first name": "brigitte",
        "last name": "lavoie",
        "single status": False,
        "date count": 10,
        },
    }
