pets = {
    'Roxy' : {
        "race" : "Pincher",
        "owner" : "Brigitte",
        "age" : 13,
        },
    'Zeus' : {
        "race" : "Boston Terrier",
        "owner" : "Jean-Francois",
        "age" : 9,
        },
    'Brutus' : {
        "race" : "Pug",
        "owner" : "Wilbrod",
        "age" : 15,
        },
    'Newton' : {
        "race" : "dashong",
        "owner" : "Brigitte & Jean-Francois",
        "age" : 3,
        },
    }

for name, dog_info in pets.items():
    print(f"Next dogs to be presented: {name}")
    race = dog_info["race"]
    owner = dog_info["owner"]
    age = dog_info["age"]
    print(f"\t{name} is a {race} presented by it owner's {owner}.")
    print(f"\t{name} is only {age} years old.\n")