start = (0, 2)  # 3,2
path1 = [start]
maze1 = (("X", "X", "S", "X", "X"), ("X", "X", "O", "X", "X"), ("X", "X", "O", "X", "X"), ("X", "X", "E", "X", "X"))

for i in maze1:
    row = ""
    for j in i:
        row += j
    print(row)


def derp(maze, path, end):
    current_square = list(path[-1])
    position_in_maze = maze[current_square[0]][current_square[1]]

    # Base cases
    if current_square[0] >= len(maze) or current_square[0] < 0 or current_square[1] < 0 or current_square[1] >= len(maze[0]):
        return False

    if position_in_maze == "X":
        return False

    if position_in_maze == "E":
        return True

    if path.count(current_square) > 1:
        return False

    path.append(current)






print(derp(maze1, path1, [3, 2]))
