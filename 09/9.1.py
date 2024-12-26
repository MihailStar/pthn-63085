# 1
def file_read(path: str) -> None:
    file = open(path, encoding="utf-8")
    print(file.read())
    file.close()


# 2
def file_n_lines(path: str, n: int) -> None:
    file = open(path, encoding="utf-8")
    for _ in range(n):
        print(file.readline().rstrip())
    file.close()


# 3
def create_file_with_numbers(n: int) -> None:
    path = f"range_{n}.txt"
    file = open(path, "w", encoding="utf-8")
    for i in range(1, n + 1):
        file.write(f"{i}\n")
    file.close()


# 4
from string import punctuation
def longest_word_in_file(path: str) -> str:
    file = open(path, "r", encoding="utf-8")
    longest_word = max(
        reversed(
            "".join(char for char in file.read() if char not in punctuation).split()
        ),
        key=len,
    )
    file.close()
    return longest_word

# 4
from string import punctuation
def longest_word_in_file(path: str) -> str:
    file = open(path, "r", encoding="utf-8")
    longest_word = max(
        reversed([word.rstrip(punctuation) for word in file.read().split()]), key=len
    )
    file.close()
    return longest_word
