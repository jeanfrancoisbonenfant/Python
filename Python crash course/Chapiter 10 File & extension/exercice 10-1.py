filename = 'text/learning_python.txt'

#retrieve and print all content at once
with open(filename) as file_object:
    contents = file_object.read()

print(contents,"\n")
#retrive list of line of content
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines: #loop through list and print them
    print(line.strip())
print()

text = ""
for line in lines: #loop through list and add line to for a text
    text += line.strip()
print(text)
