cities = {
    "Berlin" : {
        "country" : "germany",
        "population" : 3_645_000,
        "Fun fact" : "I have never been to Berlin"
        },
    "Vancouver" : {
        "country" : "canada",
        "population" : 675_000,
        "Fun fact" : "Too expensive to live in"
        },
    "Denver" : {
        "country" : "united states",
        "population" : 705_000,
        "Fun fact" : "The only city I have visited in the states"
        }
    }

for city, city_info in cities.items():
    print(f"Have you ever heard of {city}?")
    
    country = city_info["country"]
    population = city_info["population"]
    fun_fact = city_info["Fun fact"]
    
    print(f"\nHere are some interesting information about {city.title()}:")
    print(f"\tCountry : {country.title()}")
    print(f"\tPopulation : {population}")
    print(f"\tFun fact : {fun_fact}")