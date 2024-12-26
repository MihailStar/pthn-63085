# 1
n = int(input())
for divider in range(2, n + 1):
    if n % divider == 0:
        print(divider)
        break


# 2
a, b = int(input()), int(input())
n = a
while n <= b:
    if n % 777 == 0:
        n += 1
        break
    if n % 2 == 0 or n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1


# 3
n = int(input())
counter = 0
while True:
    if n == 1:
        break
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    counter += 1
print(counter)


# 4
word = input()
index = 0
while index < len(word):
    if word[index] in ("a", "e"):
        print("Ага! Нашлась")
        break
    print(f"Текущая буква: {word[index]}")
    index += 1
else:
    print("Распечатали все буквы")
