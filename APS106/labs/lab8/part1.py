import csv

# PART 1: LOADING THE MAZE

filename = open("solvable_maze2-1.csv")
maze_reader = csv.reader(filename)
maze1 = []

# Get the maze tuple
for row in maze_reader:
    maze1.append(tuple(row))

print("Maze tuple: " + str(tuple(maze1)))


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


# PART 2: Solve the maze
path1 = [start]
print()
def derp(maze, path, end):
    current = list(path[-1])

    print("The current coordinate is: " + str(current))
    maze_pos = maze[current[0]][current[1]]
    print("Your are at: " + str(maze_pos))

    if maze_pos == "E":
        return True

    elif maze_pos == "X" or path.count(current) > 1:
        print("Deleting " + str(path[-1]))
        del path[-1]

    else:

        previous = current
        while current != end:
            # Go up
            if current[0] - 1 >= 0 and current[0] - 1 != previous[0]:  # Make sure you're within the maze
                print("Going up...")
                path.append(tuple(current[0] - 1, current[1]))
                print(path)
                if derp(maze, path, end):
                    return True

            # Go right
            if current[1] + 1 < len(maze[0]) and current[1] + 1 != previous[1]:
                print("Going right...")
                path.append(tuple(current[0], current[1] + 1))
                print(path)
                if derp(maze, path, end):
                    return True

            # Go left
            if current[1] - 1 > -1 and current[1] - 1 != previous[1]:
                print("Going left...")
                path.append(tuple(current[0], current[1] - 1))
                print(path)
                if derp(maze, path, end):
                    return True

            # Go down
            if current[0] + 1 < len(maze) and current[0] + 1 != previous[0]:
                print("Going down...")
                path.append(tuple(current[0] + 1, current[1]))
                print(path)
                if derp(maze, path, end):
                    return True

            previous = path[-1]
            print("Deleting the last coordinate " + str(path[-1]))
            del path[-1]
            print("The previous coordinate is now " + str(previous))
            current = path[-1]
            print("The current coordinate is now " + str(current))
            return False


print(derp(maze1, path1, end))




print(path1
      )


