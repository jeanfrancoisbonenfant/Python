from pprint import pprint
from re import T

#initial list creation
motorcycle = ["honda", "suzuki", "yamaha"]
print(motorcycle)

# list index[0] modification
motorcycle[0] = "ducati"
print(motorcycle)

# list adding
motorcycle.append("honda")

print()
print(motorcycle)

#new list creation
programming = []

#list appending item
programming.append("python")
programming.append("javascript")
programming.append("Java")

#print new list result
print()
print(programming)

# index[0] insertion
programming.insert(0, "C++")
programming.insert(2,"C")

print()
print(programming)

#removing from list
del programming[0]
print()
print(programming)

""" pop() function to use removed item afterward
*** always remove last item from list by default"""
popped_programming = programming.pop()

print()
print(programming)
print(popped_programming)

#using pop to remove specific index
next_programming = programming.pop(1)

print()
print(f"The programming I have basic knowledge are: {programming[0]} and {programming[-1]}")
print(f"The next programming languige I will lean will be: {next_programming}")


print()
print(motorcycle)

#removing from list by value name

favorite = "ducati"
motorcycle.remove(favorite)

print()
print(motorcycle)
print(f"\nA have a preferance for {favorite.title()}.")