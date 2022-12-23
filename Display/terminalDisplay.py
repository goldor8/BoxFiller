# display module for basic terminal

import string
import block
from Display.viewBufferUtil import *
from main import get_input


def show_board(play_grid, blocks):
    grid_view, block_view = [], []
    prepare_block_view(blocks, 30, 3, block_view)
    prepare_grid_view(play_grid, grid_view)

    max_column = len(grid_view)
    if len(block_view) > max_column:
        max_column = len(block_view)

    for i in range(0, max_column):
        if i < len(grid_view):
            print(grid_view[i], end="")
        else:
            print(" " * len(grid_view[0]), end="")
        if i < len(block_view):
            print(block_view[i])
        else:
            print("")


def print_grid(play_grid):
    grid_view = []
    prepare_grid_view(play_grid, grid_view)
    for i in range(0, len(grid_view)):
        print(grid_view[i])


def print_blocks(blocks):
    blocks_view = []
    prepare_block_view(blocks, 30, 3, blocks_view)
    for i in range(0, len(blocks_view)):
        print(blocks_view[i])


def prepare_grid_view(play_grid, grid_view):  # Store the grid display in a list of string
    clear_view(grid_view)
    set_line_view(0)

    # Add letter on top of each column
    add_to_view("    ", grid_view)
    for i in range(len(play_grid[0])):
        add_to_view(chr(ord('a') + i) + "  ", grid_view)
    increment_view_line()

    # Add fancy top border
    add_to_view("  ╔", grid_view)
    for i in range(len(play_grid[0])):
        add_to_view("═══", grid_view)
    add_to_view("╗", grid_view)
    increment_view_line()

    # Draw line Add letter for each line and add fancy border
    for y in range(len(play_grid)):
        add_to_view(chr(ord('A') + y) + " ║", grid_view)  # Add letter for each line and fancy border
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
        block_number_text = str(blockIndex + 1)
        before_space = int((block_size * 3 - len(block_number_text)) / 2) + 1
        after_space = block_size * 3 - len(block_number_text) - before_space + 1
        add_to_view(" " * before_space + block_number_text + after_space * " " + " ", block_view)


def select_grid_type():
    print("Select grid type :")
    print("1. Circle")
    print("2. Triangle")
    print("3. Lozenge")

    grid_type = get_valid_int_input("Enter your choice : ", lambda x: x in [1, 2, 3])
    return int(grid_type) - 1


def select_grid_size():
    print("Select grid odd size between 21 and 25 : ")

    grid_size = get_valid_int_input("Enter your choice : ", lambda x: x in range(21, 27) and x % 2 == 1)
    return grid_size


def menu():
    print("Select what you want to do")
    print("1. Play")
    print("2. Show rules")

    choice = get_valid_int_input("Enter your choice : ", lambda x: x in [1, 2])
    return choice


def show_rules():
    rules = open("Regles.txt", "r", encoding="utf-8")
    rules_lines = rules.readlines()
    for line in rules_lines:
        print(line, end="")
    rules.close()
    print()
    get_input_not_parsed("Press any key to continue")


def get_input_not_parsed(text="Press any key to continue"):
    return input(text)


def select_block_position(play_grid, selected_block):
    def is_input_in_valid_format(input_text):
        return len(input_text) == 2 and input_text[0] in string.ascii_uppercase and input_text[1] in string.ascii_lowercase

    def get_position_from_position_input(input_text):
        return ord(input_text[1]) - ord('a'), ord(input_text[0]) - ord('A')

    block_position = get_input("Enter block position: ")
    while not is_input_in_valid_format(block_position):
        print("Wrong format for block position ! Please enter a uppercase letter followed by an lowercase letter")
        block_position = get_input("Enter your choice : ")

    return get_position_from_position_input(block_position)


def select_block(list_blocks):
    num_block = 0
    while (num_block < 1) or (num_block > len(list_blocks)):
        num_block = get_valid_int_input("Enter block number : ", lambda x: x in range(1, len(list_blocks) + 1))
    return num_block - 1


def select_block_rotation(selected_block):
    show_current_block(selected_block)
    input_text = get_input("Enter 'y' or 'n'/nothing to rotate or not the block: ")
    while input_text != "" and input_text != "y" and input_text != "n":
        print("Wrong format for rotation ! Please enter 'y' or 'n'/nothing (blank)")
        input_text = get_input("Enter 'y' or 'n'/nothing (blank) to rotate or not the block: ")

    if input_text == "y":
        return select_block_rotation(block.rotate_block(selected_block))

    return selected_block


def show_current_block(block):
    print("Current block : ")
    for line in block:
        for number in line:
            if number == 1:
                print(" ■ ", end="")
            else:
                print(" . ", end="")
        print()


def show_game_over(score):
    print("Game over !")
    print("Your score is : " + str(score))
    get_input("Press any key to continue")


def get_valid_int_input(text, valid_expression_lambda):
    def is_digit_and_valid(input_text):
        return input_text.isdigit() and valid_expression_lambda(int(input_text))

    input_text = get_input(text)
    while not is_digit_and_valid(input_text):
        print("Invalid integer !")
        input_text = get_input(text)
    return int(input_text)


def select_block_picking_manner():
    block_picking_way = 0
    print("Select block picking manner:")
    print("1. Show all blocks")
    print("2. Show 3 random blocks from all blocks")
    while block_picking_way != 1 and block_picking_way != 2:
        block_picking_way = get_valid_int_input("Enter your choice : ", lambda x: x in [1, 2])
    return block_picking_way - 1