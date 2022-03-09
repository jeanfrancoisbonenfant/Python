
#creation of TUPLE (immuable list) that can't be changed
dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
#Presence of , is mandatory for defining Tuple
beer = ("richards",)

#Tuple can be redefined!!
dimensions = (400, 100)

print()
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)