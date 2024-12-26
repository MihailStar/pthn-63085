# 1
r, g, b = map(
    lambda color: hex(int(color)).lstrip("0x").zfill(2).upper(),
    (input() for _ in range(3)),
)
print("#", r, g, b, sep="")


# 2
# @tutorial "Символы в параметре `chars` рассматриваются не как последовательность, а как набор символов, которые необходимо удалить"
print(input().strip(" -_!?"))


# 3
print(input().lstrip("-_!?"))


# 4
print(input().rstrip("-_!?"))
