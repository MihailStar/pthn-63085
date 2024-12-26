# 1
words = ["Python", "мы любим", "тебя"]
for index in range(5):
    try:
        print(index, words[index])
    except IndexError:
        print(f"Индекс {index} вышел за границы списка")
        break
print("Знай это")


# 2
words = ["Python", "мы любим", "тебя"]
for index in range(7):
    try:
        print(index, words[index])
    except IndexError:
        print(f"Индекс {index} вышел за границы списка")
print("Знай это")


# 3
try:
    print(list(range(10_000_000_000)))
except MemoryError:
    print("У питона память сломалась")
