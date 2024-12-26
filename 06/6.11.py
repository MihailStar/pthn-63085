# 1
set_a = {
    31,
    37,
    39,
    41,
    47,
    58,
    60,
    62,
    70,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    85,
    86,
    88,
    90,
    93,
    96,
    98,
    99,
}
set_b = {
    0,
    1,
    8,
    16,
    17,
    18,
    22,
    24,
    29,
    31,
    33,
    34,
    36,
    42,
    46,
    47,
    51,
    53,
    62,
    64,
    65,
    66,
    67,
}
print(len(set_a.intersection(set_b)))


# 2
print(len(set_a.union(set_b)))


# 3
print(len(set_a.difference(set_b)))
print(len(set_b.difference(set_a)))


# 4
print(len(set_a.symmetric_difference(set_b)))


# 5
words = [
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
]
print(len(set(word for word in words if len(word) > 6)))


# 6
for _ in range(int(input())):
    print(len(set(input().split())))
