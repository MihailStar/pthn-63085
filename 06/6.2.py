# 1
my_tuple = (1, 2, 3, 4)


# 2
lonely = (777,)
print(lonely)


# 3
my_tuple = (-214, 29)
print(min(my_tuple), max(my_tuple))


# 4
from statistics import mean
my_tuple = (-214, 29)
print(mean(my_tuple))


# 5
a, b, c, d = (1,), ("R",), ("A",), (2,)
result = a * 3 + b * 5 + c * 8 + d * 5
print(result)


# 6
f, t = int(input()), int(input())
print(tuple(range(f, t + 1)))


# 7
n = int(input())
print(tuple(range(n + 1 if n % 2 == 0 else n, n**2 + 1, 2)))
