# 1
matrix = [[int(item) for item in input().split()] for _ in range(int(input()))]
total = 0
for y, row in enumerate(matrix):
    for x, item in enumerate(row):
        if y == x:
            total += item
print(total)


# 2
matrix = [list(map(int, input().split())) for _ in range(int(input()))]
for x in range(len(matrix)):
    for y in range(len(matrix)):
        print(matrix[y][x], end=" ")
    print()


# 3
matrix = [[int(item) for item in input().split()] for _ in range(int(input()))]
for x in range(len(matrix) - 1, -1, -1):
    for y in range(len(matrix) - 1, -1, -1):
        print(matrix[y][x], end=" ")
    print()


# 4
n, m = [int(size) for size in input().split()]
matrix = [[int(item) for item in input().split()] for _ in range(n)]
for y in range(n):
    for x in range(m - 1, -1, -1):
        print(matrix[y][x], end=" ")
    print()


# 5
n, m = (int(size) for size in input().split())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
for y in range(n - 1, -1, -1):
    for x in range(m):
        print(matrix[y][x], end=" ")
    print()


# 6
size = 5
matrix = [[int(item) for item in input().split()] for _ in range(size)]
center = (2, 2)
current = center
for y in range(size):
    for x in range(size):
        if matrix[y][x] == 1:
            current = (y, x)
    else:
        continue
    break
print(abs(center[0] - current[0]) + abs(center[1] - current[1]))


# 7
from typing import Dict, List, Literal
n, m = (int(size) for size in input().split())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
total: Dict[Literal["row", "col"], List[int]] = {"row": [], "col": []}
for y in range(n):
    row_total = 0
    for x in range(m):
        row_total += matrix[y][x]
    total["row"].append(row_total)
for x in range(m):
    col_total = 0
    for y in range(n):
        col_total += matrix[y][x]
    total["col"].append(col_total)
print(*total["row"])
print(*total["col"])


# 8
size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
for y in range(size):
    for x in range(size):
        if matrix[y][x] != matrix[x][y]:
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")


# 9
n, m = (int(size) for size in input().split())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
results = [(sum(row), index) for index, row in enumerate(matrix)]
max_result, max_result_index = max(results, key=lambda pair: pair[0])
print(max_result)
print(max_result_index)


# 10
n, m = (int(size) for size in input().split())
max_result, max_result_y, max_result_x = max(
    [
        max(
            ((int(item), y, x) for x, item in enumerate(input().split())),
            key=lambda it: it[0],
        )
        for y in range(n)
    ],
    key=lambda it: it[0],
)
print(max_result)
print(max_result_y, max_result_x)


# 11
n, m = (int(size) for size in input().split())
sportsmans_throws = tuple(
    tuple(int(throw) for throw in input().split()) for _ in range(n)
)
print(
    max(
        enumerate(sportsmans_throws),
        key=lambda index_and_sportsman_throws: (
            max(index_and_sportsman_throws[1]),
            sum(index_and_sportsman_throws[1]),
            -index_and_sportsman_throws[0],
        ),
    )[0]
)


# 12
n, m = (int(size) for size in input().split())
best_throws = tuple(max(int(throw) for throw in input().split()) for _ in range(n))
best = max(best_throws)
print(len([best_throw for best_throw in best_throws if best_throw == best]))


# 13
size = 4
pattern = tuple(input() for _ in range(size))
for y in range(size - 1):
    for x in range(size - 1):
        if (
            pattern[y][x]
            == pattern[y][x + 1]
            == pattern[y + 1][x + 1]
            == pattern[y + 1][x]
        ):
            print("No")
            break
    else:
        continue
    break
else:
    print("Yes")


# 14
n, _m = (int(size) for size in input().split())
source = tuple(input() for _y in range(n))
counter = 0
input()
for y in range(n):
    for x, color in enumerate(input()):
        if source[y][x] == color:
            counter += 1
print(counter)


# 15
size, looking = map(int, (input().split()))
counter = 0
for y in range(1, size + 1):
    for x in range(1, size + 1):
        if y * x == looking:
            counter += 1
print(counter)
