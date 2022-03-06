from time import sleep

message = "Welcome to nightmare movie theatre.\n"
message += "How many tickets do you need?"

count = int(input(message))
price = 0
while count > 0:
    age = input("Enter age of the customer: ")
    if age == "quit":
        break
    age = int(age)
    print()
    if age > 200:
        print("This is not possible")
        break

    if age < 3:
        print("Ticket is free for this customer.")
        count -= 1
        continue
    elif age <= 12:
        print("This customer will have to pay $10.")
        count -= 1
        price += 10
        continue
    elif age > 12:
        print("General admission is $15.")
        count -= 1
        price += 15
        continue
print(f"Grand total: ${price} please.\n")
sleep(3)
print("Thank you! have a good movie.")
