class User:

    def __init__(self, first_name, last_name):
        """ Initialize User class and attribute """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0

    def describe_user(self):
        """ Print user description message. """
        print(
            f"{self.first_name} {self.last_name} has {self.date_count} dates.")

    def greet_user(self):
        """ Print greetings to user."""
        print("Welcome {self.first_name} {self.last_name}!")

    def increment_login_attempt(self):
        """ Method increment login count """
        self.login_attempt += 1

    def reset_login_attempt(self):
        """ Method to reset login count """
        self.login_attempt = 0
