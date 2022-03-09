def make_shirt(text="I love python", size="large"):
    print(f"We are currently making your {size} shirt.\n")
    print("Message to be printed on:")
    print(f"\t {text}.\n")


make_shirt()
make_shirt(size="medium")
make_shirt("C++ is much harder", "small")
