# 1
colors = ["White", "Blue", "Yellow", "Purple", "Black", "Green"]
sizes = ["S", "M", "L", "XL", "XLL"]
print([(c, s) for c in colors for s in sizes])

# 2
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([coordinate for point in vector for coordinate in point])
