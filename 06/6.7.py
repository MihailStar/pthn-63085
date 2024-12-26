# 1
workers = {
    "employer1": {"name": "Jhon", "salary": 7500},
    "employer2": {"name": "Emma", "salary": 8000},
    "employer3": {"name": "Brad", "salary": 500},
}
for worker in workers.values():
    if worker["name"] == "Brad":
        worker["salary"] = 8_500
        break
print(workers)


# 2
string = input().lower()
counter = {}
for char in string:
    if not char.isalpha():
        continue
    counter[char] = counter.get(char, 0) + 1
print(counter)


# 3
print("YES" if sorted(input()) == sorted(input()) else "NO")


# 4
morze = {
    "a": "•—",
    "b": "—•••",
    "c": "—•—•",
    "d": "—••",
    "e": "•",
    "f": "••—•",
    "g": "——•",
    "h": "••••",
    "i": "••",
    "j": "•———",
    "k": "—•—",
    "l": "•—••",
    "m": "——",
    "n": "—•",
    "o": "———",
    "p": "•——•",
    "q": "——•—",
    "r": "•—•",
    "s": "•••",
    "t": "—",
    "u": "••—",
    "v": "•••—",
    "w": "•——",
    "x": "—••—",
    "y": "—•——",
    "z": "——••",
}
for word in input().lower().split():
    print(*(morze.get(char) for char in word))


# 5
persons = [
    ("Allison Hill", 334053, "M", "1635644202"),
    ("Megan Mcclain", 191161, "F", "2101101595"),
    ("Brandon Hall", 731262, "M", "6054749119"),
    ("Michelle Miles", 539898, "M", "1355368461"),
    ("Donald Booth", 895667, "M", "7736670978"),
    ("Gina Moore", 900581, "F", "7018476624"),
    ("James Howard", 460663, "F", "5461900982"),
    ("Monica Herrera", 496922, "M", "2955495768"),
    ("Sandra Montgomery", 479201, "M", "5111859731"),
    ("Amber Perez", 403445, "M", "0602870126"),
]
data = {n: {"salary": s, "gender": g, "passport": p} for n, s, g, p in persons}


# 6
data = {
    "my_friends": {
        "count": 10,
        "people": [
            {
                "first_name": "Kurt",
                "id": 621547005,
                "last_name": "Cobain",
                "bdate": "31.8.2005",
            },
            {
                "first_name": "Виолетта",
                "id": 484200150,
                "last_name": "Кастилио",
            },
            {
                "first_name": "Иринка",
                "id": 21886133,
                "last_name": "Бушуева",
                "bdate": "28.8.1942",
            },
            {
                "first_name": "Данил",
                "id": 282456573,
                "last_name": "Греков",
                "bdate": "4.7.2002",
            },
            {
                "first_name": "Валентин",
                "id": 184902932,
                "last_name": "Долматов",
                "bdate": "25.5",
            },
            {
                "first_name": "Евгений",
                "id": 620469646,
                "last_name": "Шапорин",
                "bdate": "6.12.1982",
            },
            {
                "first_name": "Ангелина",
                "id": 622328862,
                "last_name": "Краснова",
                "bdate": "4.11.1995",
            },
            {
                "first_name": "Иван",
                "id": 576015198,
                "last_name": "Вирин",
                "bdate": "2.2.1915",
            },
            {
                "first_name": "Паша",
                "id": 386922406,
                "last_name": "Воронов",
                "bdate": "27.9",
            },
            {
                "first_name": "Ольга",
                "id": 622170942,
                "last_name": "Савченкова",
                "bdate": "20.12",
            },
        ],
    }
}
print(
    *sorted(map(lambda people: people["first_name"], data["my_friends"]["people"])),
    sep="\n",
)
