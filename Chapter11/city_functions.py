
def city_country(city, country, population=30000):
    return city.title() + ", " + country.title() + ": Population " \
        + str(population)


print(city_country("buffalo", "ny"))