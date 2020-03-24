def make_bricks(small, big, goal):
    """
    We want to make a row of bricks that is GOAL inches long. We have a number of small bricks (1 inch each) 
    and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given 
    bricks. This is a little harder than it looks and can be done without any loops
    """

    keep_going = True
    current = 0

    if big*5 + small < goal:
        return False
    else:
        while keep_going:  # While you still wanna loop
            if goal > big:  # check to see if you can actually use big blocks
                if goal >= current + 5 and big > 0:  # check to see if you can place a big block and be in range of goal
                    current += 5  # add a big block to the current chain
                    big -= 1 # take away a big block
                else:
                    keep_going = False
            else:
                keep_going = False

        keep_going = True

        while keep_going:
            if goal > small:  # Check to see if you can use small blocks
                if goal >= current + 1 and small > 0:  # check to see if you can place a small block AND there's enough small blocks
                    current += 1  # add a small block to the current chain
                    small -= 1
                else:
                    keep_going = False
            else:
                keep_going = False

        if current == goal:
            return True
        else:
            return False
