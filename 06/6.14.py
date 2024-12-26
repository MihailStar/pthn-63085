# 1
words = [
    "feel",
    "graduate",
    "movie",
    "fashionable",
    "bacon",
    "drop",
    "produce",
    "acquisition",
    "cheap",
    "strength",
    "master",
    "perception",
    "noise",
    "strange",
    "am",
]
words_with_position = [tuple(reversed(pair)) for pair in enumerate(words, start=1)]
print(words_with_position)


# 2
english_words = (
    "attack",
    "bless",
    "look",
    "reckless",
    "short",
    "monster",
    "trolley",
    "sound",
    "ambiguity",
    "researcher",
    "trunk",
    "coat",
    "quantity",
    "question",
    "tenant",
    "miner",
    "definite",
    "kit",
    "spectrum",
    "satisfied",
    "selection",
    "carve",
    "ask",
    "go",
    "suggest",
)
for number, word in enumerate(english_words, start=1):
    print(f"Word № {number} = {word}")


# 3
# Алгоритм Луна (Luhn algorithm)
card_number = input()
temp = [int(digit) for digit in card_number]
for index in range(0, len(temp), 2):
    temp[index] *= 2
    if temp[index] > 9:
        temp[index] -= 9
print(sum(temp) % 10 == 0)
