favorite_place = {
    "Brigitte" : ["Calgary", "Blanc Sablon", "Thailand"],
    "Jean-Francois" : ["Vancouver", "Thailand", "Philippine"],
    "Danielle" : ["Mirabel", "Calgary", "Cuba"]
    }

for name, list in favorite_place.items():
    if list:
        print(f"{name} favorite vacation destinations are:")
        for place in list: 
            print("\t",place)
    print()