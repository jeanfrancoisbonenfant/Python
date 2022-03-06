multiple_ten = int(input("Please enter a number here: "))

if multiple_ten % 10 == 0:
    print(f"{multiple_ten} if a multiple of 10.")
elif multiple_ten % 10 != 0:
    print(f"{multiple_ten} is not a multiple of 10.")