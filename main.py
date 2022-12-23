"""
Project : BoxFiller
Description : This file contain the main logic of the game, how the react to the player's input and how the game is played
Author : Brisset Dimitri, Occhiminuti Marius
"""

import sys
import random
import Display.proxy as proxy

from grid import *
from block import *


play_grid = []  # represents the grid on which the player is playing
stock_blocks = []  # all blocks available for the grid shape
round_blocks = []  # blocks that will be used after the board shape has been chosen
block_picking_manner = 0    # 0 = all blocks from stock_blocks, 1 = 3 random blocks from stock_blocks

lives = 3
score = 0


def main() -> None:
    """
    Main function
    :return: None
    """
    print("Welcome to BoxFiller !")
    init_game()

    input("Press any key to continue")


def init_game() -> None:
    """
    function called at the beginning of the game
    :return: None
    """
    action_choice = proxy.menu()
    if action_choice == 2:
        proxy.show_rules()
        return init_game()

    grid_type = proxy.select_grid_type()
    grid_size = proxy.select_grid_size()
    global stock_blocks
    stock_blocks = get_blocks_from_files(get_block_paths_for_board_choice(grid_type))
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


def play_loop() -> None:
    """
    Main loop of the game (determine all the actions to be done during a round)
    :return: None
    """
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


def game_over() -> None:
    """
    function called when the player has no more lives
    :return: None
    """
    proxy.show_game_over(score)
    exit(0)


def update_round_blocks() -> None:
    """
    Updates the list of blocks that will be used in the next round
    :return: None (updates the global variable round_blocks)
    """
    global round_blocks
    if block_picking_manner == 0:
        round_blocks = stock_blocks
    elif block_picking_manner == 1:
        round_blocks = random_blocks(stock_blocks)


def random_blocks(block_list: list) -> list:
    """
    Returns a list of 3 random blocks
    :param block_list: list of blocks from which the random blocks will be chosen
    :return: list of 3 random blocks
    """
    a = 0
    b = 0
    c = 0
    while a == b and a == c and b == c:
        a = random.randint(0, len(block_list) - 1)
        b = random.randint(0, len(block_list) - 1)
        c = random.randint(0, len(block_list) - 1)
    return [block_list[a], block_list[b], block_list[c]]


def compute_score(broken_squares: int) -> int:
    """
    Computes the score of the player for new broken squares
    :param broken_squares: number of broken squares
    :return: score of the player for new broken squares
    """
    return broken_squares ** 2


def get_input(text: str) -> str:
    """
    called each time a player is asked for an input and detects if the player wants to execute an essential command
    :param text: text to be displayed to the player
    :return: input of the player
    """
    input_text = proxy.get_input_not_parsed(text)
    if parse_essential_commands(input_text):
        return get_input(text)
    return input_text


def parse_essential_commands(input_text: str) -> bool:
    """
    called each time a player is asked for an input and detects if the player wants to execute an essential command
    :param input_text: input of the player
    :return: True if the player has executed an essential command, False otherwise
    """
    input_text.lower()
    if input_text == "exit":
        exit(0)
        return True
    elif input_text == "help":
        print("help")
        return True
    return False


if __name__ == "__main__":
    # parse arguments
    display_name = ""
    arg_count = len(sys.argv)
    for i in range(arg_count):
        if (sys.argv[i] == "-d" or sys.argv[i] == "--display") and i + 1 <= arg_count:
            display_name = sys.argv[i + 1]
            break

    proxy.init_display(display_name)
    main()
