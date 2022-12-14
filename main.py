from Display.proxy import *

import random
import os
import grid
import random

play_grid = []

stock_blocks = [[[0, 0, 1], [0, 1, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
              [[1, 1, 1], [1, 1, 1], [1, 1, 1]]] * 5
round_blocks = []


def random_blocks(stock_blocks) :
    a = 0
    b = 0
    c = 0
    while a == b and a == c and b == c:
        a = random.randint(0, len(stock_blocks) - 1)
        b = random.randint(0, len(stock_blocks) - 1)
        c = random.randint(0, len(stock_blocks) - 1)
    return stock_blocks[a], stock_blocks[b], stock_blocks[c]

def get_block_for_board_choice(choice) :
    grid_blocks = os.listdir("Level\Blocks\common")
    if choice == 1:
        grid_blocks += os.listdir("Level\Blocks\circle")
    elif choice == 2:
        grid_blocks += os.listdir("Level\Blocks\\triangle")
    elif choice == 3:
        grid_blocks += os.listdir("Level\Blocks\lozenge")
    return grid_blocks


def get_blocks_from_files(grid_blocks):
    list_block_mat = []
    for blocks in grid_blocks:
        block_mat = []
        block_file = open(blocks, "r")
        block_file_lines = block_file.readlines()
        for line in range (0, len(block_file_lines)):
            block_mat.append([])
            num_list = block_file_lines[line].split(" ")
            for num in num_list :
                block_mat[line].append(int(num))
        list_block_mat.append(block_mat)
    return list_block_mat


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
        play_grid = grid.create_circle_grid(gridSize)
    elif gridType == 1:
        play_grid = grid.create_triangle_grid(gridSize)
    elif gridType == 2:
        play_grid = grid.create_lozenge_grid(gridSize)


    playLoop()


def playLoop():
    global round_blocks
    round_blocks = random_blocks(stock_blocks)
    show_board(play_grid, round_blocks)
    block_selected_index = select_block(round_blocks)
    position_x, position_y = select_block_position(play_grid)


    get_input("Press any key to continue")
    playLoop()


def compute_score(bloc_casse):
    score = bloc_casse ** 2
    return score


def parse_essential_commands(str):
    str.lower()
    if str == "exit":
        exit(0)
        return True
    elif str == "help":
        print("help")
        return True
    return False


if __name__ == "__main__":
    main()
