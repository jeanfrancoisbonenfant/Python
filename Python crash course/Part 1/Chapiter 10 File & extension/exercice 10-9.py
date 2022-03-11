filenames = ["text/cat.txt", "text/dog.txt"]    #list file with animals name

for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.readlines() #read & make list of name from file

    except FileNotFoundError:   #Silent error
        pass

    else:
        print(f"Here is the content of {filename}:")
        for name in content:    #loop list to retrieve individual name and style them
            print("\t", "-", name.title().strip())
        print()