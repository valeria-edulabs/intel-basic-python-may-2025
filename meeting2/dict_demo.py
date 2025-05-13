from pprint import pprint

my_dict = {
    1: "January",
    2: "February",
    3: "March"
}

# print(my_dict[3])

# print(my_dict[1])
countries = {
    "US": "Washington",
    "Israel": "Jerusalem"
}
print(countries["US"])
print(countries)
#
countries["France"] = "Paris"
print(countries)
countries["Israel"] = "Tel Aviv"
print(countries)

currencies = {
    "USD": 3.7,
    "EURO": 3.9,
    "USD": 4.0
}
#
person1 = {
    "first_name": "Valeria",
    "last_name": "Aynbinder",
    "id": "111111118",
    "bday": "11-02-87",
    "byear": 1987
}
#
person2 = {
    "first_name": "Zvi",
    "last_name": "Yakir",
    "id": "222222223",
    "bday": "21-12-80",
    "byear": 1980
}
#
persons = [
    person1,
    person2
]
#
print(persons)
#
for p in persons:
    print(p["first_name"])
    p["age"] = 2025 - p["byear"]

pprint(persons)
#
# print(persons[1]["age"])
# for p in persons:
#     print(p["age"])
#


persons_dict = {}
# persons_dict["1234568"] = {"name": "Val", "age": 38}
for p in persons:
    persons_dict[p["id"]] = p

pprint(persons_dict)
#
#
# print("France" in countries)

print(persons_dict["222222223"]["first_name"])