print("Enter quit to leave at any moment. \n")
while True:
    try:
        number_1 = input("Please enter a number: ")
        if number_1 == "quit":
            print("Have a good day!")
            break
        else:
            number_1 = int(number_1)
        number_2 = input("Please enter a second number: ")
        if number_2 == "quit":
            print("Have a good day!")
            break
        else:
            number_2 = int(number_2)
    except ValueError:
        print()
        print("You have to enter a number.\n")
        continue
    else:
        somme = number_1 + number_2
        print(f"The somme of {number_1} + {number_2} equals to {somme}.")
