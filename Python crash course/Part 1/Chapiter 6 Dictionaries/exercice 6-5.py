geography = {
    "nile" : "Egypt",
    "St-lawrance" : "Canada",
    "Mississipi" : "USA",
    }

for river, country in geography.items():
    print(f"The {river.title()} is a river that run through {country.title()}.","\n")
    
for river in geography:
    print(river.title(),"\n")
    
for country in geography.values():
    print(country.title(),"\n")