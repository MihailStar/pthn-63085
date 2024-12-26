# 1
print("ДА" if input() == "Python" else "НЕТ")


# 2
доход = int(input())
print(доход if доход <= 10000 else доход * 0.87)


# 3
a, b = int(input()), int(input())
print(a if a > b else b)


# 4
a, b, c = map(int, input().split())
print("YES" if a + b == c else "NO")


# 5
print([num for num in (int(dig) for dig in input().split()) if num not in (3, 5, 7, 9)])


# 6
limit = 10_000
if (summ := int(input())) <= limit:
    print(f"Сумма {summ} не превышает лимит, проходите")
else:
    difference = summ - limit
    print(f"Ого! {summ}! Куда вам столько? Мы заберем {difference}")


# 7
if "walrus" in (phrase := input()):
    print("Нашли моржа")
else:
    print("Никаких моржей тут нет")


# 8
s, t = input(), input()
print("YES" if s == "".join(reversed(t)) else "NO")


# 9
n = int(input())
print("YES" if str(n) == "".join(reversed(str(n))) else "NO")


# 10
a, b, c = (int(input()) for _ in range(3))
if a + b > c and b + c > a and c + a > b:
    print("YES")
else:
    print("NO")


# 11
ticket_number = input().zfill(6)
print(
    "YES"
    if sum(map(int, ticket_number[:3])) == sum(map(int, ticket_number[3:]))
    else "NO"
)


# 12
x1, y1 = input()
x2, y2 = input()
x1, x2 = (("a", "b", "c", "d", "e", "f", "g", "h").index(x) + 1 for x in (x1, x2))
y1, y2 = (int(y) for y in (y1, y2))
print("YES" if (x1 + y1) % 2 == (x2 + y2) % 2 else "NO")
