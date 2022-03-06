current_users = ["venoma", "bay", "yoki", "blackbeard", "bombay"]

username = input("Please enter you username:")

if username:
    for user in current_users:
        if username.lower() == user:
            print("Username unavailable please try again.")
            username = input("Please enter username:")
            username = username.lower()

current_users.append(username)
print(f"Welcome {username}, you have been registered.")

print(current_users)

#some issues are left code easy to break