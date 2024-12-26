# 1
size = int(input())
side_diagonal: list[int] = []
for y in range(size):
    for x, n in enumerate(int(n) for n in input().split()):
        if y + x == size - 1:
            side_diagonal.append(n)
            break
print(max(side_diagonal))

# 1
# Побочная диагональ (Side diagonal) `y + x == size - 1`
from math import inf
size = int(input())
mx = -inf
for y in range(size):
    for x, n in enumerate(int(n) for n in input().split()):
        if y + x == size - 1:
            mx = max(mx, n)
            break
print(mx)


# 2
# Главная диагональ (Main diagonal) `y == x`
size = int(input())
a, b, c = map(int, input().split())
for y in range(size):
    row: list[int] = []
    for x in range(size):
        if y < x:
            row.append(a)
        elif y > x:
            row.append(b)
        else:
            row.append(c)
    print(*row)


# 3
board: list[list[str]] = []
board_size = 8
y_and_x_of_T = (0, 0)
for y in range(board_size):
    row: list[str] = []
    for x, symbol in enumerate(input()):
        row.append(symbol)
        if symbol == "T":
            y_and_x_of_T = (y, x)
    board.append(row)
for n in range(board_size):
    board[n][y_and_x_of_T[1]] = "+"
    board[y_and_x_of_T[0]][n] = "+"
board[y_and_x_of_T[0]][y_and_x_of_T[1]] = "T"
for row in board:
    print(*row, sep="")

# 3
# Тура | Ладья `y == y_T or x == x_T`
board: list[list[str]] = []
board_size = 8
y_T, x_T = 0, 0
for y in range(board_size):
    row: list[str] = []
    for x, symbol in enumerate(input()):
        row.append(symbol)
        if symbol == "T":
            y_T, x_T = y, x
    board.append(row)
for n in range(board_size):
    board[y_T][n] = "+"
    board[n][x_T] = "+"
board[y_T][x_T] = "T"
for row in board:
    print(*row, sep="")


# 4
# Слон `abs(y - y_S) == abs(x - x_S)`
board: list[list[str]] = []
board_size = 8
y_S, x_S = (0, 0)
for y in range(board_size):
    row: list[str] = []
    for x, symbol in enumerate(input()):
        row.append(symbol)
        if symbol == "S":
            y_S, x_S = y, x
    board.append(row)
for y in range(board_size):
    for x in range(board_size):
        if abs(y - y_S) == abs(x - x_S):
            board[y][x] = "+"
board[y_S][x_S] = "S"
for row in board:
    print(*row, sep="")


# 5
uniforms_colors = list[tuple[str, str]]()
for _ in range(int(input())):
    inner, outer = input().split()
    uniforms_colors.append((inner, outer))
counter = 0
for i in range(len(uniforms_colors)):
    for j in range(len(uniforms_colors)):
        if i == j:
            continue
        if uniforms_colors[i][0] == uniforms_colors[j][1]:
            counter += 1
print(counter)


# 6
n, m = map(int, input().split())
field = list(list(input()) for _ in range(n))
counter = 0
for y in range(n):
    for x in range(m):
        if field[y][x] == "*":
            continue
        sub_counter = 0
        for sibling_y, sibling_x in ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)):
            try:
                if sibling_y < 0 or sibling_x < 0:
                    raise IndexError
                if field[sibling_y][sibling_x] != "*":
                    sub_counter += 1
            except IndexError:
                sub_counter += 1
        if sub_counter == 4:
            counter += 1
print(counter)

# 6
n, m = map(int, input().split())
field = list(list(input()) for _ in range(n))
counter = 0
for y in range(n):
    for x in range(m):
        if field[y][x] == "*":
            continue
        sub_counter = 0
        for sibling_y, sibling_x in ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)):
            if (
                sibling_y < 0
                or sibling_y > n - 1
                or sibling_x < 0
                or sibling_x > m - 1
                or field[sibling_y][sibling_x] != "*"
            ):
                sub_counter += 1
        if sub_counter == 4:
            counter += 1
print(counter)


# 7
# Ферзь `y == y_F or x == x_F or abs(y - y_F) == abs(x - x_F)`
board: list[list[str]] = []
board_size = 8
y_F, x_F = (0, 0)
for y in range(board_size):
    row: list[str] = []
    for x, symbol in enumerate(input()):
        row.append(symbol)
        if symbol == "F":
            y_F, x_F = y, x
    board.append(row)
