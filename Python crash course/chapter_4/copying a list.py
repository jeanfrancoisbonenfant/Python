my_foods = ['pizza', 'falafel', 'carrot cake']

# copy my_food list to friend_foods list
# [:] slice the list from each other
friend_foods = my_foods[:]

print(my_foods)

print("\n My friend's like:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)

print("\n My friend's like:")
print(friend_foods)