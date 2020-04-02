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
        return None

    def peek(self):

        # TODO: YOUR CODE HERE
        return None

    def search(self, coordinate):

        # TODO: YOUR CODE HERE
        return None

    def is_empty(self):

        if self.size == 0:
            return True
        else:
            return False


s = Stack()
s.push(((4,1),{"U":False,"D":False,"R":False,"L":False}))
s.push(((8,1),{"U":False,"D":False,"R":False,"L":False}))

print(s)