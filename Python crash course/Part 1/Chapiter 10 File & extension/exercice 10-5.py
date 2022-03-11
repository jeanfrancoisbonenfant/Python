filename = 'text/programming_poll.txt'

print("Enter quit at any moment to leave.")
while True:
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        print("Have a good day!", "\n")
        break
    else:
        print("Thanks you for answering the poll.\n")
        with open(filename, "a") as file_object:
            file_object.write(reason)
            file_object.write("\n")

with open(filename) as file_object:
    content = file_object.read()

print(content.rstrip())