# 1
repeated = {}
for word in input().split():
    lowered_word = word.lower()
    if lowered_word in repeated:
        continue
    repeated[lowered_word] = word
    print(word, end=" ")
