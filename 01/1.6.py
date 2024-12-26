# 1
numbers = list(map(int, input().split()))
print(sum(numbers) / len(numbers))


# 2
grade = list(map(int, input().split()))
print(max(grade))


# 3
n, a, b = map(int, input().split())
print(a * b * 2 * n)


# 4
s = int(input())
print(int(s * 1 / 6), int(s * 4 / 6), int(s * 1 / 6))

# 4
s = int(input())
print(s * 1 // 6, s * 4 // 6, s * 1 // 6)


# 5
x, y, z = map(int, input().split())
print(x * 3 + y * (3 + 2) + z * (3 + 2 + 7))


# 6
г, л = map(int, input().split())
print((г + л - 1) - г, (г + л - 1) - л)
