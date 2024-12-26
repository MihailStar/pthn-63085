# 1
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
for number in (111, 222, 789, 201):
    numbers.append(number)
print(numbers)


# 2
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
numbers.insert(5, 111)
numbers.insert(8, 222)
numbers.insert(0, 789)
numbers.insert(11, 201)
print(numbers)


# 3
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
numbers.extend(extra)
print(numbers)


# 4
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
sum_of_removed = numbers.pop() + numbers.pop(0) + numbers.pop(12) + numbers.pop(7)
print(numbers)
print(sum_of_removed)


# 5
numbers = [
    -214,
    777,
    181,
    9,
    32,
    -139,
    43,
    89,
    77,
    448,
    -20,
    -917,
    54,
    5,
    432,
    43,
    32,
    422,
    -895,
    7,
    198,
    284,
    472,
    3,
    -986,
    -964,
    -989,
    29,
]
numbers.remove(3)
numbers.remove(5)
numbers.remove(7)
numbers.remove(9)
print(numbers)


# 6
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
numbers.sort(reverse=True)
print(numbers)


# 7
a = list(map(int, input().split()))
a.reverse()
print(a)


# 8
a = list(map(int, input().split()))
print(a.count(999))


# 9
numbers = [
    -214,
    181,
    -139,
    448,
    -20,
    -917,
    32,
    422,
    -895,
    198,
    284,
    472,
    -986,
    -964,
    -989,
    29,
]
copy_numbers = numbers.copy()
print(copy_numbers)


# 10
word_1, word_separator, word_2 = input().upper().partition(" ")
print(
    word_separator.join(map(lambda word: "-".join(word), (word_1, word_2))),
    sep="",
)

# 10
word_1, _sep, word_2 = input().upper().partition(" ")
print(*map(lambda word: "-".join(word), (word_1, word_2)))


# 11
и, о, ф = input().split()
print(ф.capitalize(), " ", и[0].upper(), ".", о[0].upper(), ".", sep="")


# 12
print("\n".join(input().split()))
