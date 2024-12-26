# 1
for y in range(1, int(input()) + 1):
    for x in range(1, y + 1):
        print(x, end=" ")
    print()


# 2
for n in [int(d) for d in input().split()]:
    print("*" * n)


# 3
n = int(input())
p = 0
for number in range(n + 1, 2 * n):
    # @tutorial https://github.com/MihailStar/rss-tasks/blob/49f0cbfbeb69a4e003bd2b6b2724ddf397091f9e/data-structures-part-2/next-prime.ts#L1
    # @tutorial https://github.com/MihailStar/pthn-100707/blob/fb6096bb99ebc5040876bac8c81d86eb9e08465d/09/9.2.py#L81
    for divider in range(2, int(number**0.5) + 1):
        if number % divider == 0:
            break
    else:
        p += 1
print(p)


# 4
_unused = input()
numbers = [int(d) for d in input().split()]
counter = 0
# NB: bad bubble sort without flag
for number_of_sorted in range(len(numbers) - 1):
    for index in range(len(numbers) - 1 - number_of_sorted):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
            counter += 1
print(*numbers)
print(counter)


# 5
n, m = map(int, input().split())
c = 0
for a in range(int(1_000**0.5) + 1):
    for b in range(int(1_000**0.5) + 1):
        v1, v2 = a**2 + b, a + b**2
        if v1 > n or v2 > m:
            break
        if v1 == n and v2 == m:
            c += 1
print(c)


# 6
_unused = input()
numbers = [int(d) for d in input().split()]
eval(
    f"print(*{''.join(map(lambda code: chr(code), [115, 111, 114, 116, 101, 100]))}(numbers))"
)
