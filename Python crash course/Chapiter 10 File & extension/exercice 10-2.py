filename = 'text/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    message = line.replace('python', 'C')
    print(message)
