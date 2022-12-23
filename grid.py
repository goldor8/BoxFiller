"""
Project : BoxFiller
Description : This module is used to generate and manipulate a grid
Author : Brisset Dimitri, Occhiminuti Marius
"""


def save_grid(grid: list, file_path: str) -> None:
    """
    Save the grid in a file at the path specified
    :param grid: the grid to save
    :param file_path: the path of the file
    :return: None
    """
    with open("Level/Saves/" + file_path, 'w') as f:
        for y in range(len(grid)):
            f.write(" ".join([str(x) for x in grid[y]]) + "\n")


def load_grid(file_path: str) -> list:
    """
    Load the grid from a file at the path specified
    :param file_path: the path of the file
    :return: the grid
    """
    with open("Level/Saves/" + file_path, 'r') as f:
        grid = []
        for line in f:
            grid.append([int(x) for x in line.split(" ")])
        return grid


def create_circle_grid(size: int) -> list:
    """
    Create a grid with a circle shape
    :param size: the size of the grid
    :return: a grid with a circle shape
    """
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


def create_triangle_grid(size: int) -> list:
    """
    Create a grid with a triangle shape
    :param size: the size of the grid
    :return: a grid with a triangle shape
    """
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


def create_lozenge_grid(size: int) -> list:
    """
    Create a grid with a lozenge shape
    :param size: the size of the grid
    :return: a grid with a lozenge shape
    """
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


def can_emplace_block(grid: list, block: list, x: int, y: int) -> bool:
    """
    Check if the block can be placed at the position
    :param grid: grid where the block will be placed
    :param block: block to place
    :param x: x position
    :param y: y position
    :return: True if the block can be placed, False otherwise
    """

    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1 and not is_in_grid_and_empty(grid, x + j, y + i):
                return False
    return True


def emplace_block(grid: list, block: list, x: int, y: int) -> None:
    """
    Place the block at the position
    :param grid: grid where the block will be placed
    :param block: block to place
    :param x: x position
    :param y: y position
    :return: None
    """
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == 1:
                grid[y + i][x + j] = 2


def is_column_full(grid: list, x: int) -> bool:
    """
    Check if the column is full
    :param grid: the grid to check
    :param x: the column index to check
    :return: True if the column is full, False otherwise
    """
    for y in range(len(grid)):
        if grid[y][x] == 1:
            return False
    return True


def is_row_full(grid: list, y: int) -> bool:
    """
    Check if the row is full
    :param grid: the grid to check
    :param y: the row index to check
    :return: True if the row is full, False otherwise
    """
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            return False
    return True


def empty_column(grid: list, x: int) -> None:
    """
    Empty a column
    :param grid: the grid to empty
    :param x: the column index to empty
    :return: None (the grid is modified by reference)
    """
    for y in range(len(grid)):
        if grid[y][x] == 2:
            grid[y][x] = 1


def empty_row(grid: list, y: int) -> None:
    """
    Empty a row
    :param grid: the grid to empty
    :param y: the row index to empty
    :return: None (the grid is modified by reference)
    """
    for x in range(len(grid[y])):
        if grid[y][x] == 2:
            grid[y][x] = 1


def bring_cube_down_from_column_index(grid: list, row_index: int) -> None:
    """
    Bring the cube down from the row index
    :param grid: the grid to modify
    :param row_index: the row index to start from
    :return: None (the grid is modified by reference)
    """
    if row_index < 0 or row_index > len(grid[0]) - 1:
        return
    for y in range(row_index, 0, -1):
        for x in range(len(grid)):
            if grid[y][x] == 1 and grid[y - 1][x] == 2:
                grid[y][x] = 2
                grid[y - 1][x] = 1


def check_for_full_row_or_column(grid: list) -> int:
    """
    Check if there is full rows or columns and remove them
    :param grid: the grid to check
    :return: return the number of squares removed
    """
    broken_squares = 0
    for y in range(0, len(grid)):
        while is_row_full(grid, y):  # while loop because fallen squares can fill the actual line
            broken_squares += sum([1 if grid[y][x] == 2 else 0 for x in range(len(grid[y]))])
            empty_row(grid, y)
            bring_cube_down_from_column_index(grid, y)
    for x in range(len(grid[0])):
        if is_column_full(grid, x):
            broken_squares += sum([1 if grid[y][x] == 2 else 0 for y in range(len(grid))])
            empty_column(grid, x)

    return broken_squares


def is_in_grid(grid: list, x: int, y: int) -> bool:
    """
    Check if the position is in the grid
    :param grid: the grid to check
    :param x: x position
    :param y: y position
    :return: True if the position is in the grid, False otherwise
    """
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def is_empty(grid: list, x: int, y: int) -> bool:
    """
    Check if the position is empty
    :param grid: the grid to check
    :param x: x position
    :param y: y position
    :return: True if the position is empty, False otherwise
    """
    b = grid[y][x] == 1
    return b


def is_in_grid_and_empty(grid: list, x: int, y: int) -> bool:
    """
    Check if the position is in the grid and empty
    :param grid: the grid to check
    :param x: x position
    :param y: y position
    :return: True if the position is in the grid and empty, False otherwise
    """
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
