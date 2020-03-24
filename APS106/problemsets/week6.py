def find_length_using_ints_2(num):
    counter = 0

    while num / 10 >= 0.1:
        num /= 10
        counter += 1

    return counter


def flipper2(number):

    flipped_number = []
    multiple = 1

    for i in range(find_length_using_ints_2(number)):
        flipped_number.append((number // multiple) % 10)
        multiple *= 10

    multiple //= 10

    new_num = 0
    for j in flipped_number:
        j = j * multiple
        new_num += j
        multiple //= 10

    return new_num


def capitalize_string():
    string = input("Enter string: ")
    storage = string.split(" ")

    storage2 = []
    for i in storage:
        storage2.append(i.capitalize())

    string2 = " ".join(storage2)

    print(string2)


def matrix_summer():
    import random

    max_value = int(input("Enter max value: "))
    size = int(input("Enter size: "))

    matrix = []

    total = 0
    counter = 0
    for j in range(size):
        # Make a row
        list1 = []
        for i in range(size):
            list1.append(random.randint(0, max_value))

        # If in the first row or last row:
        if counter == 0 or counter == size-1:
            total += sum(list1)

        # If in any other row
        else:
            total += list1[0]
            total += list1[len(list1)-1]   

        # Append the row to the matrix
        matrix.append(list1)

        counter += 1

    for k in matrix:  # Rows
        string = ""
        for j in k:
            string += str(j)
        print(" ".join(string))

    print('The total is: ' + str(total))
   
  
def matrix_no_repeat():
    import random
    size = int(input("Enter size: "))
    max_val = size ** 2

    numbers_left = []

    for number in range(1, max_val+1):
        numbers_left.append(number)

    matrix = []
    for j in range(size):
        row = []
        for i in range(size):
            found = False
            while not found:
                num = random.randint(1, max_val)
                if num in numbers_left:
                    numbers_left.remove(num)
                    found = True
                else:
                    found = False
            row.append(num)
        matrix.append(row)

    for k in matrix:  # Rows
        print(k)
        





matrix_no_repeat()

























































