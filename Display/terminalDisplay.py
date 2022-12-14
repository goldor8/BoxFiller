from Display.viewBufferUtil import *
from main import parse_essential_commands


def show_board(play_grid, blocks):
    grid_view, block_view = [], []
    prepare_block_view(blocks, 30, 3, block_view)
    prepare_grid_view(play_grid, grid_view)

    maxColumn = len(grid_view)
    if len(block_view) > maxColumn:
        maxColumn = len(block_view)

    for i in range(0, maxColumn):
        if (i < len(grid_view)):
            print(grid_view[i], end="")
        else:
            print(" " * len(grid_view[0]), end="")
        if (i < len(block_view)):
            print(block_view[i])
        else:
            print("")


# Store the grid display in a list of string
def prepare_grid_view(play_grid, grid_view):
    clear_view(grid_view)
    set_line_view(0)

    # Add letter on top of each column
    add_to_view("    ", grid_view)
    for i in range(len(play_grid[0])):
        add_to_view(chr(65 + i) + "  ", grid_view)
    increment_view_line()

    # Add fancy top border
    add_to_view("  ╔", grid_view)
    for i in range(len(play_grid[0])):
        add_to_view("═══", grid_view)
    add_to_view("╗", grid_view)
    increment_view_line()

    # Draw line Add letter for each line and add fancy border
    for y in range(len(play_grid)):
        add_to_view(chr(97 + y) + " ║", grid_view)  # Add letter for each line and fancy border
        for x in range(len(play_grid[y])):  # Draw each cell
            if play_grid[y][x] == 1:
                add_to_view(" . ", grid_view)
            elif play_grid[y][x] == 2:
                add_to_view(" ■ ", grid_view)
            elif play_grid[y][x] == 0:
                add_to_view("   ", grid_view)
        add_to_view("║", grid_view)  # Add fancy border
        increment_view_line()

    # Add fancy bottom border
    add_to_view("  ╚", grid_view)
    for i in range(len(play_grid[0])):
        add_to_view("═══", grid_view)
    add_to_view("╝", grid_view)
    increment_view_line()


# Store the block display in a list of string
def prepare_block_view(blocks, max_lenght, block_size, block_view):
    clear_view(block_view)

    block_per_line = int((max_lenght - 3) / (block_size + 2))  # compute the number of block per line
    block_line_index = -1  # init at -1 to increment at the first loop

    for blockIndex in range(0, len(blocks)):
        block = blocks[blockIndex]

        # limit the number of block per line by adding a new line
        if blockIndex % block_per_line == 0:
            block_line_index += 1
        set_line_view(block_line_index * (block_size + 2))

        # Draw the block
        for lineIndex in range(0, len(block)):
            line = block[lineIndex]

            # Draw the block line
            for numberIndex in range(0, len(line)):
                number = line[numberIndex]

                if numberIndex == 0:
                    add_to_view(" ", block_view)
                if number == 1:
                    add_to_view(" ■ ", block_view)
                else:
                    add_to_view(" . ", block_view)
                if numberIndex == len(line) - 1:
                    add_to_view(" ", block_view)

            increment_view_line()

        # add block number under the block
        blockNumberText = str(blockIndex + 1)
        beforeSpace = int((block_size * 3 - len(blockNumberText)) / 2) + 1
        afterSpace = block_size * 3 - len(blockNumberText) - beforeSpace + 1
        add_to_view(" " * beforeSpace + blockNumberText + afterSpace * " " + " ", block_view)


def select_grid_type():
    print("Select grid type :")
    print("1. Circle")
    print("2. Triangle")
    print("3. Lozenge")

    gridType = get_input("Enter your choice : ")
    while gridType not in ["1", "2", "3"]:
        print("Invalid choice !")
        gridType = get_input("Enter your choice : ")

    return int(gridType) - 1


def select_grid_size():
    print("Select grid odd size between 21 and 43 : ")
    gridSize = int(get_input("Enter your choice : "))
    while gridSize not in range(21, 44) or gridSize % 2 == 0:
        print("Invalid choice !")
        gridSize = int(get_input("Enter your choice : "))

    return gridSize


def menu():
    print("Select what you want to do")
    print("1. Play")
    print("2. Show rules")

    choice = int(get_input("Enter your choice : "))
    while choice != 1 and choice != 2:
        print("Invalid choice !")
        choice = int(get_input("Enter your choice : "))

    return choice


def show_rules():
    regles = open("Regles.txt", "r", encoding="utf-8")
    regle = regles.readlines()
    for ligne in regle:
        print(ligne, end="")
    regles.close()
    print()
    get_input_not_parsed("Press any key to continue")


def get_input_not_parsed(text="Press any key to continue"):
    return input(text)


def get_input(text):
    str = get_input_not_parsed(text)
    if parse_essential_commands(str):
        return get_input(text)
    return str
def choose_block (list_blocks) :
    num_block = 0
    while (num_block < 1) or (num_block > len(list_blocks)) :
        num_block = int(input("Choose a block : "))
    return num_block - 1
