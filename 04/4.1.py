# 1
n = 1000
while n < 2001:
    print(n)
    n += 1


# 2
n = 6785
while n >= 195:
    print(n)
    n -= 5


# 3
l, b = map(int, input().split())
counter = 0
while not l > b:
    counter += 1
    l *= 3
    b *= 2
print(counter)


# 4
numbers = [2, 4, 0]
print(*filter(lambda number: number != 4, numbers))


# 5
text = input()
while len(text) >= 1:
    print(text)
    text = text[1:-1]


# 6
n, i = int(input()), 1
while (square := i**2) <= n:
    print(square)
    i += 1


# 7
x, y = map(int, input().split())
counter = 0
while x < y:
    counter += 1
    x *= 1.15
print(counter + 1)


# 8
n, m = map(int, input().split())
counter = 0
while n > 0:
    counter += 1
    n -= 1
    if counter % m == 0:
        n += 1
print(counter)


# 9
a, b = map(int, input().split())
counter = 0
while a > 0:
    counter += 1
    a -= 1
    if counter % b == 0:
        a += 1
print(counter)


# 10
n = int(input())
power = 0
while (to_power := 2**power) <= n:
    if to_power == n:
        print(power)
        break
    power += 1
else:
    print("НЕТ")


# 11
n = int(input())
while n <= 1e9:
    first = int(str(n)[0])
    if first == 1:
        print(n)
        break
    n *= first
else:
    print(n)
