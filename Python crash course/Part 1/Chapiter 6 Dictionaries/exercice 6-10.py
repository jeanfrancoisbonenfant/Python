favorite_number = {
    "Jean-Francois" : [89, 772, 578],
    "Brigitte" : [5, 1, 3, 55, 55555],
    "Danielle" : [12, 0],
    "Joannie" : [3, "de quoi tu parle"],
    "Louka" : [69],
    }

for key, list in favorite_number.items():
    print(f"{key} favorite number is:")
    for number in list:
        print('\t',number)