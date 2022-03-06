favorite_pizzas = ["all dress", "buffalo", "hawaienne"]

friend_pizza = favorite_pizzas[:]

favorite_pizzas.append("shawarma")

friend_pizza.append("vegan")

print("My favorite pizza are:","\n")
for pizza in favorite_pizzas[1:]:
    print(pizza)
print()

print("My friend's favorite pizza are:",'\n')
for pizza in friend_pizza[-3:]:
    print(pizza,'\n')