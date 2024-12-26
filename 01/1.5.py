# 1
print(int(input()) + 1)


# 2
number = int(input())
print(number * 2)
print(number / 2)


# 3
a = float(input())
s = a**2
print(s)


# 4
number_a = int(input())
number_b = int(input())
print(number_a + number_b)


# 5
a, b = map(float, (input(), input()))
s = a * b
p = 2 * (a + b)
print(s, p)


# 6
f = float(input())
c = (f - 32) * 5 / 9
print(c)


# 7
a = int(input())
b = int(input())
print(abs(a) + abs(b))


# 8
x1 = float(input())
x2 = float(input())
print(abs(x1 - x2))


# 9
number = float(input())
print(round(number, 2), round(number, 3))


# 10
hour_a, minute_a, second_a = map(int, (input(), input(), input()))
hour_b, minute_b, second_b = map(int, (input(), input(), input()))
print(
    (hour_b * 60 * 60 + minute_b * 60 + second_b)
    - (hour_a * 60 * 60 + minute_a * 60 + second_a)
)


# 11
a, b, c = map(int, (input() for _ in range(3)))
print(max(a + b + c, a * b + c, a * (b + c), a + b * c, (a + b) * c, a * b * c))
