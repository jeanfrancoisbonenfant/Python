glossary = {
    "variable" : "container for something",
    "if statement" : "conditional statement",
    "for loop" : "loop that run for some time",
    "boolean" : "true or false",
    "list" : "container of a series of things",
    "while loop" : "is a loop that stop when false",
    "dictionnary" : "is a collective of pair of key and value",
    "in statement" : "used to verify in something is part of something else",
    "key()" : "is a function used to retrieve keys for a dictionnary",
    "value()" : "is a function used to retrieve value for a dictionary",
}
count = 0
for key, value in glossary.items():
    print(f"A {key} is a {value}.\n")
    count += 1
print(count)