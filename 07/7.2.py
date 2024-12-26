# 1
def repeat_please_n_times(n: int) -> None:
    for _ in range(n):
        print("Just do it")


# 2
def is_between(a: float, b: float, c: float) -> None:
    print(b >= a >= c or b <= a <= c)
is_between(*map(int, input().split()))


# 3
def count_letter(text: str, letter: str) -> None:
    print(text.count(letter))
count_letter(input(), input())


# 4
def print_initials(name: str, surname: str, middlename: str) -> None:
    print(f"{surname.title()} {name[0].upper()}.{middlename[0].upper()}.")
print_initials(input(), input(), input())
