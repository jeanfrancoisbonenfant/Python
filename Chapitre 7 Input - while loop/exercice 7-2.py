group_size = int(input("How many people will join you for diner? "))

if group_size >= 8:
    print("Their will be delay for a table of that size.")
elif group_size < 8:
    print("Table is ready please follow me.")