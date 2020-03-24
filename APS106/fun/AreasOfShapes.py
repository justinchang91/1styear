import math


def area_of_triangle(base, height):
    """
    Calculates area of triangle
    """
    area = (float(base)*float(height))/2

    print("The area is " + str(area))


def area_of_rectangle(length, width):
    """
    Calculates area of rectangle
    """
    area = float(length) * float(width)
    print("The area is " + str(area))


def area_of_circle(radius):
    """
    Calculates area of circle
    """
    area = math.pi * (float(radius)) ** 2
    print("The area is " + str(area))


def go_again():
    """
    Asks user if they would like to preform another calculation
    """
    answer = input("Calculate another area? (yes/no): ")
    answer = answer.lower()

    if answer == "no":
        return False
    else :
        return True


again = True

while again:

    shape = input("What shape would you like to calculate the area of? ")
    shape = shape.lower()
    print(shape)

    if shape == "triangle":
        inputBase = input("Enter base: ")
        inputHeight = input("Enter height: ")
        area_of_triangle(inputBase, inputHeight)
        again = go_again()

    elif shape == "rectangle":
        inputLength = input("Enter length: ")
        inputWidth = input("Enter width: ")
        area_of_rectangle(inputLength, inputWidth)
        again = go_again()

    elif shape == "circle":
        inputRadius = input("Enter radius: ")
        area_of_circle(inputRadius)
        again = go_again()

    else:
        print("Invalid request")
        again = go_again()












