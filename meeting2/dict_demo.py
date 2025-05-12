import datetime
import pprint

my_dict = {
    1: "January",
    2: "February"
}

print(my_dict[1])
countries = {
    "Israel": "Jerusalem",
    "US": "Washington"
}
print(countries["US"])

countries["France"] = "Paris"
print(countries)
countries["Israel"] = "Tel Aviv"
print(countries)

person1 = {
    "first_name": "Valeria",
    "last_name": "Aynbinder",
    "id": "111111118",
    "bday": "11-02-87",
    "byear": 1987
}

person2 = {
    "first_name": "Zvi",
    "last_name": "Yakir",
    "id": "222222223",
    "bday": "21-12-80",
    "byear": 1980
}

persons = [
    person1,
    person2
]

print(persons)

for p in persons:
    print(p["first_name"])
    p["age"] = 2025 - p["byear"]

print(persons[1]["age"])
for p in persons:
    print(p["age"])

persons_dict = {}
for p in persons:
    persons_dict[p["id"]] = p

pprint.pprint(persons_dict)

print("France" in countries)