# 1
import os
print(os.name)


# 2
import os
print(os.environ["HOME"])


# 3
from string import Template
values = {"one": "Привет", "copter": "Квадракоптер"}
t = Template("""
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
""")
print(t.substitute(values))


# 4
from sys import getrecursionlimit
print(getrecursionlimit())


# 5
from string import ascii_lowercase, ascii_uppercase, punctuation
print(punctuation)
print(ascii_uppercase)
print(ascii_lowercase)
