import math
from decimal import Decimal


def flipping_numbers():  # Question 1

    number = input("Enter a positive number less than 1000: ")

    # Method 1 with strings

    if len(number) == 2:
        print("The number flipped is: " + number[len(number)::-1] + "0")

    elif len(number) == 1:
        print("The number flipped is: " + number[len(number)::-1] + "00")

    else:
        print("The number flipped is: " + number[len(number)::-1])

    # Method 2 with integers

    number1 = int(number)

    if number1 // 10 == 0:   # if the number is only 1 digit
        ones = (number1 % 100) % 10
        print("The number flipped is : " + str(ones) + "00")

    elif number1 // 100 == 0:   # if the number is 2 digits
        tens = (number1 % 100) // 10
        ones = (number1 % 100) % 10
        print("The number flipped is: " + str(ones) + tens + "0")

    else:   # the number is 3 digits
        hundreds = number1 // 100  # integer division
        tens = (number1 % 100) // 10  # This will get you the tens and ones number but
        # then you integer divide by 10 to get just the tens
        ones = (number1 % 100) % 10 # This will get you the tens and ones number but
        # then you mod again but by 10 this time to get just the ones
        print("The number flipped is : " + str(ones) + str(tens) + str(hundreds))


def number_of_coins():  # Question 2

    amount = input("Enter an amount: ")
    amount = int(amount)

    num_quarters = amount // 25
    amount = amount % 25

    num_dimes = amount // 10
    amount = amount % 10

    num_nickels = amount // 5
    amount = amount % 5

    num_pennies = amount // 1

    print(str(num_quarters) + " quarter(s), " + str(num_dimes) + " dime(s), " + str(num_nickels) + " nickel(s) "
          + str(num_pennies) + " penny(ies)")


def min_coins(change):  # Question 2 but with parameter, no input
    
    change = change * 100

    num_quarters = change // 25
    change = change % 25

    num_dimes = change // 10
    change = change % 10

    num_nickels = change // 5
    change = change % 5

    num_nickels = num_nickels + 1

    print(str(num_quarters) + " quarter(s), " + str(num_dimes) + " dime(s), " + str(num_nickels) + " nickel(s)")


def truncate_and_round():  # Question 3

    def truncate(n, decimals):
        multiplier = 10 ** decimals
        truncated_number = int(n * multiplier) / multiplier
        return truncated_number

    float_num = input("Enter a float: ")

    num1 = truncate(float(float_num), 1)
    num2 = round(float(float_num), 1)

    print(num1)
    print(num2)


def sin_cos_tan():  # Question 4

    angle = input("Enter an angle in degrees: ")
    angle = float(math.radians(angle))  # convert angle to radians

    sin = math.sin(angle)
    cos = math.cos(angle)
    tan = math.tan(angle)

    print("sin(" + str(angle) + ") is " + str(sin))
    print("cos(" + str(angle) + ") is " + str(cos))
    print("tan(" + str(angle) + ") is " + str(tan))


def store_clerk():  # Question 5, 6, 7
    cost = float(input("Enter cost of the item: "))
    paid = float(input("Amount tendered: "))

    if paid > cost:
        change = paid - cost
        str_decimal = str(change).split(".")[1]
        str_number = str(change).split(".")[0]

        if len(str_decimal) < 2:  # The decimal is less than 2
            print("Change: " + str(change) + "0")  # Add a zero
            min_coins(change)
        elif len(str_decimal) > 2:
            new_decimal = str_decimal[:2:]
            print("Change: " + str_number + "." + new_decimal)
            min_coins(change)
        else:
            print("Change: " + str(change))
            min_coins(change)
    else:
        due = cost - paid

        str_decimal = str(due).split(".")[1]
        str_number = str(due).split(".")[0]

        if len(str_decimal) < 2:
            print("Still due: " + str(due) + "0")
        elif len(str_decimal) > 2:
            new_decimal = str_decimal[:2:]
            print("Still due: " + str_number + "." + new_decimal)
        else:
            print("Still due: " + str(due))


store_clerk()

