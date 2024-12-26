# 1
print(("Я стану крутым программистом!" + "\n") * 3)


# 2
print("W" * 777)


# 3
print('Лев Николаевич Толстой написал "Война и мир"')


# 4
print(input())
print(input())


# 5
phrases = [input() for _ in range(3)]
for phrase in reversed(phrases):
    print(phrase)


# 6
print(" ".join(([input()] * 4)))


# 7
print(len(input()))


# 8
phrase_a, phrase_b = [input() for _ in range(2)]
print(phrase_b, phrase_a, sep="")


# 9
print(input() * 3)


# 10
symbols = input().split()
for symbol in symbols:
    code = ord(symbol)
    print(f"Simvol code {symbol} is {code}.")
