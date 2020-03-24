# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name:
# PRA Section:


################################################
# Part 1 - Finding Errors and Debugging
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()

# tell alex where to go
alex.setheading(0)      # make alex face east
alex.down()
alex.circle(100, 360)   # make alex go in a circle with radius of 100 for 180 degrees
alex.left(45)
alex.forward(141.421)

alex.setheading(270)
alex.down()
alex.circle(-50, 180)
alex.circle(50, 90)

alex.setheading(90)
alex.down()
alex.circle(-50, 360)

alex.setheading(180)
alex.down()
alex.circle(50, 90)

alex.left(45)
alex.forward(141.421)
# alex.circle(50, 180)

# alex.circle(100, 180)
# alex.setheading(90)     # make alex face north
# alex.down()             # make alex put pen down
# alex.forward(50)        # make alex go 100 forward
# alex.right(90)          # make alex turn right 90 degree
# alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
# alex.left(90)           # make alex turn to the left for 90 degree
# alex.forward(150)       # make alex go forward 150 steps

# alex.setheading(0)      # make alex face east
# alex.down()             # make alex put pen down
# alex.forward(50)        # make alex go 100 forward
# alex.right(90)          # make alex turn right 90 degree
# alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
# alex.left(90)           # make alex turn to the left for 90 degree
# alex.forward(150)       # make alex go forward 150 steps

# alex.setheading(180)    # make alex face west
# alex.down()             # make alex put pen down
# alex.forward(50)        # make alex go 100 forward
# alex.right(90)          # make alex turn right 90 degree
# alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
# alex.left(90)           # make alex turn to the left for 90 degree
# alex.forward(150)       # make alex go forward 150 steps

# alex.setheading(270)    # make alex face south
# alex.down()             # make alex put pen down
# alex.forward(50)        # make alex go 100 forward
# alex.right(90)          # make alex turn right 90 degree
# alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
# alex.left(90)           # make alex turn to the left for 90 degree
# alex.forward(150)       # make alex go forward 150 steps

################################################
# Part 2 - Draw The Shape In the Handout
################################################
# modify the above code to tell alex
# alex.setheading(0)      # make alex face east
# alex.circle(100, 180)   # make alex go in a circle with radius of 100 for 180 degrees
# TODO: Enter your code here



turtle.done()
