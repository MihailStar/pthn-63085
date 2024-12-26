# 1
print(int(input()) > 0)


# 2
print(not (int(input()) % 2))


# 3
print(int(input()) % 6 == 0)


# 4
print(bool(int(input()) % 9))


# 5
print(int(input()) % 10 == 2)


# 6
number_a, number_b = map(int, input().split())
print(number_a % 7 == 0 and number_b % 7 == 0)


# 7
a, b, c = map(int, input().split())
print(a == b and b == c and c == a)


# 8
number = int(input())
print(5 < number <= 19)


# 9
print(input() == "awesome" or input() == "awesome")


# 10
a, b, c = map(int, input().split())
print(a == b or b == c or c == a)


# 11
number = int(input())
print(9 < number < 100)


# 12
a, b, c = map(int, input().split())
print(
    a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2
)
