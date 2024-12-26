# 1
ages = {"Jim": 30, "Pam": 28, "Kevin": 33}
person = input()
age = ages.get(person)

if age:
    print(f"{person} is {age} years old.")
else:
    print(f"{person}'s age is unknown.")


# 2
data = input()
if data.isdigit():
    number = int(data)
    print(number)
else:
    print("Введенные данные не могут быть преобразованы в число")

# 2
try:
    print(int(input()))
except ValueError:
    print("Введенные данные не могут быть преобразованы в число")
