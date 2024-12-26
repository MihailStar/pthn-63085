# 1
def keanu_reeves() -> None:
    print("YOU'RE BREATHTAKING")


# 2
def say_hello_world(name: str) -> None:
    print(f"{name} говорит hello world!")


# 3
def summa_n(t: int) -> None:
    print(f"Я знаю, что сумма чисел от 1 до {t} равна {sum(range(1, t + 1))}")


# 4
def exponentiation(n: int) -> None:
    print(n**2, n**3)


# 5
def sum_num(line: str) -> None:
    print(sum(int(char) for char in line if char.isdigit()))


# 6
def get_body_mass_index(масса: int, рост: int) -> None:
    индекс = масса / (рост / 100) ** 2
    if индекс < 18.5:
        print("Недостаточная масса тела")
    elif 18.5 <= индекс <= 25:
        print("Норма")
    else:
        print("Избыточная масса тела")


# 7
from string import ascii_lowercase, ascii_uppercase, digits
def check_password(password: str) -> None:
    counter = {"lowercase": 0, "uppercase": 0, "digits": 0, "punctuation": 0}
    for char in password:
        match char:
            case char if char in ascii_lowercase:  # abcdefghijklmnopqrstuvwxyz
                counter["lowercase"] += 1
            case char if char in ascii_uppercase:  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
                counter["uppercase"] += 1
            case char if char in digits:  # 0123456789
                counter["digits"] += 1
            case char if char in "!@#$%*":
                counter["punctuation"] += 1
            case _:
                pass
    if (
        len(password) > 9
        and counter["digits"] > 2
        and counter["uppercase"] > 0
        and counter["punctuation"] > 0
    ):
        print("Perfect password")
    else:
        print("Easy peasy")


# 8
def count_letters(phrase: str) -> None:
    counter = {"lowercase": 0, "uppercase": 0}
    for char in phrase:
        match char:
            case char if char.islower():
                counter["lowercase"] += 1
            case char if char.isupper():
                counter["uppercase"] += 1
            case _:
                ...
    print(f"Количество заглавных символов: {counter['uppercase']}")
    print(f"Количество строчных символов: {counter['lowercase']}")
