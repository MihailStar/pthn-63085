# 1
a = int(input())
b = int(input())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")


# 2
a = int(input())
b = int(input())
c = int(input())
max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)


# 3
n = int(input())
if n == 1:
    print(0)
elif n % 2 == 0:
    print(n // 2)
else:
    print(n)


# 4
salary_a, salary_b, salary_c = map(int, input().split())
if salary_b < salary_a < salary_c or salary_b > salary_a > salary_c:
    print(abs(salary_b - salary_c))
elif salary_a < salary_b < salary_c or salary_a > salary_b > salary_c:
    print(abs(salary_a - salary_c))
elif salary_b < salary_c < salary_a or salary_b > salary_c > salary_a:
    print(abs(salary_b - salary_a))


# 5
string_a, string_b = (input().lower() for _ in range(2))
if string_a < string_b:
    print(-1)
elif string_a > string_b:
    print(1)
else:
    print(0)


# 6
# @tutorial https://stepik.org/lesson/295934/step/8?discussion=1846075&unit=277638
s, v1, v2, t1, t2 = map(int, input().split())
if s * v1 + 2 * t1 < s * v2 + 2 * t2:
    print("First")
elif s * v1 + 2 * t1 > s * v2 + 2 * t2:
    print("Second")
else:
    print("Friendship")


# 7
city_a, city_b = (input() for _ in range(2))
print(
    ("Bad", "Good")[
        (city_a[-2] if city_a.endswith("ь") else city_a[-1]).lower()
        == city_b[0].lower()
    ]
)
