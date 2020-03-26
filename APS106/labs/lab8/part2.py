start = (0, 1)
path1 = [start]
maze1 = (("X", "S", "X"), ("X", "O", "X"), ("X", "O", "X"), ("X", "E", "X"))

for i in maze1:
    row = ""
    for j in i:
        row += j
    print(row)


def derp(maze, path, end):
    current = list(path[-1])
    print(current)
    maze_pos = maze[current[0]][current[1]]
    print(maze_pos)
    if maze_pos == "E":
        print(path)
        return True

    if maze_pos == "X":
        if len(path) > 1:
            del path[-1]
            return path

    else:

        return False



print(derp(maze1, path1, (3, 1)))