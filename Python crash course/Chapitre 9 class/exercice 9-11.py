from user import User
from privilege import Privileges, Administrator

admin =  Administrator("Brigitte", "Lavoie")
print(admin.privileges.show_privilege())