# 1
my_set = set()
print(my_set)


# 2
from statistics import mean
my_list = [
    56,
    59,
    53,
    75,
    62,
    61,
    75,
    65,
    59,
    62,
    64,
    53,
    54,
    62,
    69,
    53,
    55,
    62,
    54,
    66,
    55,
    57,
    58,
    75,
    72,
    55,
    51,
    56,
    71,
    66,
    57,
    56,
    59,
    73,
    68,
    57,
    50,
    54,
    62,
    68,
    59,
    64,
    59,
    59,
    71,
    68,
    57,
    54,
    53,
    72,
]
my_set = set(my_list)
print(mean(my_set))


# 3
print("CHAT WITH HER!" if len(set(input())) % 2 == 0 else "IGNORE HIM!")


# 4
print(4 - len(set(input().split())))


# 5
print("YES" if len(set(input().upper())) == 26 else "NO")


# 6
beautiful_year = int(input())
while True:
    beautiful_year += 1
    if len(set(str(beautiful_year))) == 4:
        print(beautiful_year)
        break


# 7
from re import split
antons_set = set(split(r" ?, ?", input().strip(" {}")))
print(0 if antons_set == {""} else len(antons_set))
