# 1
my_list = [1] * 77
print(my_list)


# 2
my_list = ["q", "w", "t"] * 15
print(my_list)


# 3
my_list = [-989, 993]
print(min(my_list), max(my_list))


# 4
print(any(map(lambda digit: digit == "777", input().split())))


# 5
print(sum(map(int, input().split())))


# 6
mas = list(map(int, input().split()))
print(min(mas), max(mas))


# 7
from statistics import mean
print(float(mean(map(int, input().split()))))
