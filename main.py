"""
Project : BoxFiller
Description : This file contain the main logic of the game, how the react to the player's input and how the game is played
Author : Brisset Dimitri, Occhiminuti Marius
"""

import sys
import os
import random

from grid import *
from block import *

import Display.proxy as proxy  # different proxy import to avoid strange import errors

play_grid = []  # represents the grid on which the player is playing

stock_blocks = [[[0, 0, 1], [0, 1, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
                [[1, 1, 1], [1, 1, 1], [1, 1, 1]]] * 5
round_blocks = []  # blocks that will be used after the board shape has been chosen
block_picking_manner = 0    # 0 = all blocks from stock_blocks, 1 = 3 random blocks from stock_blocks

lives = 3
score = 0


def main():
    print("Welcome to BoxFiller !")
    init_game()

    input("Press any key to continue")


def init_game():  # function called at the beginning of the game
    action_choice = proxy.menu()
    if action_choice == 2:
        proxy.show_rules()
        return init_game()

    grid_type = proxy.select_grid_type()
    grid_size = proxy.select_grid_size()
    global stock_blocks
    stock_blocks = get_blocks_from_files(get_paths_for_board_choice(grid_type))
    normalize_block_list(stock_blocks)

    global block_picking_manner
    block_picking_manner = proxy.select_block_picking_manner()

    global play_grid
    if grid_type == 0:
        play_grid = create_circle_grid(grid_size)
    elif grid_type == 1:
        play_grid = create_triangle_grid(grid_size)
    elif grid_type == 2:
        play_grid = create_lozenge_grid(grid_size)

    play_loop()


def get_paths_for_board_choice(choice):  # returns the paths corresponding to the choice of board
    grid_blocks = ["Level/Blocks/common/" + i for i in os.listdir("Level/Blocks/common")]
    if choice == 0:
        grid_blocks += ["Level/Blocks/circle/" + i for i in os.listdir("Level/Blocks/circle")]
    elif choice == 1:
        grid_blocks += ["Level/Blocks/triangle/" + i for i in os.listdir("Level/Blocks/triangle")]
    elif choice == 2:
        grid_blocks += ["Level/Blocks/lozenge/" + i for i in os.listdir("Level/Blocks/lozenge")]
    return grid_blocks


def get_blocks_from_files(blocks_path):  # returns a list of blocks from the list of paths
    block_list = []
    for block_path in blocks_path:
        block_list.append(load_block(block_path))
    return block_list


def play_loop():  # determine all the actions to be done during a round
    update_round_blocks()

    global round_blocks
    proxy.show_board(play_grid, round_blocks)

    selected_block_index = proxy.select_block(round_blocks)
    round_blocks[selected_block_index] = proxy.select_block_rotation(round_blocks[selected_block_index])
    position_x, position_y = proxy.select_block_position(play_grid, round_blocks[selected_block_index])
    while not can_emplace_block(play_grid, round_blocks[selected_block_index], position_x, position_y):
        global lives
        lives -= 1
        if lives == 0:
            game_over()
            return

        print("Invalid position ! You have " + str(lives) + " tries left")
        position_x, position_y = proxy.select_block_position(play_grid, round_blocks[selected_block_index])

    emplace_block(play_grid, round_blocks[selected_block_index], position_x, position_y)

    broken_squares = check_for_full_row_or_column(play_grid)

    global score
    score += compute_score(broken_squares)
    print("Score : " + str(score))

    play_loop()


def game_over():  # function called when the player has no more lives
    proxy.show_game_over(score)
    exit(0)


def update_round_blocks():  # updates the list of blocks that will be used in the next round
    global round_blocks
    if block_picking_manner == 0:
        round_blocks = stock_blocks
    elif block_picking_manner == 1:
        round_blocks = random_blocks(stock_blocks)


def random_blocks(block_list):  # returns a list of 3 random blocks
    a = 0
    b = 0
    c = 0
    while a == b and a == c and b == c:
        a = random.randint(0, len(block_list) - 1)
        b = random.randint(0, len(block_list) - 1)
        c = random.randint(0, len(block_list) - 1)
    return [block_list[a], block_list[b], block_list[c]]


def compute_score(broken_squares):  # returns the score of the player for new broken squares
    return broken_squares ** 2


def get_input(text):  # called each time a player is asked for an input and detects if the player wants to execute an essential command
    input_text = proxy.get_input_not_parsed(text)
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
    display_name = ""
    arg_count = len(sys.argv)
    for i in range(arg_count):
        if (sys.argv[i] == "-d" or sys.argv[i] == "--display") and i + 1 <= arg_count:
            display_name = sys.argv[i + 1]
            break
    proxy.init_display(display_name)
    main()