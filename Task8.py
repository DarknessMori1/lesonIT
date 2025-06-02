def cities_information(s: str) -> tuple:
    return s, len(s)

cities = input().split()
d = {city: cities_information(city)[1] for city in cities}

for city in sorted(d, key=d.get):
    print(f"'{city}': {d[city]}")пше