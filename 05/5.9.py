# 1
zeroes = [0 for _ in range(100)]


# 2
print([n for n in range(1, int(input()) + 1)])


# 3
names = ["Alice", "Bob", "Marry", "Joe", "Hilary", "Stevia", "Dylan", "Kevin", "Darvin"]
print(list(map(lambda name: "My name is {name}".format(name=name), names)))


# 4
print([x * x for x in range(15) if x % 2 == 0])


# 5
n = int(input())
print([d for d in range(1, n + 1) if n % d == 0])


# 6
n = int(input())
print([d for d in range(n if n % 2 else n + 1, n**2 + 1, 2)])


# 7
a, b = map(int, input().split())
print(
    [n**2 for n in range(a, b + 1)]
    if a <= b
    else [n**3 for n in range(b, a - 1, -1)]
)


# 8
st = "Create a list of the first letters of every word in this string"
print([w[0] for w in st.split()])


# 9
from string import ascii_uppercase
print([ascii_uppercase[i] for i in range(0, int(input()))])


# 10
from string import ascii_uppercase
print([ascii_uppercase[i] * (i + 1) for i in range(0, int(input()))])


# 11
print([(i, j) for i in range(1, 4) for j in range(1, 5)])


# 12
phrase = "Take only the words that start with t in this sentence"
print([w for w in phrase.split() if w.startswith(("t", "T"))])
