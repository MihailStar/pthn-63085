# 1
number = int(input())
while number > 0:
    print(number % 10)
    number //= 10


# 2
number = int(input())
result = 0
while number > 0:
    result += number % 10
    number //= 10
print(result)


# 3
number = int(input())
result = 1
while number > 0:
    result *= number % 10
    number //= 10
print(result)


# 4
from math import inf
number = int(input())
mi = inf
ma = -inf
while number > 0:
    di = number % 10
    if di < mi:
        mi = di
    if di > ma:
        ma = di
    number //= 10
print(mi)
print(ma)


# 5
number = int(input())
counter = 0
while number > 0:
    if number % 10 == 7:
        counter += 1
    number //= 10
print(counter)


# 6
number = int(input())
while number > 0:
    print(number % 2)
    number //= 2
