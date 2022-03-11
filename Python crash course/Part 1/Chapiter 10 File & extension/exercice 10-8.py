filenames = ["text/cat.txt", "text/dog.txt"]

for filename in filenames:
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.readlines()

    except FileNotFoundError:
        print()
        print(f"Error {filename} was not found.\n")

    else:
        print(f"Here is the content of {filename}:")
        for name in content:
            print("\t", "-", name.title().strip())
        print()