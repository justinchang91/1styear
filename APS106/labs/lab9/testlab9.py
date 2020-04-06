class Node:
    """
    Node object for LinkedList
    """

    def __init__(self, cargo=None, next=None):
        """
        Create and initialize a Node object

        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        self.cargo = cargo
        self.next = next

    def __str__(self):
        """
        (Node) -> str

        Return a string representation of the node

        You may use this to print a visualization of a node

        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """

        neighbours_explored = ''
        for n in self.cargo[1]:
            if self.cargo[1][n]:
                neighbours_explored += (n + ' ')

        box_width = len("Neighbours Explored: ")
        pad1 = box_width - len("Coordinate Node")
        pad2 = box_width - len("Coordinate: ") - len(str(self.cargo[0]))
        pad3 = box_width - len(neighbours_explored)

        s = ('+' + '-' * box_width + '+\n' +
             '|' + 'Coordinate Node' + ' ' * pad1 + '|\n' +
             '+' + '-' * box_width + '+\n' +
             '|' + 'Coordinate: ' + str(self.cargo[0]) + ' ' * pad2 + '|\n' +
             '+' + '-' * box_width + '+\n'
                                     '|' + 'Neighbours Explored: ' + '|\n' +
             '|' + neighbours_explored + ' ' * pad3 + '|\n' +
             '+' + '-' * box_width + '+\n')
        return s


class Stack:
    """
    LinkedList with stack behaviour
    """

    def __init__(self):
        """
        Create and initialize an empty stack

        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        self.size = 0
        self.top = None

    def __str__(self):

        node = self.top

        if not self.is_empty():
            nodes_str = " " * 9 + "Top\n" + 10 * " " + "|\n" + 10 * " " + "V\n"
            while node != None:
                nodes_str += str(node)
                if node.next != None:
                    # add an arrow
                    arrow = 10 * " " + "|\n" + 10 * " " + "V\n"
                    nodes_str += arrow
                node = node.next
        else:
            nodes_str = ""

        return "Stack:\nsize : " + str(self.size) + "\nNodes: \n" + nodes_str

    def push(self, cargo):

        # TODO: YOUR CODE HERE
        new_node = Node(cargo)
        if self.size == 0:  # if it's an empty stack
            new_node.next = None  # There is no next node
            self.top = new_node  # top becomes this node
            self.size += 1
        else:
            new_node.next = self.top  # connect the new node to the top
            self.top = new_node  # make this new node the top
            self.size += 1

    def pop(self):

        # TODO: YOUR CODE HERE
        to_be_removed = self.top  # access the top node
        self.top = to_be_removed.next  # make the next node the top node
        to_be_removed.next = None  # Make the original top node linked to nothing
        self.size -=1
        return to_be_removed.cargo

    def peek(self):

        # TODO: YOUR CODE HERE
        return self.top.cargo

    def search(self, coordinate):

        # TODO: YOUR CODE HERE
        current_node = self.top  # start at the top
        while current_node.next is not None:
            if current_node.cargo[0] == coordinate:  # if the coordinate is found in the linked list, return True
                # use node.cargo to access the cargo, then index the cargo
                return True
            current_node = current_node.next  # shuffle to the next node

        return False  # if you can't find the thing

    def is_empty(self):

        if self.size == 0:
            return True
        else:
            return False


def print_maze(maze):
    """
    (tuple) -> None

    Input is a nested tuple representing a
    maze. Function prints the maze.

    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """

    for row in maze:
        print("".join(row))


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

    Will return:


    You may assume the following:
        1. Each line of the csv file has the same number of columns
        2. Each file will contain one and only one starting location ("S")
        3. Each file will contain one and only one exit location ("E")
        4. Each cell of the csv file will contain a single character


    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """

    # start with a list of coordinates
    maze = []
    start_position = None
    exit_position = None

    # open the file for reading
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        row = 0
        for line in csv_reader:
            # create a tuple of the values within the row
            maze_row = tuple(line)

            # add the row to the maze
            maze.append(maze_row)

            # check if the row contains the start and/or end positions
            if "S" in maze_row:
                col = maze_row.index("S")
                start_position = (row, col)

            if "E" in maze_row:
                col = maze_row.index("E")
                exit_position = (row, col)

            row += 1

    # convert the maze to a tuple
    maze = tuple(maze)

    return maze, start_position, exit_position


def valid_path_coordinate(maze, coord):
    """
    (maze-tuple, coordinate-tuple) -> bool

    Checks if the input coordinate is a valid path position
    in the maze. Maze characters have the following meaning:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location

    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """

    # check if the coordinate is out-of-bounds
    if (coord[0] < 0 or coord[0] >= len(maze)) or \
            (coord[1] < 0 or coord[1] >= len(maze[0])):
        return False

    # check if the coordinate is a wall
    if maze[coord[0]][coord[1]] == "X":
        return False

    # all other squares are valid
    return True


# Loadeth the mazeth
(maze1, start_pos, end_pos) = load_maze("unsolvable_maze1.csv")


def solve_maze(maze, start, end):
    # Initialize the empty stack
    path = Stack()

    # Push the start position
    start_pos_data = (start, {"L": False, "R": False, "U": False, "D": False})
    path.push(start_pos_data)

    # Algorithm

    while path.peek()[0] != end:

        # Get current position
        current_position = path.peek()

        # Check if this is the end


        # Check if directions have been explored

        # Explore up:
        if not current_position[1]["U"]:
            next_square = (current_position[0][0] - 1, current_position[0][1])

            # Check the next square:
            if valid_path_coordinate(maze, next_square) and not path.search(next_square):  # if the next square is valid
                path.push((next_square, {"U": False, "D": True, "L": False, "R": False})) # D is true cuz u already were there

            current_position[1]["U"] = True

        # Explore down:
        elif not current_position[1]["D"]:
            next_square = (current_position[0][0] + 1, current_position[0][1])

            # Check the next square:
            if valid_path_coordinate(maze, next_square) and not path.search(next_square):  # if it's true
                path.push((next_square, {"U": True, "D": False, "L": False, "R": False})) # U is true cuz u already were there

            current_position[1]["D"] = True

        # Explore left:
        elif not current_position[1]["L"]:
            next_square = (current_position[0][0], current_position[0][1] - 1)

            # Check the next square:
            if valid_path_coordinate(maze, next_square) and not path.search(next_square):  # if it's true
                path.push((next_square, {"U": False, "D": False, "L": False, "R": True}))  # U is true cuz u already were there

            current_position[1]["L"] = True

        # Explore right:
        elif not current_position[1]["R"]:
            next_square = (current_position[0][0], current_position[0][1] + 1)

            # Check the next square:
            if valid_path_coordinate(maze, next_square) and not path.search(next_square):  # if it's true
                path.push((next_square, {"U": False, "D": False, "L": True, "R": False})) # U is true cuz u already were there

            current_position[1]["R"] = True

        # If none of the options work:
        else:
            path.pop()

            # If the stack is empty:
            if path.size == 0:
                return False, path

    # If it exits the while loop, it means there's a solution

    return True, path


print(solve_maze(maze1, start_pos, end_pos))

s = Stack()
data1 = ((2,1),{"U":False,"D":False,"R":False,"L":False})
data2 = ((2,2),{"U":False,"D":False,"R":False,"L":False})

s.push(data1)
s.push(data2)
popped = s.pop()
print(popped)
peeked = s.peek()
print(peeked)
