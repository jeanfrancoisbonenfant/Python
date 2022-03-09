username = ["admin", 'venoma', "bay", 'Yuki', "Baltazzar"]

if username:
    for user in username:
        
        if user == "admin":
            print(f"Hello {user.title()}!, would you like to see a status report?")
        else:
        
            print(f"Welcome {user.title()}, thank you for logging in again.")
else:
    print("Please enter a username.")