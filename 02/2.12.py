# 1
print(list(map(int, input().split()))[1])


# 2
print(list(map(int, input().split()))[2:5])


# 3
print(list(map(int, input().split()))[-3:])


# 4
print(list(map(int, input().split()))[1::3])


# 5
print(list(map(int, input().split()))[::-1])


# 6
top = [
    "Игра престолов",
    "Шерлок",
    "Друзья",
    "Во все тяжкие",
    "Доктор Хаус",
    "Теория большого взрыва",
    "Бригада",
]
top[top.index("Бригада")] = "Сверхъестественное"
top[top.index("Друзья")] = "Настоящий детектив"
print(top)


# 7
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
print(months[int(input()) - 1])
