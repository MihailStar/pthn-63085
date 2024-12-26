# 1
print(sum((int(digit) for digit in iter(input, "0"))))


# 2
last_true = None
while 4 < len(last := input()) < 10:
    last_true = last
print(last_true)


# 3
max_volume = int(input())
volume = 0
counter = 0
while True:
    new_volume = volume + int(input())
    if new_volume > max_volume:
        print("Довольно!")
        break
    volume = new_volume
    counter += 1
print(volume)
print(counter)


# 4
number_of_tasks, k = map(int, input().split())
time_to_solve_tasks = 4 * 60 - k
for counter_of_solved_tasks in range(1, number_of_tasks + 1):
    time_to_solve_tasks -= counter_of_solved_tasks * 5
    if time_to_solve_tasks < 0:
        counter_of_solved_tasks -= 1
        break
print(counter_of_solved_tasks)


# 5
number_of_cubes = int(input())
height_in_cubes = 0
while True:
    number_of_cubes -= sum(range(1, height_in_cubes + 2))
    if number_of_cubes < 0:
        break
    height_in_cubes += 1
print(height_in_cubes)


# 6
from typing import List, TypeVar
T = TypeVar("T", int, float)
def merge_lists(list_a: List[T], list_b: List[T]) -> List[T]:
    """
    @tutorial https://github.com/MihailStar/pthn-100707/blob/fb6096bb99ebc5040876bac8c81d86eb9e08465d/07/7.7.py#L102
    @tutorial AI
    """
    index_a = 0
    index_b = 0
    result: List[T] = []
    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] <= list_b[index_b]:
            result.append(list_a[index_a])
            index_a += 1
        else:
            result.append(list_b[index_b])
            index_b += 1
    while index_a < len(list_a):
        result.append(list_a[index_a])
        index_a += 1
    while index_b < len(list_b):
        result.append(list_b[index_b])
        index_b += 1
    return result
_unused = input()
result = merge_lists(
    [int(d) for d in input().split()], [int(d) for d in input().split()]
)
print(*result)


# 7
counter = 0
_number_of_m = int(input())
skills_of_m = sorted(map(int, input().split()))
index_m = 0
_number_of_w = int(input())
skills_of_w = sorted(map(int, input().split()))
index_w = 0
while index_m < len(skills_of_m):
    skill_of_m = skills_of_m[index_m]
    while index_w < len(skills_of_w):
        skill_of_w = skills_of_w[index_w]
        if skill_of_m in (skill_of_w - 1, skill_of_w, skill_of_w + 1):
            counter += 1
            del skills_of_w[index_w]
            break
        index_w += 1
    index_w = 0
    index_m += 1
print(counter)
