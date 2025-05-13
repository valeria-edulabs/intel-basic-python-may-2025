cities = ("Tel Aviv", "Kiryat Gat", "Netanya")
for city in cities:
    print(city)

for char in "Intel":
    print(char)

for i in range(10, 0, -1):
    print(i)

# r = range(2, 20, 2)

# for i in 10:
#     print(i)

counter = 1
for city in cities:
    print(f"city {counter}: {city}")
    counter +=1

for i, city in enumerate(cities):
    print(f"city {i}: {city}")

countries = ["Israel", "France", "Germany"]
capitals = ["Jerusalem", "Paris", "Berlin"]
temperatures = [25, 15]

# for i in range(len(countries)):
#     print(countries[i], capitals[i], temperatures[i])

for coutry, city, t in zip(countries, capitals, temperatures):
    print( coutry, city, t)

# a, b = [1, "tttt"]
