# 1
numbers = [99, 15]
for number in numbers:
    print(number)


# 2
words = ["require", "sometimes"]
for word in words:
    if not len(word) > 6:
        pass
    else:
        print(word)


# 3
numbers = [-35, -51]
numbers = list(map(lambda number: number * 2, numbers))
print(numbers)


# 4
print([input() for _ in range(int(input()))])


# 5
search_letter = input().lower()
for word in input().split():
    if search_letter not in word.lower():
        continue
    print(word)


# 6
numbers = map(int, input().split())
search_number = int(input())
for index, number in enumerate(numbers):
    if search_number == number:
        print(index + 1)
        break
else:
    print("ErrorValue")


# 7
try:
    minimum_positive_number = min(filter(lambda n: n > 0, map(int, input().split())))
    print(minimum_positive_number)
except ValueError:
    print("Empty")


# 8
from collections import Counter

print(Counter(input().lower()).most_common())

# 8
from collections import Counter

print(Counter(input().lower()).most_common()[0][1])


# 9
numbers = list(map(int, filter(lambda char: char.isdigit(), input())))
print(len(numbers), sum(numbers))


# 10
even_digits, odd_digits = [], []
for index, digit in enumerate(input()):
    (odd_digits if index % 2 else even_digits).append(int(digit))
print("NO" if (sum(even_digits) - sum(odd_digits)) % 11 else "YES")


# 11
numbers = [int(digit) for digit in input().split()]
print(numbers == [*sorted(numbers)])


# 12
counter = 0
for next in input():
    counter += 1 if next == "(" else -1
    if counter < 0:
        print("NO")
        break
else:
    print("YES" if counter == 0 else "NO")


# 13
from typing import Generic, List, TypeVar
T = TypeVar("T")
class Stack(Generic[T]):
    """
    @tutorial https://github.com/MihailStar/rss-tasks/blob/49f0cbfbeb69a4e003bd2b6b2724ddf397091f9e/basic-js-ds/stack.ts#L1
    @tutorial AI
    """
    _stack: List[T]
    def __init__(self, initial_stack: List[T] | None = None) -> None:
        self._stack = [] if initial_stack is None else initial_stack[:]
    def push(self, element: T) -> None:
        self._stack.append(element)
    def pop(self) -> T | None:
        if self._stack:
            return self._stack.pop()
        return None
    def peek(self) -> T | None:
        if self._stack:
            return self._stack[-1]
        return None
    def is_empty(self) -> bool:
        return not self._stack
    def size(self) -> int:
        return len(self._stack)
stack: Stack[str] = Stack[str]()
brackets = {"(": ")", "[": "]", "{": "}"}
for next in input():
    if next in brackets:
        stack.push(next)
    else:
        prev = stack.pop()
        if prev is None or brackets[prev] != next:
            print("NO")
            break
        else:
            pass
else:
    print("YES" if stack.is_empty() else "NO")
