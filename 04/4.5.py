# 1
a, b = map(int, input().split())
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)  # НОД вычитанием


# 2
a, b = map(int, input().split())
while b > 0:
    division_remainder = a % b
    a = b
    b = division_remainder
print(a)  # НОД делением


# 3
from math import gcd
a, b = map(int, input().split())
nod = gcd(a, b)
nok = (a * b) // nod
print(nok)  # НОК
