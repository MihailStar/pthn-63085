# 1
print(f"Мое имя {input()}!")


# 2
name = input()
age = input()
print(f"Hello {name.upper()}. You are {age} years old.")


# 3
name = input()
year = int(input())
print(f"{name}, вам исполнится 77 лет в {year + 77}")


# 4
seconds = int(input())
print(f"{seconds} сек - это {seconds // 60} мин. {seconds % 60} сек.")


# 5
w, h = map(int, input().split())
print(f"Разрешение экрана: {w} x {h}.")
print(f"Общее количество пикселей = {w * h}.")


# 6
a, b = (int(input()) for _ in range(2))
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")


# 7
x, y, z = (int(input()) for _ in range(3))
print(f"Vector A({x}, {y}, {z})")
print(f"Vector B({x + 5}, {y + 5}, {z + 5})")


# 8
курс = float(input())
количество = int(input())
стоимость = курс * количество
print(f"Current dollar rate is {курс}. You want to buy {количество} dollars")
print(f"You must pay {стоимость}")
