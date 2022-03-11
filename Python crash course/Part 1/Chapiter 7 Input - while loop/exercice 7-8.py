from time import sleep

sandwich_orders = ["tuna", "chicken", "ham", "chicken", "rosbeef"]
finished_sandwich = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich} sandwich.\n")
    finished_sandwich.append(current_sandwich)
    sleep(2)
print("All sandwiches are completed: ")
for sandwich in finished_sandwich:
    print(f"\t{sandwich}")
