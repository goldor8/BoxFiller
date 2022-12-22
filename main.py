import Display.proxy
from Display.proxy import *
from grid import *
from block import *

import os
import random

play_grid = []  # represents the grid on which the player is playing

stock_blocks = [[[0, 0, 1], [0, 1, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                [[1, 1, 1], [1, 1, 1], [1, 1, 1]]] * 5
round_blocks = []  # blocks that will be used after the board shape has been chosen
block_picking_way = 0    # 0 = 3 random blocks from stock_blocks, 1 = all blocks from stock_blocks

lives = 3
score = 0


def number_of_blocks(block_list, grid_shape_choice):
    num_block_choice = select_block_picking_way()
    if num_block_choice == 1:
        stock_blocks = random_blocks(block_list)
    else:
        stock_blocks = get_blocks_from_files(get_paths_for_board_choice(grid_shape_choice))
    return stock_blocks


def random_blocks(block_list):  # returns a list of 3 random blocks
    a = 0
    b = 0
    c = 0
    while a == b and a == c and b == c:
        a = random.randint(0, len(block_list) - 1)
        b = random.randint(0, len(block_list) - 1)
        c = random.randint(0, len(block_list) - 1)
    return [block_list[a], block_list[b], block_list[c]]


def get_paths_for_board_choice(choice):  # returns the paths corresponding to the choice of board
    grid_blocks = "Level\\Blocks\\common" + os.listdir("Level\\Blocks\\common")
    if choice == 1:
        grid_blocks += ["Level\\Blocks\\circle" + i for i in os.listdir("Level\\Blocks\\circle")]
    elif choice == 2:
        grid_blocks += ["Level\\Blocks\\triangle" + i for i in os.listdir("Level\\Blocks\\triangle")]
    elif choice == 3:
        grid_blocks += ["Level\\Blocks\\lozenge" + i for i in os.listdir("Level\\Blocks\\lozenge")]
    return grid_blocks


def get_blocks_from_files(blocks_path):  # returns a list of blocks from the list of paths
    block_list = []
    for block_path in blocks_path:
        block_list.append(load_block(block_path))
    return block_list


def main():
    print("Welcome to BoxFiller !")
    init_game()

    input("Press any key to continue")


def init_game():
    action_choice = menu()
    if action_choice == 2:
        show_rules()
        return init_game()

    grid_type = select_grid_type()
    grid_size = select_grid_size()
    stock_blocks = get_blocks_from_files(get_paths_for_board_choice(grid_type))

    block_picking_way = select_block_picking_way()

    global play_grid
    if grid_type == 0:
        play_grid = create_circle_grid(grid_size)
    elif grid_type == 1:
        play_grid = create_triangle_grid(grid_size)
    elif grid_type == 2:
        play_grid = create_lozenge_grid(grid_size)

    play_loop()


def play_loop():
    global round_blocks
    round_blocks = random_blocks(stock_blocks)

    show_board(play_grid, round_blocks)

    selected_block_index = select_block(round_blocks)
    round_blocks[selected_block_index] = select_block_rotation(round_blocks[selected_block_index])
    position_x, position_y = select_block_position(play_grid, round_blocks[selected_block_index])
    while not can_emplace_block(play_grid, round_blocks[selected_block_index], position_x, position_y):
        global lives
        lives -= 1
        if lives == 0:
            game_over()
            return

        print("Invalid position ! You have " + str(lives) + " tries left")
        position_x, position_y = select_block_position(play_grid, round_blocks[selected_block_index])

    emplace_block(play_grid, round_blocks[selected_block_index], position_x, position_y)

    broken_squares = check_for_full_row_or_column(play_grid)

    global score
    score += compute_score(broken_squares)
    print("Score : " + str(score))

    play_loop()


def game_over():  # function called when the player has no more lives
    show_game_over(score)
    exit(0)


def compute_score(broken_squares):  # returns the score of the player for new broken squares
    return broken_squares ** 2


def get_input(text):
    input_text = Display.proxy.get_input_not_parsed(text)
    if parse_essential_commands(input_text):
        return get_input(text)
    return input_text


def parse_essential_commands(value):  # called each time a player is asked for an input and detects if the player wants to execute an essential command
    value.lower()
    if value == "exit":
        exit(0)
        return True
    elif value == "help":
        print("help")
        return True
    return False


if __name__ == "__main__":
    main()
