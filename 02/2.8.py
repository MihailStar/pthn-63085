# 1
print("Что Вы сказали? {word}? Какое интересное слово".format(word=input()))


# 2
print("Здравствуйте, {} {}!".format(input(), input()))


# 3
num = int(input())
print(
    "Для числа {num} предыдущим будет число {prev_num}.".format(
        num=num, prev_num=num - 1
    )
)
print(
    "Для числа {num} следующим будет число {next_num}.".format(
        num=num, next_num=num + 1
    )
)
