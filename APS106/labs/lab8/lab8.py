##############################################
# APS106 Winter 2020 - Lab 8 - Maze Solver   #
##############################################

##############################################
# Helper functions
#
# These are provided to help you complete
# the lab. 
#
# YOU DO NOT NEED TO EDIT THIS FUNCTION 
##############################################

def print_maze(maze):
    """
    (tuple) -> None
    
    Input is a nested tuple representing a
    maze. Function prints the maze.
    
    """
    
    for row in maze:
        print("".join(row))
    

###########################################
# PART 1 - Read the maze from csv file    #
###########################################

import csv

def load_maze(filename):
    """
    (str) -> Maze-Tuple, Start-Coordinate, End-Coordinate
    
    Open a csv file containing a maze represented by ascii characters
    and return a nested tuple with each element representing a different
    square within the maze.
    
    Additionally, return the location of the start and end positions of the 
    maze as tuples representing x,y coordinates.
    
    For example, for the following maze:
        
        XXXXXXXXXXXXXXXXXX
        XOXOOOOOOOOOOOXOOE
        XOOOXOOXXXXXXOOOXX
        XXXOXXXXXXXXXXXXXX
        XOOOOOXXOOXXXXXXXX
        XXXXXOOOOXOOOOOXXX
        XXXXXXXOOOOXOXXXXX
        XXXXXXXXXXXXSXXXXX
    
    >>> load_maze_from_file(maze_file)
    ((('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'E'), 
    ('X', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X'), 
    ('X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'S', 'X', 'X', 'X', 'X', 'X')), 
    (7, 12), (1, 17))
        
    
    You may assume the following:
        1. Each line of the csv file has the same number of columns
        2. Each file will contain one and only one starting location ("S")
        3. Each file will contain one and only one exit location ("E")
        4. Each cell of the csv file will contain a single character
        
    """
    
    ## TODO - YOUR CODE HERE
    file = open(filename)
    maze_reader = csv.reader(file)
    maze1 = []

    # Get the maze tuple
    for row in maze_reader:
        maze1.append(tuple(row))

    # Find start and end coordinate
    start = ()
    end = ()
    for i in range(len(maze1)):
        for j in range(len(maze1[0])):
            if maze1[i][j] == "S":
                start = (i, j)
            elif maze1[i][j] == "E":
                end = (i, j)

    return tuple(maze1), start, end


###########################################
# PART 2 - Recursively solve the maze     #
###########################################

def solve_maze(maze,path,end):
    """
    (tuple,list,tuple) -> bool
    
    maze - a 2D tuple containing the characters defining the maze indexed by
            row and column
    path - a list of coordinates defining the current search path
    end  - the coordinate of the maze exit

    Recursively solve the maze stored as a 2D tuple of ASCII characters.
    Characters have the following meanings:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location 
    
    You may only move in horizontal or vertical directions. That is, the
    solution path, if it exists, should not contain any diagonal movements.
    
    The solution path, if it exists, should begin at the current location
    and end at the exit point.
    
    If no path exists, the path should be empty and the function should
    return "False"
    """
    
    ## TODO: YOUR CODE HERE

    current = list(path[-1])
    maze_pos = maze[current[0]][current[1]]

    if maze_pos == "E":
        return True

    elif maze_pos == "X" or path.count(current) > 1:
        del path[-1]

    else:

        previous = current
        while current != end:
            # Go up
            if current[0] - 1 >= 0 and current[0] - 1 != previous[0]:  # Make sure you're within the maze
                path.append([current[0] - 1, current[1]])
                if solve_maze(maze, path, end):
                    return True

            # Go right
            if current[1] + 1 < len(maze[0]) and current[1] + 1 != previous[1]:
                path.append([current[0], current[1] + 1])
                if solve_maze(maze, path, end):
                    return True

            # Go left
            if current[1] - 1 > -1 and current[1] - 1 != previous[1]:

                path.append([current[0], current[1] - 1])

                if solve_maze(maze, path, end):
                    return True

            # Go down
            if current[0] + 1 < len(maze) and current[0] + 1 != previous[0]:

                path.append([current[0] + 1, current[1]])

                if solve_maze(maze, path, end):
                    return True

            previous = path[-1]

            del path[-1]

            current = path[-1]

            return False
