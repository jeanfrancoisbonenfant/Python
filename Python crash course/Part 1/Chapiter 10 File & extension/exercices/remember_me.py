import json

#Load the username, if it had been stored previously
#   Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("What is your username: ")

    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will try to remember you {username.title()}.")

else:
    print(f"Welcome back, {username.title()}!")