# 1
my_tuple = (32, 27)
print(my_tuple[44])
print(my_tuple[-9])


# 2
my_tuple = (32, 27)
print(my_tuple[5:10+1])
print(my_tuple[20:])
print(my_tuple[:35])


# 3
my_tuple = (32, 27)
print(my_tuple[::-1])


# 4
my_tuple = (32, 27)
print(my_tuple.count(50))


# 5
words_tuple = (
    "quaint",
    "leftovers",
    "thesis",
    "density",
    "retired",
    "weak",
    "tolerate",
    "sensitivity",
    "primary",
    "definition",
    "determine",
    "bring",
    "monstrous",
    "hurl",
    "timetable",
    "month",
    "advocate",
    "provoke",
    "stress",
    "omission",
)
for word in words_tuple:
    print(f"Длина слова {word} = {len(word)}")


# 6
from statistics import mean
my_tuple = (-214, 29)
print(float(mean([n for n in my_tuple if n % 2 == 1])))
