def make_album(name, title):
    dictionnary = {"artist": name.title(), "album": title.title()}
    return dictionnary


print("Enter q at any moment to quit \n")
while True:
    name = input("Enter artist name: ")
    if name == "q":
        break
    album = input("Enter album title: ")
    if album == "q":
        break
    requested_album = make_album(name, album)
    print(requested_album)
