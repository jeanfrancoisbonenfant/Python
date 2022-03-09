from user import User

class Privileges:
    """Initialize separate Privilege class """
    def __init__(self):
        self.privilege = ["Can add post", "can delete post", "can ban user"]

    def show_privilege(self):
        """ Return list of privileges """
        return self.privilege


class Administrator(User):
    """ Initialize subclass of User
        Add privileges attribute from Privilege class
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()