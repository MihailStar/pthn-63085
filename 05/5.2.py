# 1
print(*range(1, int(input()) + 1), sep="\n")


# 2
print(*range(0, 501, 5), sep="\n")


# 3
print(*range(int(input()), 0, -1), sep="\n")


# 4
print("Надо было брать биткоин в 2012!\n" * 13)


# 5
print((input() + "\n") * int(input()))


# 6
f, t = int(input()), int(input())
for n in range(f, t + 1):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# 7
for n in range(int(input()), int(input()) + 1):
    print(f"Число {n}; его квадрат = {n ** 2}; его куб = {n ** 3}")


# 8
total = 0
for n in range(int(input()) - 1, 0, -1):
    if n % 3 == 0 or n % 5 == 0:
        total += n
print(total)


# 9
from math import factorial
print(factorial(int(input())))


# 10
from typing import Dict, Literal
counter: Dict[Literal["Mishka", "Chris"], int] = {"Mishka": 0, "Chris": 0}
for _ in range(int(input())):
    Mishka, Chris = map(int, input().split())
    if Mishka > Chris:
        counter["Mishka"] += 1
    elif Chris > Mishka:
        counter["Chris"] += 1
if counter["Mishka"] > counter["Chris"]:
    print("Mishka")
elif counter["Chris"] > counter["Mishka"]:
    print("Chris")
else:
    print("Friendship is magic!^^")


# 11
for line_number in range(1, int(input()) + 1):
    index = input().lower().find("рок")
    if index == -1:
        continue
    print(line_number, index + 1)


# 12
print(
    *(word for _ in range(int(input())) if (word := input()).find("соль") == -1),
    sep=", ",
)


# 13
for _ in range(int(input())):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{(len(word)-2)}{word[-1]}")
    else:
        print(word)
