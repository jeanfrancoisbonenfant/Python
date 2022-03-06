class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
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


class Administrator(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege = ["Can add post", "can delete post", "can ban user"]

    def show_privilege(self):
        return self.privilege


admin = Administrator("jeff", "bonenfant")
print(admin.show_privilege())
