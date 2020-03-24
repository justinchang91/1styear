def sum_odd(number):
    total = 0
    for i in range(number+1):  # Could have modified this so it starts at 1, ends at num+1 and steps every 2
        if i % 2 != 0:
            total += i

    return total


def multiple_finder(storage):
    unique_storage = []
    for i in storage:

        if unique_storage.count(i) == 0:
            if storage.count(i) > 1:
                unique_storage.append(i)

    unique_storage = set(unique_storage)
    return unique_storage


print(multiple_finder([2,3,4,5,1, 6,2,2,4,4,5,5,6]))






