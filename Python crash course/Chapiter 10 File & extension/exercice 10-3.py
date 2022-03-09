filename = "text/guest.txt"

name = input("What is your name? ")

with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename) as file_object:
    content = file_object.read()

print(content)