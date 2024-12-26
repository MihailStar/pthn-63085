# 1
my_dict = {}
print(my_dict)


# 2
person = {"name": "Vasya", "surname": "Petrov", "age": 25}
print(person)


# 3
sweet = {"id": "0001", "type": "donut", "name": "Cake", "ppu": 0.55, "calories": 125}
print(sweet["name"])
print(sweet["calories"])
print(sweet["id"])


# 4
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days[int(input()) - 1])


# 5
sweet = {"id": "0001", "type": "donut", "name": "Cake", "ppu": 0.55, "calories": 125}
sweet["weight"] = 230
sweet["have_topping"] = True
sweet["name"] = "SuperCake"
sweet["calories"] = 350
print(sweet)


# 6
sweet = {"id": "0001", "type": "donut", "name": "Cake", "ppu": 0.55, "calories": 125}
del sweet["ppu"]
del sweet["type"]
print(sweet)


# 7
print({n: n**2 for n in range(1, int(input()) + 1)})


# 8
from string import ascii_lowercase
alphabet = {char: index + 1 for index, char in enumerate(ascii_lowercase)}
print(alphabet)
