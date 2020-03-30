import csv

# Load the maze
filename = open("solvable_maze1.csv")
maze_reader = csv.reader(filename)
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

print("Start coordinate: " + str(start))
print("End coordinate: " + str(end))


# Print the maze (There is a function for this on the actual lab)
for i in maze1:
    row = ""
    for j in i:
        row += j
    print(row)


maze2 = []
for i in maze1:
    maze2.append(list(i))

path1 = [start]
end1 = end


def solve(maze, path, end):
    current = path[-1]
    maze1_pos = maze[current[0]][current[1]]
    maze2_pos = maze2[current[0]][current[1]]

    # Bases
    if maze1_pos == "X" or maze2_pos == "T":
        return False

    if maze1_pos == "E":
        return True

    if path.count(current) > 1:
        return False

    # Down
    if current[0] + 1 < len(maze):
        path.append((current[0] + 1, current[1]))
        if solve(maze, path, end):
            return True
        else:
            del path[-1]

    # Right
    if current[1] + 1 < len(maze[0]):
        path.append((current[0], current[1] + 1))
        if solve(maze, path, end):
            return True
        else:
            del path[-1]

    # Up
    if current[0] - 1 >= 0:
        path.append((current[0] - 1, current[1]))
        if solve(maze, path, end):
            return True
        else:
            del path[-1]

    # Left
    if current[1] - 1 > -1:
        path.append((current[0], current[1] - 1))
        if solve(maze, path, end):
            return True
        else:
            del path[-1]

    # If all options don't work, its a dead end. Mark and backtrack.
    if maze[current[0]][current[1]] == "S":
        del path[-1]
    maze2[current[0]][current[1]] = "T"
    return False


print(solve(maze1, path1, end1))
print(path1)