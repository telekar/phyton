import numpy as np
data = open("puzzle_3a.txt").read().strip()
step = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}
grid = np.zeros((1000, 1000), dtype='int32')
santa_x = 500
santa_y = 500
robot_x = 500
robot_y = 500
grid[santa_x, santa_y] += 1
grid[robot_x, robot_y] += 1
for i, direction in enumerate(data):
    delta_x, delta_y = step[direction]
    if (i % 2) == 0:
        santa_x += delta_x
        santa_y += delta_y
        grid[santa_x, santa_y] += 1
    else:
        robot_x += delta_x
        robot_y += delta_y
        grid[robot_x, robot_y] += 1
print("At least one present:", len(np.nonzero(grid)[0]))