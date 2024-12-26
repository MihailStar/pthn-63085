# 1
from math import ceil
n = int(input())
print(ceil(n / 10))


# 2
from math import ceil
n = int(input())
print(ceil(n / 4))


# 3
from math import ceil
a, b, c = (int(input()) for _ in range(3))
print(ceil(a / 2) + ceil(b / 2) + ceil(c / 2))


# 4
from math import ceil
l, w, h = map(int, (input().split()))
print(ceil((l * h * 2 + w * h * 2) / 16))
