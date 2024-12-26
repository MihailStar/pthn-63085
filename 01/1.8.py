# 1
print(int(input()) // 1_000)


# 2
n, k = map(int, (input(), input()))
print(k // n)


# 3
n, r = map(int, (input(), input()))
print(n // r)


# 4
print(int(input()) % 10)


# 5
print(int(input()) // 100 % 10)


# 6
n = int(input())
print(n // 100 % 10 + n // 10 % 10 + n // 1 % 10)


# 7
n = int(input())
banknotes = (1, 5, 10, 20, 100)
banknote_counter = 0
for banknote in reversed(banknotes):
    number_of = n // banknote
    n -= number_of * banknote
    banknote_counter += number_of
print(banknote_counter)

# 7
n = int(input())
banknotes = (1, 5, 10, 20, 100)
banknote_counter = 0
for banknote in reversed(banknotes):
    banknote_counter += n // banknote
    n %= banknote
print(banknote_counter)


# 8
n = int(input())
print(n // 60 % 24, n % 60)


# 9
n = int(input())
print(n + (2 - n % 2))


# 10
n = int(input())
h, m, s = n // 60 // 60 % 24, n // 60 % 60, n % 60
H, M, S = (
    str(h),
    str(m // 10 % 10) + str(m % 10),
    str(s // 10 % 10) + str(s % 10),
)
print(H, M, S, sep=":")
