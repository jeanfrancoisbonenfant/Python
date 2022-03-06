message = "If you could visit one place in the world, "
message01 = "Where would you go? "
message += message01
dream_destination = input(message)

dream = True

while dream:
    if dream_destination.lower() == "montreal":
        print("LOL you are funny!\n")
        break
    print(f"{dream_destination.title()} what a lovely place.\n")
    more = input("Do you have any other dream destination? Yes or No: ")
    if more.lower() == "yes":
        dream_destination = input(message01)
        continue
    elif more.lower() == "no":
        dream = False
