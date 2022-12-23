"""
Project : BoxFiller
Description : This module is used to generate and manipulate a grid
Author : Brisset Dimitri, Occhiminuti Marius
"""


def save_grid(grid, file_path):  # save the grid in a file at the path specified
    with open(file_path, 'w') as f:
        for y in range(len(grid)):
            f.write(" ".join([str(x) for x in grid[y]]) + "\n")


def load_grid(file_path):  # load the grid from a file at the path specified
    with open(file_path, 'r') as f:
        grid = []
        for line in f:
            grid.append([int(x) for x in line.split(" ")])
        return grid


def create_circle_grid(size):  # create a grid with a circle shape
    def is_in_circle(x, y, radius):
        return (x + 0.5 - radius) ** 2 + (y + 0.5 - radius) ** 2 <= radius ** 2  # offset by 0.5 to center the sample point in the middle of the cell

    grid = []
    for x_index in range(size):
        grid.append([])
        for y_index in range(size):
            if is_in_circle(x_index, y_index, size / 2):
                grid[x_index].append(1)
            else:
                grid[x_index].append(0)
    return grid


def create_triangle_grid(size):  # create a grid with a triangle shape
    grid = []
    for k in range(int(size / 2) + 1):
        grid.append([])
        middle = int(size / 2)
        for i in range(size):
            if middle - k <= i <= middle + k:
                grid[k].append(1)
            else:
                grid[k].append(0)
    return grid


def create_lozenge_grid(size):  # create a grid with a lozenge shape
    grid = []
    a = -1  # a represents the width of the lozenge
    middle = int(size / 2)
    for k in range(int(size / 2) + 1):
        a += 1
        grid.append([])
        for i in range(size):
            if middle - a <= i <= middle + a:
                grid[k].append(1)
            else:
                grid[k].append(0)
    for k in range(int(size / 2) + 1, size):
        grid.append([])
        a -= 1
        for i in range(size):
            if middle - a <= i <= middle + a:
                grid[k].append(1)
            else:
                grid[k].append(0)
    return grid


def can_emplace_block(grid, block, x, y):  # check if the block can be placed at the position
    for i in range(len(block)):
        for j in range(len(block[i])):
            if not is_in_grid(grid, x + j, y - len(block) + 1 + i):
                return False
            if block[i][j] == 1 and not is_empty(grid, x + j, y - len(block) + 1 + i):
                return False
            if grid[y - len(block) + 1 + i][x + j] == 2 and block[i][j] == 1:
                return False
    return True


def emplace_block(grid, block, x, y):  # place the block at the position
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                grid[y - len(block) + 1 + i][x + j] = 2


def is_column_full(grid, x):  # check if the column is full
    for y in range(len(grid)):
        if grid[y][x] == 1:
            return False
    return True


def is_row_full(grid, y):  # check if the row is full
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            return False
    return True


def bring_cube_down_from_column_index(grid, row_index):  # bring the cube down from the row index
    if row_index < 0 or row_index >= len(grid[0]) - 1:
        return
    for y in range(row_index, -1, -1):
        for x in range(len(grid)):
            if grid[y + 1][x] == 1 and grid[y][x] == 2:
                grid[y + 1][x] = 2
                grid[y][x] = 1


def fill_column(grid, x):  # fill a column
    for y in range(len(grid)):
        if grid[y][x] == 1:
            grid[y][x] = 2


def empty_column(grid, x):  # empty a column
    for y in range(len(grid)):
        if grid[y][x] == 2:
            grid[y][x] = 1


def fill_row(grid, y):  # fill a row
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            grid[y][x] = 2


def empty_row(grid, y):  # empty a row
    for x in range(len(grid[y])):
        if grid[y][x] == 2:
            grid[y][x] = 1


def fill_all_grid(grid):  # fill the grid (used for the test)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                grid[y][x] = 2


def check_for_full_row_or_column(grid):  # check if there is full rows or columns and remove them
    broken_squares = 0
    for y in range(0, len(grid)):
        if is_row_full(grid, y):  # fallen squares can fill the line
            empty_row(grid, y)
            broken_squares += len(grid[y])
            bring_cube_down_from_column_index(grid, y)
    for x in range(len(grid[0])):
        if is_column_full(grid, x):
            empty_column(grid, x)
            broken_squares += len(grid)

    return broken_squares


def is_in_grid(grid, x, y):  # check if the position is in the grid
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def is_empty(grid, x, y):  # check if the position is empty
    b = grid[y][x] == 1
    return b


def is_in_grid_and_empty(grid, x, y):  # check if the position is in the grid and empty
    return is_in_grid(grid, x, y) and is_empty(grid, x, y)


def row_state(grid, i):
    return is_row_full(grid, i)


def col_state(grid, j):
    return is_column_full(grid, j)


def row_clear(grid, i):
    empty_row(grid, i)


def col_clear(grid, j):
    empty_column(grid, j)


def valid_position(grid, block, i, j):
    return can_emplace_block(grid, block, i, j)
