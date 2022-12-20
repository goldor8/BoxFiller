from Display.proxy import *
from grid import *
from block import *

import random
import os
import random

play_grid = []

stock_blocks = [[[0, 0, 1], [0, 1, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
              [[1, 1, 1], [1, 1, 1], [1, 1, 1]]] * 5
round_blocks = []

lives = 3
score = 0


def random_blocks(stock_blocks) :
    a = 0
    b = 0
    c = 0
    while a == b and a == c and b == c:
        a = random.randint(0, len(stock_blocks) - 1)
        b = random.randint(0, len(stock_blocks) - 1)
        c = random.randint(0, len(stock_blocks) - 1)
    return [stock_blocks[a], stock_blocks[b], stock_blocks[c]]

def get_block_for_board_choice(choice) :
    grid_blocks = os.listdir("Level\Blocks\common")
    if choice == 1:
        grid_blocks += os.listdir("Level\Blocks\circle")
    elif choice == 2:
        grid_blocks += os.listdir("Level\Blocks\\triangle")
    elif choice == 3:
        grid_blocks += os.listdir("Level\Blocks\lozenge")
    return grid_blocks


def get_blocks_from_files(blocks_path):
    block_list = []
    for block_path in blocks_path:
        block_list.append(load_block(block_path))
    return block_list


def main():
    print("Welcome to BoxFiller !")
    init_game()

    input("Press any key to continue")


def init_game():
    actionChoice = menu()
    if actionChoice == 2:
        show_rules()
        return init_game()


    gridType = select_grid_type()
    gridSize = select_grid_size()

    global play_grid
    if gridType == 0:
        play_grid = create_circle_grid(gridSize)
    elif gridType == 1:
        play_grid = create_triangle_grid(gridSize)
    elif gridType == 2:
        play_grid = create_lozenge_grid(gridSize)


    playLoop()


def playLoop():
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

    playLoop()


def game_over():
    show_game_over(score)
    exit(0)


def compute_score(broken_squares):
    return broken_squares ** 2


def parse_essential_commands(value):
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
