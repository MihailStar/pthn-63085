# 1
print("Привет, Мир!")


# 2
print(*input().split(), sep=",")


# 3
n = int(input())
print(n - 1, n, n + 1, sep="<")


# 4
strings = (input() for _ in range(3))
sep = "---"
print(sep.join(strings))

# 4
print(*(input() for _ in range(3)), sep="---")


# 5
sep = input()
print(sep.join(str(n) for n in range(1, 6)))

# 5
print(*(str(n) for n in range(1, 6)), sep=input())


# 6
postfix = " - Сказала она!"
print(input(), end=postfix)
