def city_formated(city,country, population=""):
    if population:
        formated = f"{city.title()}, {country.title()} - population {population}."
        return formated
    elif not population:
        formated = f"{city.title()}, {country.title()}."
        return formated