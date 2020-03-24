import math

# 1
print("1")
print("I am going to love this course")

# 2
largest3 = 999
smallest5 = 10000
sumDigits = largest3 + smallest5
print()
print(2)
print(largest3)
print(smallest5)
print(sumDigits)

# 3
cost = input("What is the cost of the item? (In $)")
numberOf = input("How many item(s)")

totalCost = float(cost)*float(numberOf)
print("The total cost is $" + str(totalCost))

# 4
CorF = input("Enter 1 for celsius to fahrenheit or 2 for vice versa")

if int(CorF) == 2:
    fahrenheit = input("Enter temperature in fahrenheit")
    celsius = (int(fahrenheit) - 32)*(5/9)
    print("The temperature in celsius would be " + str(math.trunc(celsius)) + " degrees")


elif int(CorF) == 1:
    celsius = input("Enter temperature in celsius")
    fahrenheit = int(celsius)*(9/5) + 32
    print("The temperature in fahrenheit would be " + str(math.trunc(fahrenheit)) + " degrees")

else:
    print("Invalid choice. Shutting down (until loops get implemented")

# 5
x = input("Please input a value for x: ")
y = 4*float(x) + 3
round(y,2)
print("The value of y = 4x+3 is " + str(y))