# 1

marks = [
        [["Mohamed"], ["A", "A+", "C", "FZ", "B-"]],
         [["Cindy"], ["B", "B", "C", "A", "B"]],
         [["Mustafa"], ["A", "A+", "A+", "C", "C"]],
         [["Stefan"], ["FZ", "B", "B", "C", "C"]]]


def mark_book(data_set, grade):
    students = []

    for i in data_set:
        for j in i[1]:
            if j == grade.upper():
                if i[0] not in students:
                    students.append(i[0])

    return students


print(mark_book(marks, "A"))


# 2

def upper_lower_conversion(string):
    new_string = ""

    for i in string:
        if i == i.upper():  # check if upper case
            new_string += i.lower()
        else:
            new_string += i.upper()

    return new_string


print(upper_lower_conversion("derp"))


# 3

def double_reversal(string, stepper):
    substrings = []
    complete = False
    start = 0
    end = stepper

    if len(string) % stepper == 0:

        while not complete:

            substrings.append(string[start:end])
            start += stepper
            end += stepper

            if start == len(string):
                complete = True

    else:
        return "Invalid input. String length must be divisible by k"

    new_substrings = []
    for i in substrings:
        new_substrings.append(i[::-1])

    new_substrings.reverse()

    string_version = ""
    for j in new_substrings:
        string_version += j + " "

    print(string_version)


double_reversal("university", 2)


# 4

def short_strings():
    n = int(input("How many strings: "))
    k = int(input("How many characters in a short string: "))
    counter = 1
    done = False
    storage = []

    while not done:
        string = input("Please enter string " + str(counter) + ": ")

        if len(string) <= k:
            storage.append(string)

        counter += 1

        if counter > n:
            done = True

    storage.reverse()
    storage_in_string = ", ".join(storage)

    print(storage_in_string)


# 5

def take_out_expression():
    string = input("Enter a string: ")

    new_string = ""
    for i in string:
        if i != "!" and i != "?":
            new_string += i

    print(new_string)


