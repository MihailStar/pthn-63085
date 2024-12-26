# 1
print(input().upper())


# 2
print(input().lower())


# 3
print(input().upper() == input().upper())


# 4
string = input()
print(string[:3].upper(), string[3:-3].lower(), string[-3:].upper(), sep="")


# 5
print(input().swapcase())


# 6
print(input().title().swapcase())


# 7
print(input().lower().count("e"))


# 8
print(input().find("a"))


# 9
print(input().rfind("a"))


# 10
print(input().replace(" ", ","))


# 11
print(input().replace("w", "").replace("z", ""))


# 12
print(
    *(
        f".{char}"
        for char in input().lower()
        if char not in ("a", "o", "y", "e", "u", "i")
    ),
    sep="",
)
