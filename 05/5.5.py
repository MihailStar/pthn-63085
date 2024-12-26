# 1
number = int(input())
counter = [0] * 10
for digit in str(number):
    counter[int(digit)] += 1
for i in range(len(counter)):
    if counter[i] == 0:
        continue
    print(i, counter[i])


# 2
_unused = input()
numbers = [int(digit) for digit in input().split()]
counter = [0] * (100 + 1 + 100)
for number in numbers:
    counter[number + 100] += 1
for i in range(len(counter)):
    if counter[i] == 0:
        continue
    print(f"{i - 100} " * counter[i], end="")
