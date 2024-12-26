# 1
my_set = {
    "government",
    "control",
    "winter",
    "few",
    "generation",
    "service",
    "national",
    "tradition",
    "government",
}
my_set.update({"concert", "brown", "jacket", "value"})


# 2
my_set = {
    "mention",
    "soup",
    "pneumonia",
    "tradition",
    "concert",
    "tease",
    "generation",
    "winter",
    "national",
    "jacket",
    "winter",
    "wrestle",
    "proposal",
    "error",
    "pneumonia",
    "concert",
    "value",
    "value",
    "disclose",
    "glasses",
    "tank",
    "national",
    "soup",
    "feel",
    "few",
    "concert",
    "wrestle",
    "proposal",
    "soup",
    "sail",
    "brown",
    "service",
    "proposal",
    "winter",
    "jacket",
    "mention",
    "tradition",
    "value",
    "feel",
    "bear",
    "few",
    "value",
    "winter",
    "proposal",
    "government",
    "control",
    "value",
    "few",
    "generation",
    "service",
    "national",
    "tradition",
    "government",
    "mention",
    "proposal",
}
for item in {"government", "national", "tease"}:
    my_set.remove(item)


# 3
my_set = {
    "mention",
    "soup",
    "pneumonia",
    "tradition",
    "concert",
    "tease",
    "generation",
    "winter",
    "national",
    "jacket",
    "winter",
    "wrestle",
    "proposal",
    "preference",
    "fascinate",
    "earthflax",
    "meadow",
    "bitter",
    "march",
    "feel",
    "wind",
    "location",
    "need",
    "adviser",
    "error",
    "pneumonia",
    "concert",
    "value",
    "value",
    "disclose",
    "glasses",
    "tank",
    "national",
    "soup",
    "feel",
    "few",
    "concert",
    "wrestle",
    "proposal",
    "soup",
    "sail",
    "brown",
    "service",
    "proposal",
    "winter",
    "jacket",
    "mention",
    "tradition",
    "value",
    "feel",
    "bear",
    "few",
    "value",
    "winter",
    "proposal",
    "government",
    "control",
    "value",
    "few",
    "generation",
    "service",
    "national",
    "tradition",
    "government",
    "mention",
    "proposal",
    "sunrise",
    "refund",
    "formulate",
    "despise",
    "hobby",
    "noble",
    "parameter",
    "update",
    "serious",
    "potential",
    "entry",
    "week",
    "tenant",
    "debut",
    "dentist",
    "explode",
    "default",
    "slam",
}
for item in {"noble", "offend", "error", "eagle", "sail"}:
    my_set.discard(item)


# 4
set_from_lists = set[str]()
for _ in range(int(input())):
    set_from_lists.update(input().split())
print(len(set_from_lists))


# 5
cache = set[str]()
for phrase in input().split(","):
    lower_phrase = phrase.lower()
    if lower_phrase in cache:
        print("ДА")
        continue
    print("НЕТ")
    cache.add(lower_phrase)


# 6
a, b = input().split(), input().split()
print(*sorted(set(a).intersection(b), key=int))


# 7
a, b = input().split(), input().split()
print(*sorted(set(a).difference(b), key=int))


# 8
from collections import Counter
more_1 = sorted(
    pair[0]
    for pair in Counter(int(char) for char in input() if char.isdigit()).most_common()
    if pair[1] > 1
)
if more_1:
    print(*more_1)
else:
    print("NO")


# 9
cache = set[str]()
for char in input():
    if char in cache:
        continue
    print(char, end="")
    cache.add(char)
