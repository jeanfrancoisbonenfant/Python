city = ["calgary", "reyjavik", "new york"]
country = ["canada", "iceland", "united states"]


def city_country(city, country):
    formatted = (f'"{city.title()}, {country.title()}"')
    return formatted


"""
function doesn't work

def print_list(list01, list02):
    for city in list01:
        for country in list02:
            message = city_country(city, country)
    print(message)
"""

message = city_country("calgary", "canada")
print(message)
print()
print()
# print_list(city, country)
