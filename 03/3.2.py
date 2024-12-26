# 1
text = "Odd" if int(input()) % 2 else "Even"
print(text)


# 2
a = int(input())
b = int(input())
minimum, maximum = (a, b) if a < b else (b, a)
print(minimum, maximum)


# 3
sentence = "Вопросительное" if input().endswith("?") else "Обычное"
print(sentence)


# 4
polarity_a = input()
polarity_b = input()
experiment = "Притягиваются" if polarity_a != polarity_b else "Отталкиваются"
print(experiment)
