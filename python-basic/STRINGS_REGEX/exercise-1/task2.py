city = 'berlin'

population = 3645000

print(city.capitalize()+': '+str(population))

print(f"{city.capitalize()} has the population of: {population}")

print("{}: {}".format(city.capitalize(), population))

print("%s: %d" % (city.capitalize(), population))