for y in range(board_size):
    for x in range(board_size):
        if y == y_F or x == x_F or abs(y - y_F) == abs(x - x_F):
            board[y][x] = "+"
board[y_F][x_F] = "F"
for row in board:
    print(*row, sep="")


# 8
# Конь `abs((y - y_H) * (x - x_H)) == 2`
board: list[list[str]] = []
board_size = 8
y_H, x_H = (0, 0)
for y in range(board_size):
    row: list[str] = []
    for x, symbol in enumerate(input()):
        row.append(symbol)
        if symbol == "H":
            y_H, x_H = y, x
    board.append(row)
for y in range(board_size):
    for x in range(board_size):
        if abs((y - y_H) * (x - x_H)) == 2:
            board[y][x] = "+"
board[y_H][x_H] = "H"
for row in board:
    print(*row, sep="")


# 9
n, m = map(int, input().split())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
for y in range(1, n):
    for x in range(1, m):
        matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]
for row in matrix:
    print(*row)


# 10
n, m = map(int, input().split())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
for y in range(n - 2, -1, -1):
    for x in range(m - 2, -1, -1):
        matrix[y][x] = matrix[y + 1][x] + matrix[y][x + 1]
for row in matrix:
    print(*row)


# 11
# @tutorial https://github.com/MihailStar/pthn-68343/blob/3147a62cc567aedeed014829086334c57ee11708/04/4.6.py#L75
n, m = map(int, input().split())
width = len(str(n * m))
for y in range(n):
    for x in range(0, m) if y % 2 == 0 else range(m - 1, -1, -1):
        print(str(x + m * y).ljust(width), end=" ")
    print()


# 12
n, _m = map(int, input().split())
for _ in range(n):
    for char in input():
        if char in ("C", "M", "Y"):
            print("#Color")
            break
    else:
        continue
    break
else:
    print("#Black&White")


# 13
# @tutorial https://github.com/MihailStar/pthn-68343/blob/3147a62cc567aedeed014829086334c57ee11708/04/4.6.py#L112
from enum import Enum
from itertools import cycle
n = m = int(input())
width = len(str(n * m))
y, x, c, matrix = 0, 0, 1, [[0] * m for _ in range(n)]
class Direction(Enum):
    Right = 1
    Bottom = 2
    Left = 3
    Top = 0
def move_to_next_cell(direction: Direction) -> None:
    global y, x
    if direction == Direction.Right:
        x += 1
    elif direction == Direction.Bottom:
        y += 1
    elif direction == Direction.Left:
        x -= 1
    elif direction == Direction.Top:
        y -= 1
    else:
        raise ValueError("Invalid direction")
def fill_in(direction: Direction) -> None:
    try:
        global y, x, c, matrix
        while True:
            if matrix[y][x] != 0:
                raise IndexError
            matrix[y][x] = c
            c += 1
            move_to_next_cell(direction)
    except IndexError:
        if direction == Direction.Right:
            move_to_next_cell(Direction.Left)
        elif direction == Direction.Bottom:
            move_to_next_cell(Direction.Top)
        elif direction == Direction.Left:
            move_to_next_cell(Direction.Right)
        elif direction == Direction.Top:
            move_to_next_cell(Direction.Bottom)
for direction in cycle(
    (Direction.Right, Direction.Bottom, Direction.Left, Direction.Top)
):
    if c > n * m:
        break
    fill_in(direction)
    if direction == Direction.Right:
        move_to_next_cell(Direction.Bottom)
    elif direction == Direction.Bottom:
        move_to_next_cell(Direction.Left)
    elif direction == Direction.Left:
        move_to_next_cell(Direction.Top)
    elif direction == Direction.Top:
        move_to_next_cell(Direction.Right)
print("\n".join(map(lambda r: " ".join(map(lambda n: str(n).ljust(width), r)), matrix)))


# 14
from typing import Literal
n, m = map(int, input().split())
pie = [list(input()) for _ in range(n)]
counter = 0
berry_in_column: dict[int, Literal[True]] = {}
for y in range(n):
    for x in range(m):
        if pie[y][x] == "S":
            berry_in_column[x] = True
            break
    else:
        pie[y] = [""] * m
        counter += m
for x in range(m):
    if berry_in_column.get(x, False):
        continue
    for y in range(n):
        if pie[y][x] == "S" or pie[y][x] == "":
            continue
        counter += 1
print(counter)
