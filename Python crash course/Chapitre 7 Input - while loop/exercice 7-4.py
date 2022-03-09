from time import sleep


toppings = []

ordering = True
message = "Welcome to Calgary's best pizza!"
print("\n" + message)
while ordering:
    order = input("Please enter desired toppings: ")
    toppings.append(order)
    print(f"{order.title()} will be added to your pizza. Anything else?")
    more = input("Enter yes or no: ")
    if more.lower() == "no":
        ordering = False
    elif more.lower() == "yes":
        continue
    else:
        print("Wrong commend entered")
        continue
print("Understood! you pizza will be filled with:")
for topping in toppings:
    print(f"\t{topping}")
sleep(1)
print()
print("Your pizza is in the oven.")
sleep(2)
print("...")
sleep(3)
print("Your pizza is ready!"+"\n")
