start = [3,2]  # 3,2
path1 = [start]
maze1 = (("X", "X", "X", "X", "X"), ("E", "O", "O", "O", "X"), ("X", "X", "O", "X", "X"), ("X", "X", "S", "X", "X"))

for i in maze1:
    row = ""
    for j in i:
        row += j
    print(row)


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
                path.append([current[0] - 1, current[1]])
                print(path)
                if derp(maze, path, end):
                    return True

            # Go right
            if current[1] + 1 < len(maze[0]) and current[1] + 1 != previous[1]:
                print("Going right...")
                path.append([current[0], current[1] + 1])
                print(path)
                if derp(maze, path, end):
                    return True

            # Go left
            if current[1] - 1 > -1 and current[1] - 1 != previous[1]:
                print("Going left...")
                path.append([current[0], current[1] - 1])
                print(path)
                if derp(maze, path, end):
                    return True

            # Go down
            if current[0] + 1 < len(maze) and current[0] + 1 != previous[0]:
                print("Going down...")
                path.append([current[0] + 1, current[1]])
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





print(derp(maze1, path1, (1,0)))