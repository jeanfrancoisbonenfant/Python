class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.single = True
        self.date_count = 0
        self.login_attempt = 0

    def describe_user(self):
        print(
            f"{self.first_name} {self.last_name} has {self.date_count} dates.")

    def greet_user(self):
        print("Welcome {self.first_name} {self.last_name}!")

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


bob = User("bob", "marley")
bob.increment_login_attempt()
print(bob.login_attempt)

bob.reset_login_attempt()
print(bob.login_attempt)
