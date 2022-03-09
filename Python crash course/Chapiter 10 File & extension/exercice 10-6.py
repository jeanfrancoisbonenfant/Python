
try:
    number_1 = int(input("Please enter a number: "))

except ValueError:
    print("You have to enter a number.")

else:
    try:
        number_2 = int(input("Please enter a second number: "))

    except ValueError:
        print(f"You have to enter a number.")

    else:
        somme = number_1 + number_2
        print(f"The somme of {number_1} + {number_2} equals to {somme}.")


