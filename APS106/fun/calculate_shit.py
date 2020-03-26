list1 = []
coordinate = []
for t in range(-5, 6, 1):
    coordinate = [t ** 2, 3 - 2 * (t ** 2), 1 + 2 * (t ** 2)]
    list1.append(coordinate)

for thing in list1:
    print(thing)

