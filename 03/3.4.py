# 1
number = int(input())
if number % (3 * 5) == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


# 2
a, b, c = (int(input()) for _ in range(3))
if a == b and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)


# 3
print(
    (
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
    )[int(input()) - 1]
)


# 4
age = int(input())
match age:
    case age if age < 2:
        print("Младенец")
    case age if age < 4:
        print("Малыш")
    case age if age < 12:
        print("Ребенок")
    case age if age < 19:
        print("Подросток")
    case age if age < 65:
        print("Взрослый человек")
    case _:
        print("Пожилой человек")


# 5
operand_a, operand_b, operator = (input() for _ in range(3))
match operator:
    case "+" | "-" | "*" | "/":
        try:
            eval(f"print({operand_a} {operator} {operand_b})")
        except ZeroDivisionError:
            print("Неизвестно")
    case _:
        print("Неизвестно")


# 6
password_a, password_b = (input() for _ in range(2))
if len(password_a) < 7:
    print("Short")
elif password_a != password_b:
    print("Difference")
else:
    print("OK")
