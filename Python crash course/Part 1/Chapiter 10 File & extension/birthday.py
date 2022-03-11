filename = 'text/pi_million_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()

pi_string = ""
for line in contents:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("You birthday doesn't appear in the first million digits of pi.")