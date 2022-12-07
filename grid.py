def save_grid(grid, filePath):
    with open(filePath, 'w') as f:
        for x in range(len(grid)):
            for y in range(len(grid[x]) - 1):
                f.write(str(grid[x][y]))
                f.write(' ')
            f.write(str(grid[x][len(grid[x]) - 1]))
            f.write("\n")


def create_circle_grid(diameter):
    def is_in_circle(x, y, radius):
        return (x + 0.5 - radius) ** 2 + (y + 0.5 - radius) ** 2 <= radius ** 2

    grid = []
    for x in range(diameter):
        grid.append([])
        for y in range(diameter):
            if is_in_circle(x, y, diameter / 2):
                grid[x].append(1)
            else:
                grid[x].append(0)
    return grid


def create_triangle_grid(taille):
    grid = []
    for k in range(int(taille / 2) + 1):
        grid.append([])
        middle = int(taille / 2)
        for i in range(taille):
            if (i <= middle + k and i >= middle - k):
                grid[k].append(1)
            else:
                grid[k].append(0)
    return grid


def create_lozenge_grid(taille):
    grid = []
    a = -1
    middle = int(taille / 2)
    for k in range(int(taille / 2) + 1):
        a += 1
        grid.append([])
        for i in range(taille):
            if (i <= middle + a and i >= middle - a):
                grid[k].append(1)
            else:
                grid[k].append(0)
    for k in range(int(taille / 2) + 1, taille):
        grid.append([])
        a -= 1
        for i in range(taille):
            if (i <= middle + a and i >= middle - a):
                grid[k].append(1)
            else:
                grid[k].append(0)
    return grid

def can_emplace_block(grid, block, y, x):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if grid[y + i][x + j] == 2 and block[i][j] == 1:
                return False
    return True

def emplace_block(grid, block, x, y):
    for i in range(len(block)):
        for j in range(len(block[i])):
            grid[x + i][y + j] = block[i][j]


def is_column_full(grid, x):
    for y in range(len(grid)):
        if grid[y][x] == 1:
            return False
    return True

def is_row_full(grid, y):
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            return False
    return True

def bring_cube_down_from_column_index(grid, rowIndex):
    if rowIndex < 0 or rowIndex >= len(grid[0]) - 1:
        return
    for y in range(rowIndex, -1, -1):
        for x in range(len(grid)):
            if grid[y + 1][x] == 1 and grid[y][x] == 2:
                grid[y + 1][x] = 2
                grid[y][x] = 1

def fill_column(grid, x):
    for y in range(len(grid)):
        if grid[y][x] == 1:
            grid[y][x] = 2


def empty_column(grid, x):
    for y in range(len(grid)):
        if grid[y][x] == 2:
            grid[y][x] = 1

def fill_row(grid, y):
    for x in range(len(grid[y])):
        if grid[y][x] == 1:
            grid[y][x] = 2


def empty_row(grid, y):
    for x in range(len(grid[y])):
        if grid[y][x] == 2:
            grid[y][x] = 1


def fill_all_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                grid[y][x] = 2

def check_for_full_row_or_column(grid):
    for y in range(len(grid)):
        if is_row_full(grid, y):
            empty_row(grid, y)
    for x in range(len(grid[0])):
        if is_column_full(grid, x):
            empty_column(grid, x)