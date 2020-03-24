import math


def final_loc(l1, l2, a1, a2):
    """
    Float ---> float
    returns (x,y) coordinates for final location of robotic arm
    """

    # define parameters

    length1 = l1
    length2 = l2
    theta1 = a1 * math.pi / 180
    theta2 = a2 * math.pi / 180

    # find location (x1,y1)

    x1 = length1 * math.cos(theta1)
    y1 = length1 * math.sin(theta1)

    # find difference between (x1,y1) and final location

    x2 = length2 * math.cos(theta1 + theta2)
    y2 = length2 * math.sin(theta1 + theta2)

    # find final location

    x = x1 + x2
    y = y1 + y2

    # print results

    print("x = " + str(x))
    print("y = " + str(y))


final_loc(2, 3, 30, 60)

