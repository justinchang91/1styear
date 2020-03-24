def main():  # 1
    valid = False

    while not valid:
        number = int(input("Enter an odd, positive integer: "))

        if number % 2 == 0 or number == 0:  # if the number is not odd
            valid = False
        else:  # if the number is odd
            valid = True

    print("The sum of the odds is: " + str(sum_odd(number)))


def sum_odd(number):  # Part of 1
    number_list = []
    for i in range(1, number+1):
        number_list.append(i)

    total = 0
    for j in number_list:
        if j % 2 != 0:  # then number is odd
            total += j

    return total


def integer_asker():  # 2
    done = False
    positives = 0
    negatives = 0

    while not done:
        number = int(input("Enter an integer: "))

        if number == 0:
            done = True

        else:

            if number > 0:
                positives += 1
            else:
                negatives += 1

            done = False

    print("You entered " + str(positives) + " positive and " + str(negatives) + " negative values.")


def evaluate_tanh():
    valid = False
    while not valid:
        x = float(input("Enter an x value: "))
        n = int(input("Enter the number of elements (n): "))

        if x >= 1 or x <= -1 or n < 5:
            print("Invalid input. Try again.")
            valid = False
        else:
            valid = True

    exponent = 1
    tanh = 0

    for i in range(n):
        tanh += (x ** exponent)/exponent
        exponent += 2

    print("The approximation is: " + str(tanh))


def binary_search(array, value):
    pointer = len(array) // 2
    found = False
    max_value = len(array)
    min_value = 0

    while not found:
        if array[pointer] == value:
            return array.index(array[pointer])
            found = True
        elif array[pointer] < value:
            min_value = pointer
            pointer = (min_value + max_value) // 2
            found = False
        else:
            max_value = pointer
            pointer = (min_value + max_value) // 2
            found = False


def find_dups(list1):
    list2 = []
    for i in list1:
        if list1.count(i) > 1 and i not in list2:
            list2.append(i)
    set1 = set(list2)
    return set1


def find_multiples(list1, k):
    dict1 = {}
    list2 = []
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for j, p in dict1.items():
        print(j, p)
        if p >= k:
            list2.append(j)

    return set(list2)


def mating_pairs(males, females):
    list1 = []
    for i in range(len(males)):
        couple = (males.pop(), females.pop())
        list1.append(couple)

    return set(list1)


def convert_list(list1):
    dict1 = {}
    for i in range(0, len(list1), 2):
        dict1[list1[i]] = list1[i+1]

    return dict1


def letter_count():
    word = input("Enter a word: ")
    word = word.lower()

    dict1 = {}

    for i in word:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    letter = ""
    counter = 0

    for letters, count in dict1.items():
        if counter < count:
            counter = count
            letter = letters

    print("The letter " + letter + " appears most often: " + str(counter) + " time(s).")


letter_count()



