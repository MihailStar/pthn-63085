# 1
match int(input()):
    case 1:
        print("Совсем еще зеленый студентик")
    case 2:
        print("Джун-студент")
    case 3:
        print("Мидл-студент")
    case 4:
        print("Сеньор-студент")
    case 5:
        print("Босс качалки")
    case _:
        print("Неизвестный курс")


# 2
match int(input()):
    case 2:
        print(28)
    case 4 | 6 | 9 | 11:
        print(30)
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(31)
    case _:
        raise ValueError()


# 3
match input():
    case "Овен" | "Лев" | "Стрелец":
        print("Огненный")
    case "Телец" | "Дева" | "Козерог":
        print("Земной")
    case "Близнецы" | "Весы" | "Водолей":
        print("Воздушный")
    case "Рак" | "Скорпион" | "Рыбы":
        print("Водный")
    case _:
        raise ValueError()
