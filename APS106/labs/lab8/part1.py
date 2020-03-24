import csv

# PART 1: LOADING THE MAZE

filename = open("solvable_maze1.csv")
maze_reader = csv.reader(filename)
maze = []

# Get the maze tuple
for row in maze_reader:
    maze.append(tuple(row))

print("Maze tuple: " + str(tuple(maze)))


# Find start and end coordinate
start = ()
end = ()
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start = (i, j)
        elif maze[i][j] == "E":
            end = (i, j)

print("Start coordinate: " + str(start))
print("End coordinate: " + str(end))


# Print the maze (There is a function for this on the actual lab)
for i in maze:
    row = ""
    for j in i:
        row += j
    print(row)






