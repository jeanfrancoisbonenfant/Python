from time import sleep

sandwich_orders = ["tuna", "chicken", "pastrami", "ham", "chicken"]
new_order = ["pastrami", "rosbeef", "pastrami"]

for sandwich in new_order:
    sandwich_orders.append(sandwich)

finished_sandwich = []
print("We have to advise you that we ran out of pastrami.")

while sandwich_orders:
    current_sandwich = sandwich_orders[0]
    sandwich_orders.pop(0)

    if current_sandwich == "pastrami":
        continue
    print(f"I have made your {current_sandwich} sandwich.\n")
    finished_sandwich.append(current_sandwich)
    sleep(2)

print("All sandwiches are completed: ")
for sandwich in finished_sandwich:
    print(f"\t{sandwich}")
