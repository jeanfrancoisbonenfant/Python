def make_sandwich(*ingredients):
    print("Your sandwich will contain: ")
    for ingredient in ingredients:
        print(f"\t- {ingredient.title()}")


make_sandwich("cheeze", 'smoked meat', 'peperonni', 'cheezewiz', 'tomato')
