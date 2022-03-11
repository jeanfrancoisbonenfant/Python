from distutils.command.build_scripts import first_line_re


people = {
    'person_01' : {
        "first_name" : "Brigitte",
        "last_name" : "Lavoie",
        "age" : 38,
        "city": "Calgary",
        },

    'person_02' : {
        "first_name" : "Jean-Francois",
        "last_name" : "Bonenfant",
        "age" : 32,
        "city": "Calgary",
        },

    'person_03' : {
        "first_name" : "Danielle",
        "last_name" : "Senneville",
        "age" : 59,
        "city": "Mirabel",
        },
}

for person, person_info in people.items():
    print(f"Our next subject {person}:")
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    age = person_info["age"]
    city = person_info["city"]
    print(f"\tName: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tFrom: {city.title()}\n")