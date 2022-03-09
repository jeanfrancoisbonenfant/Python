from user import User
from privilege import Privileges, Administrator

admin = Administrator("Danielle", "Senneville")
print(admin.privileges.show_privilege())