# 1
d1 = {"a": 100, "b": 200, "c": 333}
d2 = {"x": 300, "y": 200, "z": 777}
d2 |= d1
d2.update(d1)
print(d2)


# 2
db = {}
for _ in range(int(input())):
    name = input()
    if name in db:
        i = 1
        while f"{name}{i}" in db:
            i += 1
        db[f"{name}{i}"] = name
        print(f"{name}{i}")
    else:
        db[name] = name
        print("OK")


# 3
countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"],
}
city = input()
for country, cities in countries.items():
    if city in cities:
        print(f"INFO: {city} is a city in {country}")
        break
else:
    print(f"ERROR: Country for {city} not found")


# 4
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
}
user["secret"] = user.pop("password")
user["surname"] = user.pop("last_name")


# 5
*keys, key, value = [int(key) for key in input().split()]
result = {key: value}
for key in reversed(keys):
    result = {key: result}
print(result)
