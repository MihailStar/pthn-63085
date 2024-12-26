# 1
x, y = (int(input()) for _ in range(2))
print(f"Точка({x=}, {y=})")


# 2
number_pi = 3.141592653589793
print(f"{number_pi:.6f}")


# 3
print(f"{float(input()):.2f}")


# 4
print(f"{int(input()):010d}")


# 5
print(f"{int(input()):-^15}")


# 6
text = input()
print("|", f"{text:&^20}", "|", sep="")
print("|", f"{text:&>20}", "|", sep="")
print("|", f"{text:&<20}", "|", sep="")
