import math

print(math.sin(math.pi/2))  # math takes in radians

string = "word"

print(string[-1])

print(string[0])

print(string[1:-1])  # For slicing, the slice starts with the value at index 1 (inclusive) and ends at the last value
# (not inclusive)

print(string[len(string)::-1])  # Take every item from last term to the first term, make sure the steps are negative
# since you're going backwards
print(string[:len(string):1])  # Slices from 0 inclusive to string length (exclusive)
# take every item from 0 to string length


# Python slicing works like this ---> slice[start:end:step] default for step is 1
print(19 % 10)  # For mod, just subtract the number from the original number
# until you can't and then whatever left is the result

print(23%2)

print(9 // 10)
print(99 // 100)

import math


def magnitude(x, y):
    r = math.sqrt(x**2 + y ** 2)
    return r


print(str(magnitude(2, 4)))


def phase(x, y):
    r = math.atan(y/x)
    return r


def other(x, y):
    r = math.atan2(y, x)
    return r


print(str(phase(-4, 2)))
print(str(other(-4, -2)))


print(int(0.9983))

foo = "23.5340934"

print(foo.split('.')[0])
print(foo.split('.')[1])

print(foo.split('.'))


print(foo.find("."))

poo = "derpa.skull@mail.utoronto.ca".split(".")

print(poo)

first = poo[0]
last = poo[1].split("@")[0]

last = last.upper()
first = first.upper()

print(last + "," + first)

scores = "10.0,20.0,30.0,0.0"

scores.split(",")[0]
scores.split(",")[1]
elements = scores.split(",")

average = (float(elements[0]) + float(elements[1]) + float(elements[2]))/3

print(max(elements))


elements = scores.split(",")        # Split the scores by comma into 4 individual elements
print(elements)
f_elements = []                                             # Create a new empty list
for x in elements:                                          # Use a for loop to fill new list with float scores
    f_elements.append(float(x))                             # for loop loops through the actual elements, in elements

print(f_elements)

average = sum(f_elements) / len(f_elements)                 # Calculate the average

print(average)

high = float(max(elements))
low = float(min(elements))

print(high - low)

email = "anna.conda@mail.utoronto.ca"
elements = email.split(".")
first = elements[0]
last = elements[1].split("@")[0]

first = first.upper()
last = last.upper()

print(last + "," + first)

print(elements[1])

print(1 // 10)

print(id(34))

red = 34

print(id(red))

red = 28

print(id(red))
print("""
You suck! \n
You're gay \n
You eat poo


""")

print(53//24)

poo = "hello I need to poo"
print(poo.capitalize())

print("\"it's raining\"")
print('it\'s raining')

print('"\\" is the backslash')

print(ord("6"))
print(chr(90))

number = 1



