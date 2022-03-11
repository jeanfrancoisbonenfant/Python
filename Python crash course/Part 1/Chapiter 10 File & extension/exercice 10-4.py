filename = 'text/guest_boot.txt'

print("Enter quit at any moment to leave.")
while True:
    name = input("What is your name? ")
    if name == "quit":
        break
    else:
        print(f"Welcome {name} you have been added to our guests record.")
        with open(filename, "a") as file_object:
            file_object.write(name)
            file_object.write("\n")


with open(filename) as file_object:
    content = file_object.read()

print(content)